#creating empty dictionary
contacts = {}

while True:
    print("\nContact book app")
    print("1.Create contact")
    print("2.View contact")
    print("3.Update contact")
    print("4.Delete contact")
    print("5.search contact")
    print("6.count contact")
    print("7.Exit")

    choice = input("enter your choice...")
    if choice == '1':
        name = input('enter name')
        if name in contacts:
            print(f'{name} already exist')

        else:
            mobile = input("enter no.")
            email = input("enter email..")
            age = input("enter age")

            contacts[name] = {'mobile':mobile, 'email': email,'age':int(age)}

            print(f"contact {name} has been created successfully")
    elif choice == '2':
        name = input('enter name')
        if name in contacts:
            contact = contacts[name]
            print(f"name: {name} ; mobile:{contact['mobile']} ; email:{contact['email']} ; age:{contact['age']}")
        else:
            print("contact not exist")
    elif choice == '3':
        name = input('enter contact name')
        if name in contacts:
             mobile = input("enter no.")
             email = input("enter email..")
             age = input("enter age")

             contacts[name] = {'mobile':mobile, 'email': email,'age':int(age)}
        else:
            print("contact not found")

    elif choice == '4':
        name = input("enter name ")
        if name in contacts:
            del contacts[name]
            print("contact deleted ")
        else:
            print("contact not found")
    elif choice == '5':
        search_name = input("enter name")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"name:{name}, mobile:{contact['mobile']}, email:{contact['email']}")
                found = True
        if not found:
            print("contact not found")
    elif choice == '6':
        print(f"total contacts = {len(contacts)}")

    elif choice == '7':
        print("good bye")
        break

    else:
        print("invalid input")
