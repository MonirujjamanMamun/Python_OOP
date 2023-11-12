class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        super().__init__()
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)

        self.seats[id] = []
        for row in range(self.rows):
            row_data = []
            for col in range(self.cols):
                row_data.append(0)
            self.seats[id].append(row_data)

    def book_seats(self, id, seat_list):
        if id not in self.seats:
            print(f"Error: Show with ID {id} does not exist.")
            return

        for seat in seat_list:
            row, col = seat
            if (0 <= row < self.rows and 0 <= col < self.cols and self.seats[id][row][col] == 0):
                self.seats[id][row-1][col-1] = 1
                print(
                    f"Seat ({row}, {col}) booked successfully for show {id}.")
            elif self.seats[id][row-1][col-1] == 1:
                print(f"Seat ({row}, {col}) is already booked for show {id}.")
            else:
                print(f"Error: Seat ({row}, {col}) is invalid for show {id}.")

    def view_show_list(self):
        print("List of Shows:")
        for show in self.show_list:
            print(f"Show ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.seats:
            print(f"Error: Show with ID {id} does not exist.")
            return

        print(f"Available seats for Show ID {id}:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == 0:
                    print(f"Seat ({row + 1}, {0}) is available.")
                else:
                    print(f"Seat ({row + 1}, {1}) is not available.")


# # Example usage:
# hall1 = Hall(3, 4, 1)
# hall1.entry_show(1, "Movie A", "2:00 PM")
# hall1.entry_show(2, "Movie B", "4:30 PM")

# hall2 = Hall(2, 3, 2)
# hall2.entry_show(3, "Movie C", "3:15 PM")

# hall1.view_show_list()
# hall2.view_show_list()

# hall1.book_seats(1, [(0, 0), (1, 1), (2, 2)])
# hall1.book_seats(2, [(0, 0), (0, 1), (1, 2)])

# hall1.view_available_seats(1)
# hall2.view_available_seats(3)

# while True:
#     print("1: VIEW ALL SHOW TODAY")
#     print("2: VIEW AVAILABLE SEATS")
#     print("3: BOOK TICKET")
#     print("4: EXIT")
#     option = int(input("ENTER OPTION: "))
#     if option == 1:
#         hall.view_show_list()
#     elif option == 2:
#         hall.view_available_seats(1)
#     elif option == 3:
#         rows = int(input('ENTER ROWS: '))
#         cols = int(input('ENTER COLS: '))
#         hall_no = int(input('ENTER HALL_NO: '))
#         hall = Hall(rows, cols, hall_no)
#         hall.entry_show(1, "Movie A", "2:00 PM")
#     elif option == 4:
#         break

# Example usage:
hall1 = Hall(5, 5, 1)
hall1.entry_show("1", "Movie 1", "10:00 AM")
hall1.entry_show("2", "Movie 2", "2:00 PM")

while True:
    print("1: VIEW ALL SHOW TODAY")
    print("2: VIEW AVAILABLE SEATS")
    print("3: BOOK TICKET")
    print("4: EXIT")
    option = int(input("ENTER OPTION: "))

    if option == 1:
        hall1.view_show_list()
    elif option == 2:
        show_id = input("Enter show ID: ")
        hall1.view_available_seats(show_id)
    elif option == 3:
        show_id = input("Enter show ID: ")
        num_seats = int(input("Enter the number of seats: "))
        seat_list = []
        for seat in range(num_seats):
            # row_col = input("Enter row and column (e.g., 1 2): ").split()
            # row, col = map(int, row_col)
            row = int(input("Enter row : "))
            col = int(input("Enter col : "))
            seat_list.append((row, col))
        hall1.book_seats(show_id, seat_list)
    elif option == 4:
        break
