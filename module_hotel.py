from menu import *

def report_add_room(addroom_hotel):
    with open('addroom.txt', 'a') as f: 
        textfile = ','.join(map(str, addroom_hotel)) 
        f.write(textfile + '\n') 

def report_add_customer(add_customer):
    with open('addcustomer.txt', 'a') as f: 
        textfile = ','.join(map(str, add_customer)) 
        f.write(textfile + '\n')  

def select_room(number):
    if number == '1':
        return "Budget Class"
    elif number == '2':
        return "Standard Class"
    elif number == '3':
        return "Luxury Class"
    else:
        number != '1' or number != '2' or number != '3'
        return 'Error Select room'
    
def select_status(number):
    if number == '1':
        return "Free"
    elif number == '2':
        return "Full"
    else:
        return 'Error Status room'

def addroom_hotel():
    room_hotel = input("Add room ID: ")
    type_room()  
    type_hotel = input("Add type room: ")
    select = select_room(type_hotel)  
    price_hotel = int(input("Add price room: "))
    status_room()
    select_status_number = input("Add status room : ")
    status = select_status(select_status_number)
    if status == "Error Status room":
        print("Invalid status room. Please enter either 1 or 2.")
        return 
    room_details = [room_hotel, select, price_hotel, status]
    report_add_room(room_details)

def view_room():
    with open('addroom.txt', 'r') as f:  
        view_room = f.readlines() 
        print("=" * 72)
        print("| {:^15} | {:^15} | {:^15} | {:^15}|".format("Room ID", "Type room", "Price hotel","Status"))
        print("=" * 72)
        for line in view_room:
            room_name, type_room, price, status = line.strip().split(',')
            print("| {:^15} | {:^15} | {:^15} | {:^15}|".format(room_name, type_room, price,status))
            print('-' * 72)
        print("=" * 72)

def edit_room(edit_room_id : int):
    with open('addroom.txt', 'r') as f:
        view_room = f.readlines()
        
    with open('addroom.txt', 'w') as f:
        for i in view_room:
            room_data = i.strip().split(',')  
            if int(room_data[0]) == edit_room_id:
                edit_new_room = addroom_hotel()
                print(edit_new_room)
            else:
                f.write(i)
             
def delete_room(delete_room: int):
    with open('addroom.txt', 'r') as f:
        rooms = f.readlines() 
    room_found = False
    with open('addroom.txt', 'w') as f:
        for room in rooms:
            room_data = room.strip().split(',')  
            if int(room_data[0]) == delete_room:
                 room_found = True
                 print(f"Room {delete_room} has been successfully removed.")
            else:
                 f.write(room)
    if not room_found:
        print(f'This room {delete_room} does not exist. Cannot be deleted.')

def add_customer():
    name_customer = input("Add Name customer: ")

    while True:
        tel_customer = input("Add Tel customer: ")
        if tel_customer.isdigit() and len(tel_customer) == 10:
            print("Customer Tel added successfully.")
            break
        else:
            print("Tel not correct. Please use a valid 10-digit Tel.")

    while True:
        email_customer = input("Add Email customer: ")
        if '@gmail.com' in email_customer:
            print("Customer information added successfully.")
            break
        else:
            print("Email not correct. Please use a valid Gmail address.")
    
    room_id = input("Enter room ID to book: ")
    check_in_date = input("Check-in date (YYYY-MM-DD): ")
    check_out_date = input("Check-out date (YYYY-MM-DD): ")
    return f"{name_customer},{tel_customer},{email_customer} ,{room_id},{check_in_date},{check_out_date}\n"


def view_customer():
    with open('bookings.txt', 'r') as f:  
        view_customer = f.readlines() 
        print("=================================================================================")
        print("| {:^5} | {:^20} | {:^15} | {:^28} |".format("No.", "Name Customer", "Tel Customer", "Email Customer"))
        print("=================================================================================")
        index = 1
        for line in view_customer:
            data = line.strip().split(',')
            if len(data) >= 3:
                name, tel, email = data[:3]
                print("| {:^5} | {:^20} | {:^15} | {:^28} |".format(index, name, tel, email))
                print("---------------------------------------------------------------------------------")
                index += 1
        print("=================================================================================")

def edit_customer(edit_customer_id):
    with open('bookings.txt', 'r') as f:
        view_customer = f.readlines()
    
    customer_found = False
    updated_customers = []

    for line in view_customer:
        customer_data = line.strip().split(',')
        
        if customer_data[0] == edit_customer_id:
            print(f"Editing customer with ID: {edit_customer_id}")
            updated_customer = add_customer()
            updated_customer_line = f"{updated_customer}"
            updated_customers.append(updated_customer_line)
            print('-------------------------------------------------------------------------')
            print(f"Customer {edit_customer_id} has been successfully edited.")
            customer_found = True
        else:
            updated_customers.append(line.strip())
    final_data = ','.join(updated_customers)
    with open('bookings.txt', 'w') as f:
        f.write(final_data)
    if not customer_found:
        print(f"Customer {edit_customer_id} does not exist. Cannot be edited.")

