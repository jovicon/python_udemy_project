from classes.clientClass import client
from classes.printerClass import printer

menu_option = 0
list_clients = []

printer_object = printer()
printer_object.welcome_message()

while menu_option != 4:

    printer_object.choose_options()
    menu_option = int(input("Choose an options: "))

    if menu_option == 1:

        name = input("Please write the client name: ")
        last_name = input("Please write client last name: ")
        age = input("Please write the client age: ")
        weight = input("Please write the client weight: ")
        smoke = input("Does the client smoke?: ")
        print("\n")

        new_client = client(name,last_name,age,weight,smoke)
        list_clients.append(new_client)

    elif menu_option == 2:
        name_to_search = input("insert a name to search client, please: ")
        last_name_to_search = input("insert a name to search client, please: ")

        for client_from_list in list_clients:
            if client_from_list.name.upper() == name_to_search.upper() and client_from_list.last_name.upper() == last_name_to_search.upper():
                print("Yes, we know your client: ")
                print(vars(client_from_list))
                print("\n")


    elif menu_option == 3:
        for client_from_list in list_clients:
            print(vars(client_from_list))

    else:
        print("Please choose a good option.")
        print("\n")

    if menu_option == 4:
        print("Thanks for use our system.")
        print("Good bye.")