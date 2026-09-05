def shutdown():
    choice = input("do you want to shut down? (yes/no)")

    if choice.lower() == "yes":
        print("Shutting down the computer...")
    else:
        print("Shutdown cancelled.")

shutdown()