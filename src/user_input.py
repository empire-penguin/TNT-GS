def user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print("Input is an integer number. Number = ", val)
        #Add Dictionary Mappinng for num to gesture in user output?
    except ValueError:
            print("Not an integer")
    else:
        if input in range(0,6):
          break
        else
          print("Please type an integer in [0,5]")


input1 = input("Enter an Integer")
check_user_input(input1)
