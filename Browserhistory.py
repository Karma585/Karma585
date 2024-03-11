from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

# Visit function
NoOfVisists = int(input("enter the number of url history: "))
print("Enter URLs to visit:")
for i in range(NoOfVisists) :
    url = input("URL: ")
    print(f"visiting {url}")
    backward_history.put(current_page)
    current_page = url

    # Display current page
    print(f"Current page : {current_page}")

    # Go back
    while input("Do you want to go back? (yes/no): ").lower() == 'yes':
        if not backward_history.empty():
            forward_history.put(current_page)
            current_page = backward_history.get()
            print(f"going back to {current_page}")
        else:
            print("No previous page available")

# Go forward
    while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
        if not forward_history.empty():
            backward_history.put(current_page)
            current_page = forward_history.get()
            print(f"Going forward to {current_page}")
        else:
            print("No forward page available")
