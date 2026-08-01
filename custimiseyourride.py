print("Select your ride: ")
print("1. Bike")
print("2. Car")



choice = int(input("Enter your choice: "))


if( choice == 1 ):
    print( "what type of bike? " )
    print("1.Scooty\n")
    print("2.Scooter\n")


    choice2=int(input("Enter your choice2"))
    if choice2==1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")


elif( choice == 2 ):
    print( "what type of car?" )