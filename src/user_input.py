from multiprocessing import Process, Pipe

def user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
        #Add Dictionary Mapping for num to gesture in user output?
    except ValueError:
            print("Not an integer")
    else:
        if val in range(0,6):
          pass
        else:
          print("Please type an integer in [0,5]")

def f(child_conn):
    msg = user_input(input("Enter an Integer: "))
    child_conn.send(msg)
    child_conn.close()