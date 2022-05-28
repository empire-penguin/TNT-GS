from pylsl import StreamInfo, StreamInlet
from data_augmentation import data_augmentor
from joblib import load

info = StreamInfo('Python Stream','Markers',1,0,'string','Test Marker Stream')
info_out = StreamInfo('Python Stream','Markers',1,0,'string','Test Marker Stream')

outlet = StreamInlet(info_out)
inlet = StreamInlet(info)

inlet.open_stream()
clf = load('rf_model.sav')

print('Listening for incoming data... ')
while True:

    received_data = inlet.pull_sample()
    feature_vector = data_augmentor.channel_wise_crop(received_data,150)
    model_output = clf.predict(feature_vector)
    outlet.push_sample(model_output)
