from airline_flight import Flight, AirlineSystem

def main():
    system = AirlineSystem()
    
    # Setup initial flights
    system.add_flight(Flight("A1101", "BOM", "DEL", 5, 4, 2500, 5000))
    system.add_flight(Flight("B2002", "DEL", "CCU", 10, 6, 2000, 4000))
    
    while True:
        print("\n*** Airline Booking System ***")
        print("1. View flights")
        print("2. View seat map")
        print("3. Book a seat")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()
        
        if choice == '1':
            system.list_flights()
            
        elif choice == '2':
            f_no = input("Enter Flight Number: ").upper()
            flight = system.find_flight(f_no)
            if flight:
                flight.show_seat_map()
            else:
                print("❌ Flight not found.")
                
        elif choice == '3':
            f_no = input("Enter Flight Number: ").upper()
            flight = system.find_flight(f_no)
            
            if not flight:
                print("❌ Flight not found.")
                continue
            
            flight.show_seat_map()
            seat_id = input("Enter Seat (e.g., 1A): ").upper()
            p_name = input("Enter Passenger Name: ").strip()
            
            booking_obj = flight.book_seat(seat_id, p_name)
            
            if booking_obj:
                # Save to external file
                with open("bookings.txt", "a") as f:
                    f.write(booking_obj.to_text() + "\n")
                system.save_log(f"BOOKED {f_no} {seat_id}")
                print(f"✅ Success! Price: {booking_obj.price}")
            else:
                print("❌ Seat unavailable or invalid format.")
        
        elif choice == '4':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()