def book_room():
    print("=== Book a Room ===")
    try:
        with open('bookings.txt', 'r+') as f:
            lines = f.readlines()
            if lines and not lines[-1].endswith('\n'):
                f.write('\n')

        with open('bookings.txt', 'a') as f:
            name_customer = input("Enter customer's name: ")
            while True:
                tel_customer = input("Enter customer's phone number: ")
                if tel_customer.isdigit() and len(tel_customer) == 10:
                    break
                else:
                    print("Invalid phone number. Please enter a valid 10-digit phone number.")
            while True:
                email_customer = input("Enter customer's email address: ")
                if '@gmail.com' in email_customer:
                    break
                else:
                    print("Invalid email address. Please enter a valid Gmail address.")
            view_room()  
            room_id = input("Enter room ID to book: ")
            checkin_date = input("Enter check-in date (YYYY-MM-DD): ")
            checkout_date = input("Enter check-out date (YYYY-MM-DD): ")
            booking_details = [name_customer, tel_customer, email_customer, room_id, checkin_date, checkout_date]
            booking_text = ','.join(booking_details)
            f.write(booking_text + '\n')
            print(f"Room {room_id} has been successfully booked by {name_customer} from {checkin_date} to {checkout_date}.\n")

        # บันทึก user.txt
        with open('user.txt', 'a') as user_file:
            user_details = [name_customer, tel_customer, email_customer]
            user_text = ','.join(user_details)
            user_file.write(user_text + '\n')

        # อัปเดต addroom.txt
        try:
            with open('addroom.txt', 'r') as room_file:
                room_lines = room_file.readlines()

            updated_room_lines = []
            for line in room_lines:
                room_data = line.strip().split(',')
                if room_data[0] == room_id and room_data[-1] == 'Free':
                    room_data[-1] = 'Full'
                    updated_line = ','.join(room_data)
                    updated_room_lines.append(updated_line + '\n')
                else:
                    updated_room_lines.append(line)

            with open('addroom.txt', 'w') as room_file:
                room_file.writelines(updated_room_lines)

        except Exception as e:
            print(f"error addroom.txt: {e}")

    except Exception as e:
        print(f"An error occurred while booking the room: {e}")


def view_bookings():
    try:
        with open('bookings.txt', 'r') as f:
            view_booking = f.readlines()
            if not view_booking:
                print("No bookings found.")
                return
            
            print("=" * 135)
            print("| {:^5} | {:^20} | {:^15} | {:^28} | {:^15} | {:^15} | {:^15} |".format("No.", "Name Customer", "Tel Customer", "Email Customer", "Room ID", "Check-in Date", "Check-out Date"))
            print("=" * 135)

            index = 1
            for line in view_booking:
                if line.strip():
                    name, tel, email, room_id, checkin_date, checkout_date = line.strip().split(',')
                    print("| {:^5} | {:^20} | {:^15} | {:^28} | {:^15} | {:^15} | {:^15} |".format(index, name, tel, email, room_id, checkin_date, checkout_date))
                    print('-' * 135)
                    index += 1

            print("=" * 135)

    except FileNotFoundError:
        print("No bookings found. The bookings file does not exist.")


def delete_bookings(delete_room: int):
    with open('bookings.txt', 'r') as f:
        rooms = f.readlines() 
    room_found = False
    with open('bookings.txt', 'w') as f:
        for room in rooms:
            room_data = room.strip().split(',')  
            if int(room_data[3]) == delete_room:
                 room_found = True
                 print(f"Room {delete_room} has been successfully removed.")
            else:
                 f.write(room)
    if not room_found:
        print(f'This room {delete_room} does not exist. Cannot be deleted.')

def reports_date():
    try:
        with open('bookings.txt', 'r') as f:
            view_booking = f.readlines()
            if not view_booking:
                print("No bookings found.")
                return

            start_date = input("Enter start date to filter (YYYY-MM-DD): ")
            end_date = input("Enter end date to filter (YYYY-MM-DD): ")

            print("=" * 127)
            print("| {:^20} | {:^15} | {:^28} | {:^15} | {:^15} | {:^15} |".format("Name Customer", "Tel Customer", "Email Customer", "Room ID", "Check-in Date", "Check-out Date"))
            print("=" * 127)

            booking_found = False
            for line in view_booking:
                if line.strip():
                    name, tel, email, room_id, checkin_date, checkout_date = line.strip().split(',')
                    if (start_date <= checkin_date <= end_date) or (start_date <= checkout_date <= end_date):
                        print("| {:^20} | {:^15} | {:^28} | {:^15} | {:^15} | {:^15} |".format(name, tel, email, room_id, checkin_date, checkout_date))
                        print('-' * 127)
                        booking_found = True

            if not booking_found:
                print(f"No bookings found between {start_date} and {end_date}.")
            print("=" * 127)

    except FileNotFoundError:
        print("No bookings found. The bookings file does not exist.")

def reports_customer():
    try:
        with open('bookings.txt', 'r') as f:
            view_booking = f.readlines()
            if not view_booking:
                print("No bookings found.")
                return
            
            customer_name = input("Enter customer name to filter: ")
            print("=" * 127)
            print("| {:^20} | {:^15} | {:^28} | {:^15} | {:^15} | {:^15} |".format("Name Customer", "Tel Customer", "Email Customer", "Room ID", "Check-in Date", "Check-out Date"))
            print("=" * 127)

            booking_found = False
            for line in view_booking:
                if line.strip():
                    name, tel, email, room_id, checkin_date, checkout_date = line.strip().split(',')

                    if name.lower() == customer_name.lower():
                        print("| {:^20} | {:^15} | {:^28} | {:^15} | {:^15} | {:^15} |".format(name, tel, email, room_id, checkin_date, checkout_date))
                        print('-' * 127)
                        booking_found = True

            if not booking_found:
                print(f"No bookings found for customer: {customer_name}")
            print("=" * 127)
            
    except FileNotFoundError:
        print("No bookings found. The bookings file does not exist.")
