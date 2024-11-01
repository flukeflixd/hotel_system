from module_hotel import *
done = True
while done:
    main_hotel()
    hotel_input = int(input('Select an option: '))
    
    if hotel_input == 1:
        while True:
            room_management()
            room_manage = int(input("Select an option: "))
            if room_manage == 1:
                addroom_hotel()
            elif room_manage == 2:
                view_room()
            elif room_manage == 3:
                room_number = int(input('Room number to edit: '))
                edit_room(room_number)
            elif room_manage == 4:
                room_number = int(input("Room number to delete: "))
                delete_room(room_number)
            elif room_manage == 0:
                break
            else:
                print("Invalid option. Try again.")

    elif hotel_input == 2:
        while True:
            customer_management()
            customer_manage = int(input('Select an option: '))
            if customer_manage == 1:
                customer_name = input('Customer name to edit: ')
                edit_customer(customer_name)
            elif customer_manage == 2:
                view_customer()
            elif customer_manage == 0:
                break
            else:
                print("Invalid option. Try again.")
    elif hotel_input == 3:
        while True:
            booking_management()
            booking_manage = int(input("Select an option: "))
            if booking_manage == 1:
                book_room()
            elif booking_manage == 2:
                view_bookings()
            elif booking_manage == 3:
                booking_id = int(input("Booking ID to cancel: "))
                delete_bookings(booking_id)
            elif booking_manage == 0:
                break
            else:
                print("Invalid option. Try again.")
    elif hotel_input == 4:
        while True:
            reports()
            reports_manage = int(input("Select an option: "))
            if reports_manage == 1:
                reports_date()
            elif reports_manage == 2:
                reports_customer()
            elif reports_manage == 3:
                view_bookings()
            elif reports_manage == 0:
                break
            else:
                print("Invalid option. Try again.")

    elif hotel_input == 0:
        print("Exiting... Thank you! Goodbye!")
        done = False
    else:
        print("Invalid option. Try again.")
