from multiprocessing import Process,Queue,Pipe
from user_input import f

if __name__ == '__main__':
    parent_conn,child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print("Output: ",parent_conn.recv())   # prints input