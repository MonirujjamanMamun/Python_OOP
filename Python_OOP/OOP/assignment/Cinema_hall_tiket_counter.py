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
            print(f"Error: Show ID {id} does not exist.")
            return

        for seat in seat_list:
            row, col = seat
            if (0 <= row < self.rows and 0 <= col < self.cols and self.seats[id][row][col] == 0):
                self.seats[id][row-1][col-1] = 0
                print(
                    f"Seat ({row}, {col}) booked for show {id}.")
            elif self.seats[id][row-1][col-1] == 1:
                print(f"Seat ({row}, {col}) is already booked for show {id}.")
            else:
                print(f"Error: Seat ({row}, {col}) is invalid for show {id}.")

    def view_show_list(self):
        print("LIST OF SHOWS:")
        print('--------------')
        for show in self.show_list:
            print(
                f"Show ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}")

    def view_available_seats(self, id):
        if id not in self.seats:
            print(f"Error: Show ID {id} does not exist.")
            return
        print('--------------')
        print(f"Available seats for Show {id}:")
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] == 0:
                    print(f"Seat ({row + 1}, {0}) is available.")
                else:
                    print(f"Seat ({row + 1}, {1}) is not available.")


hall1 = Hall(3, 3, 1)
hall1.entry_show("1", "Avengers:Endgame", "10:00 AM")
hall1.entry_show("2", "Avatar", "2:00 PM")

while True:
    print("1: VIEW ALL SHOW TODAY")
    print("2: VIEW AVAILABLE SEATS")
    print("3: BOOK TICKET")
    print("4: EXIT")
    option = int(input("ENTER OPTION: "))

    if option == 1:
        print('--------------')
        hall1.view_show_list()
        print('--------------')
    elif option == 2:
        print('--------------')
        show_id = input("ENTER SHOW ID: ")
        hall1.view_available_seats(show_id)
    elif option == 3:
        print('--------------')
        show_id = input("ENTER SHOW ID: ")
        print('--------------')
        num_seats = int(input("NUMBER OF TICKETS?: "))
        seat_list = []
        for seat in range(num_seats):
            row = int(input("ENTER SEAT ROW : "))
            col = int(input("ENTER SEAT COL : "))
            seat_list.append((row, col))
        hall1.book_seats(show_id, seat_list)
    elif option == 4:
        break
