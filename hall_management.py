class Star_Cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()  
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.initialize_seats()

        Star_Cinema.entry_hall(self)  

    def initialize_seats(self):
        for show_id in range(1, len(self.show_list) + 1):
            self.seats[show_id] = [[0] * self.cols for _ in range(self.rows)]

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        self.seats[id] = [[0] * self.cols for _ in range(self.rows)]

    def book_seats(self, show_id, seats_to_book):
        if show_id not in self.seats:
            print("Error: Invalid show ID")
            return

        if show_id not in [show[0] for show in self.show_list]:
            print("Error: Invalid movie ID")
            return

        for seat in seats_to_book:
            row, col = seat
            if not (1 <= row <= self.rows) or not (1 <= col <= self.cols):
                print("Error: Invalid seat")
                continue

            if self.seats[show_id][row - 1][col - 1] == 1:
                print("Error: Seat already booked")
                continue

            self.seats[show_id][row - 1][col - 1] = 1

    def view_show_list(self):
        for show_info in self.show_list:
            print(f"Show ID: {show_info[0]}, Movie: {show_info[1]}, Time: {show_info[2]}")

    def view_available_seats(self, show_id):
        if 1 <= show_id <= len(self.show_list):
            show = self.show_list[show_id - 1]
            print(f"Available seats for Show {show[0]} - {show[1]} ({show[2]}):")
            for row in range(self.rows):
                row_str = ' '.join(str(seat) for seat in self.seats[show_id][row])
                print(f"[{row_str}]")
        else:
            print("Error: Invalid show ID")

hall1 = Hall(rows=6, cols=6, hall_no=1)
hall1.entry_show(id=1, movie_name="JAWAN", time="10:00 AM")
hall1.entry_show(id=2, movie_name="Leo", time="2:00 PM")
hall1.entry_show(id=3, movie_name="Dunki", time="8:00 PM")

while True:
    print("\nOptions:")
    print("1. View Show List")
    print("2. View Available Seats")
    print("3. Book Seats")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hall1.view_show_list()
    elif choice == "2":
        show_id = int(input("Enter show ID: "))
        hall1.view_available_seats(show_id)
    elif choice == "3":
        show_id = int(input("Enter show ID: "))
        if show_id not in [show[0] for show in hall1.show_list]:
            print("Error: Invalid movie ID")
            continue
        num_seats = int(input("Enter the number of seats to book: "))
        seats_to_book = []
        for _ in range(num_seats):
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            hall1.book_seats(show_id, [(row, col)])
            print("Seats booked successfully.")
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
