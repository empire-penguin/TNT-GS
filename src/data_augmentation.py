from numpy import arange
from tsaug import AddNoise,Crop
from numpy import array,reshape
import warnings
from data_visualizer import data_extractor
from dataset import dataset
from numpy import concatenate
from pickle import dump

warnings.filterwarnings('ignore')

class data_augmentor():

    def __init__(self,path_to_json):
        self.extractor = data_extractor(path_to_json)
        self.path_to_json = path_to_json

    '''
    Performing a crop through each channel and reshaping each channel wise crop into just one list.
    Unlike the below impementation with the TSAUG library that merges the channel observaitons into one list
    and haphazardly performs a channel wise crop in a more random fashion
    
    MAKE SURE SERIES IS A NUMPY ARRAY. INDEX SLICING DONE BELOW IS NOT DOABLE FOR STANDARD PYTHON LISTS
    '''
    @staticmethod
    def channel_wise_crop(self,series,crop_size):

        num_crops = int(len(series[0])/crop_size)
        crop_idxs = arange(0,num_crops)

        return list(map(
            lambda idx:reshape(series[:,(idx*crop_size):(idx*crop_size)+crop_size],[
                self.extractor.NUM_CHANNELS*crop_size,-1]),
            crop_idxs
        ))

    '''
    Achieves same as above function, but allowing for cross over of crops (again, channel_wise)
    '''
    def crossover_channel_wise_crop(self,series,crop_size,cross_over_proportion):
        idx_jump = int(crop_size * cross_over_proportion)
        num_crops = int((self.extractor.TIME_OBV - self.extractor.CUTOFF - crop_size) / (crop_size*cross_over_proportion))+1
        crop_idxs = arange(0,num_crops)

        return list(map(
            lambda idx:reshape(series[:,(idx*idx_jump):(idx*idx_jump)+crop_size],
            [self.extractor.NUM_CHANNELS*crop_size,]),
            crop_idxs
        ))


    ''' 
        Applies crossover, but not in a channelwise manner as was done with the above functions
    '''

    '''
        Adds noise to a single observation across channels by sampling randomly
        from a normal distribution specified by the loc and scale parameters below.
        Can also perform multiple times through manipulation of 'repeats' parameter.
        Instead of adding noise for individual channels, we are combining them into one distribution 
        (can see clearly with the jump discontinuities, and adding noise to the whole series)
    '''
    def jitter(self,label,observation,loc,scale,repeats):
        obv = array(self.extractor.get_observation(label,observation)).reshape(1,-1)
        return AddNoise(loc,scale,repeats=repeats).augment(obv)

    '''
        Performs same objective as above, but now for each observation in a label.
        e.g if label L has 10 observations, which is the case for us, and we
        extract 10 more observations from each label, now we have 100. Can see how this is useful for
        data augmentation especially when we crop those augmented distributions, and then even
        sample with replacement later on
    '''
    def jitter_full_dist(self,label,loc,scale,repeats):
        obvs = arange(1,self.extractor.NUM_OBVS+1)
        return reshape(list(map(
            lambda obv:self.jitter(label,obv,loc,scale,repeats),
            obvs
        )),[self.extractor.NUM_OBVS*repeats,-1])


    def crop_series(self,series,num_crops,size_crop):
        return Crop(size_crop,repeats=num_crops).augment(series)

    def build_dataset(self,labels,loc,scale,repeats,num_crops,size_crop):
        x = []
        y = []

        num_obvs_per = self.extractor.NUM_OBVS * repeats * num_crops
        for label in labels:
            jitter_series = self.jitter_full_dist(label,loc,scale,repeats)
            cropped_series = self.crop_series(jitter_series, num_crops, size_crop)
            x.append(cropped_series),y.extend([label]*num_obvs_per)

        return reshape(x,[num_obvs_per*len(labels),size_crop]),y

    def build_dataset_channel_wise(self,labels,loc,scale,repeats,crop_size,crossover_proportion):
        x = []
        y = []

        num_crops = int((self.extractor.TIME_OBV - self.extractor.CUTOFF - crop_size) / (crop_size*crossover_proportion))+1

        r_idx_0 = self.extractor.NUM_OBVS * repeats
        r_idx_1 = self.extractor.TIME_OBV - self.extractor.CUTOFF

        for label in labels:
            jitter_series = reshape(self.jitter_full_dist(label, loc, scale, repeats),
                            [r_idx_0,self.extractor.NUM_CHANNELS,r_idx_1])

            x.extend(
                list(map(
                    lambda series:self.crossover_channel_wise_crop(series,crop_size,crossover_proportion),
                    jitter_series
                ))
            ),y.extend([label]*repeats*self.extractor.NUM_OBVS*num_crops)

        num_elements = repeats * self.extractor.NUM_OBVS * num_crops * len(labels)
        x = reshape(x,[num_elements,self.extractor.NUM_CHANNELS*crop_size])

        return x,y


