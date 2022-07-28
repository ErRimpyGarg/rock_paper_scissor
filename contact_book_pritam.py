# Contact Book App

print("Welcome to Contact Book App!")

# Menus
menus = ['Add Contact', 'Show Contacts', 'Update Contact', 'Delete Contact', 'Quit']

# Empty Contact Book
contacts = {}

while True:
# Loops to show menu
    for i in range(len(menus)):
        print(f"{i+1}: {menus[i]}")
        
    # User Choice
    user_choice = input("Choose from the above menu: ")
    if not user_choice.isnumeric():
    	print("Please enter valid option.")

    if user_choice == "1":
        name = input("Enter name: ")
        if not name.isalpha():
        	print("Please enter alphabets only")
        	
        number = input("Enter number: ")
        if not number.isnumeric():
        	print("Please enter numbers only.\n")
        choice = input("Do you want to add this contact? y or n: ").lower()
        if not choice=="y" or choice=="n":
        	print("Please enter valid choice.")
        elif choice == "y":
            contacts.update({name:number})
            print("Your contact has been added!")
        else:
            print("Please add new contact.")
        print("\n")

    elif user_choice == "2":
    	if not user_choice.isnumeric():
    		print("Enter valid choice.")
        	'print("Your all contacts are: ")
        for key,value in contacts.items():
            print(f"{key}:{value}")
        print("\n")

   
    elif user_choice == "3":
        print("Your all contacts are: ")
        for key,value in contacts.items():
          print(f"{key}:{value}")
        print("\n")
        update_name = input("Enter the name you want to update: ")
        update_number = input("Enter the number: ")
        for key, value in contacts.items():
            if key == update_name:
                contacts[key] = update_number
                print("Your number has been updated!")

        print("\n")


    elif user_choice == "4":
        print("Your all contacts are: ")
        for key,value in contacts.items():
            print(f"{key}:{value}")
        print("\n")
        delete_name = input("Enter the name you want to update: ")
        if delete_name in contacts:
            contacts.pop(delete_name)
            print("Your contact has been deleted!")

        print("\n")


    elif user_choice == "5":
        print("Thanks for using our contact book application!")
        break

