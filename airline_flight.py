import datetime

class Booking:
    def __init__(self, flight_no, seat_id, passenger_name, price):
        self.flight_no = flight_no
        self.seat_id = seat_id
        self.passenger_name = passenger_name
        self.price = price
        self.timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_text(self):
        return f"{self.timestamp} | Flight: {self.flight_no} | Seat: {self.seat_id} | Name: {self.passenger_name} | Price: {self.price}"

class Flight :
    def __init__(self, flight_no, origin, destination, rows, cols, economy_price, business_price):
        self.flight_no = flight_no
        self.origin = origin
        self.destination = destination
        self.rows = rows
        self.cols = cols
        self.economy_price = economy_price
        self.business_price = business_price
        # Create a grid of seats: None means available, String means Passenger Name
        self.seats = [[None for _ in range(cols)] for _ in range(rows)]

    def show_seat_map(self):
        print(f"\n--- Seat Map for {self.flight_no} ---")
        header = "   " + " ".join([chr(65 + i) for i in range(self.cols)])
        print(header)
        for r in range(self.rows):
            row_str = f"{r+1:2} "
            for c in range(self.cols):
                row_str += "X " if self.seats[r][c] else ". "
            print(row_str)
        print("(. = Available, X = Booked)")

    def book_seat(self, seat_id, passenger_name):
        try:
            # Convert "3B" to row 2, col 1
            row = int(seat_id[:-1]) - 1
            col = ord(seat_id[-1]) - 65
            
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[row][col] is None:
                    self.seats[row][col] = passenger_name
                    # Simple pricing: first 2 rows are business
                    price = self.business_price if row < 2 else self.economy_price
                    return Booking(self.flight_no, seat_id, passenger_name, price)
            return None
        except (ValueError, IndexError):
            return None

class AirlineSystem:
    def __init__(self):
        self.flights = {}

    def add_flight(self, flight):
        self.flights[flight.flight_no] = flight

    def find_flight(self, flight_no):
        return self.flights.get(flight_no)

    def list_flights(self):
        print("\nAvailable Flights:")
        for f in self.flights.values():
            print(f"{f.flight_no}: {f.origin} -> {f.destination}")

    def save_log(self, message):
        with open("system_log.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {message}\n")