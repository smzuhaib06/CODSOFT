contacts={}

def add():
    name=input("Enter Name: ")
    phone=input("Enter Phone Number: ")
    email=input("Enter Email Address: ")
    address=input("Enter Address: ")
    
    contacts[name]={
        'Phone':phone , 'Email':email , 'Address':address
    }
    
    print(name + "has been added.\n")
    
def  view():
    if len(contacts)==0:
        print("No Contacts Found.\n")
    else:
        print("Contacts List: ")
        for name,info in contacts.items():
            print("Name: "+ name + ", Phone: "+ info['Phone'])
        print()
        
def search():
    search_item=input("Enter Name or Phone Number to Search: ")
    found=False
    for name,info in contacts.items():
        if search_item.lower() in name.lower() or search_item==info['Phone']:
            print("\nFound Contact:")
            print("Name: " + name)
            print("Phone: " + info['Phone'])
            print("Email: " + info['Email'])
            print("Address: " + info['Address'] + "\n")
            found = True
            break
    if not found:
        print("No Contacts Found.\n")
        
def update():
    name=input("Enter Name of Contact to Update: ")
    
    if name in contacts:
        print("\nCurrent details:")
        print("Phone: " + contacts[name]['phone'])
        print("Email: " + contacts[name]['email'])
        print("Address: " + contacts[name]['address'] + "\n")

        phone = input("Enter New Phone Number (leave blank to keep current): ")
        email = input("Enter New Email Address (leave blank to keep current): ")
        address = input("Enter New Address (leave blank to keep current): ")

        if phone != "":
            contacts[name]['phone'] = phone
        if email != "":
            contacts[name]['email'] = email
        if address != "":
            contacts[name]['address'] = address
        
        print(name + "'s contact information has been updated.\n")
    else:
        print("No contact found with that name.\n")

def delete():
    name = input("Enter the Name of the Contact to Delete: ")

    if name in contacts:
        del contacts[name]
        print(name + " has been deleted.\n")
    else:
        print("No contact found with that name.\n")

def contacts_book():
    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add()
        elif choice == '2':
            view()
        elif choice == '3':
            search()
        elif choice == '4':
            update()
        elif choice == '5':
            delete()
        elif choice == '6':
            print("Exited")
            break
        else:
            print("Invalid option, try again.\n")

contacts_book()
    