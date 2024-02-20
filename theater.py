class Seat(object):

    def __init__(self):
        self.price = 0
        self.reserved = False
        self.purchased = False


class Theater(object):

    def __init__(self):
        self.matrix = []
        self.row_size = 40
        self.row_size = 60
        self.full_price = 0
        self.total_free = 0
        self.total_purchased = 0
        self.total_reserved = 0
        self.total_price = 0
        self.total_price_reserved = 0

        while True:
            self.menu_info()
            option = int(input("Enter option: "))

            if option == 1:
                self.row_size = int(input("Enter row size: "))
                self.column_size = int(input("Enter column size: "))
                self.full_price = int(input("Enter total price: "))
                self.total_free = self.row_size * self.column_size
                self.create_matrix()

            elif option == 2:
                if not self.matrix:
                    print("Theater not created, please create")
                    continue
                self.reserve()

            elif option == 3:
                if not self.matrix:
                    print("Theater not created, please create")
                    continue
                self.buy()

            elif option == 4:
                if not self.matrix:
                    print("Theater not created, please create")
                    continue
                
                self.free_seat()

            elif option == 5:
                if not self.matrix:
                    print("Theater not created, please create")
                    continue

                self.end_show() 

            elif option == 10:
                break
            else:
                print("Invalid option")



    def end_show(self):
        total_seats = self.row_size * self.column_size
        sold_seats = sum(1 for row in self.matrix for seat in row if seat.purchased)
        occupancy_percentage = (sold_seats / total_seats) * 100

        if occupancy_percentage < 60:
            print("The show cannot be ended as occupancy is less than 60%.")
            return

        reserved_seats = sum(1 for row in self.matrix for seat in row if seat.reserved and not seat.purchased)
        total_sales = sum(seat.price for row in self.matrix for seat in row if seat.purchased)
        total_reserved_sales = self.total_price_reserved
        total_unsold_seats = self.total_free
        total_unsold_sales = total_unsold_seats * self.full_price

        print("=" * 100)
        print("Total sold seats: ", sold_seats)
        print("Total sales: ", total_sales)
        print("Total reserved seats: ", reserved_seats)
        print("Total reserved sales: ", total_reserved_sales)
        print("Total unsold seats: ", total_unsold_seats)
        print("Total unsold sales: ", total_unsold_sales)
        print("Total show revenue: ", total_sales + total_reserved_sales)
        print("=" * 100)


    def free_seat(self):
        row_number = int(input("Enter row number: "))
        column_number = int(input("Enter column number: "))

        if row_number < 0 or column_number < 0:
            return

        if row_number >= self.row_size or column_number >= self.column_size:
            print("=" * 100)
            print("Invalid size")
            print("-1. Exit")
            self.show_not_purchased()
            print("=" * 100)
            return

        seat = self.matrix[row_number][column_number]

        seat.reserve = False
        seat.purchased = False

        if seat.reserved:
            self.total_free += 1
            self.total_price -= seat.price
            self.total_price_reserved -= seat.price

        if seat.purchased:
            self.total_purchased -= 1

        seat.price = 0
    def buy(self):

        if self.total_purchased == self.row_size * self.column_size:
            print("=" * 100)
            print("Theater is full")
            return

        while self.total_purchased != self.row_size * self.column_size:

            row_number = int(input("Enter row number: "))
            column_number = int(input("Enter column number: "))

            if row_number < 0 or column_number < 0:
                return

            if row_number >= self.row_size or column_number >= self.column_size:
                print("=" * 100)
                print("Invalid size")
                print("-1. Exit")
                self.show_not_purchased()
                print("=" * 100)
                return

            seat = self.matrix[row_number][column_number]

            if seat.reserved and not seat.purchased:
                seat.purchased = True
                seat.price += (70 / 100) * self.full_price
                self.total_purchased += 1
                print("=" * 100)
                print("Purchased with success")
                break

            elif not seat.reserved and not seat.purchased:
                seat.purchased = True
                seat.reserved = True
                seat.price += self.full_price
                self.total_purchased += 1
                print("=" * 100)
                print("Purchased with success")
                break

            elif seat.reserved and seat.purchased:
                print("Already purchased")
                print("-1. Exit")
                self.show_not_purchased()

    def reserve(self):

        while self.total_free:
            row_number = int(input("Enter row number: "))
            column_number = int(input("Enter column number: "))

            if row_number < 0 or column_number < 0:
                break

            if row_number >= self.row_size or column_number >= self.column_size:
                print("=" * 100)
                print("Invalid size")
                print("-1. Exit")
                self.show_free()
                print("=" * 100)
                continue

            seat = self.matrix[row_number][column_number]

            if not seat.reserved:
                seat.reserved = True
                seat.price += (30 / 100) * self.full_price
                self.total_price_reserved += seat.price
                self.total_free -= 1
                print("=" * 100)
                print("Reserved with success, price: ", seat.price)
                break

            else:
                print("Already reserved")
                print("-1. Exit")
                self.show_free()

    def show_free(self):
        print("Free seats: ", self.total_free)
        for i in range(self.row_size):
            for j in range(self.column_size):
                if not self.matrix[i][j].reserved:
                    print(f"[{i},{j}]", end="")
                else:
                    print("[*]", end="")
            print()

    def show_not_purchased(self):
        print("Free seats: ", self.row_size * self.column_size - self.total_purchased)
        for i in range(self.row_size):
            for j in range(self.column_size):
                if not self.matrix[i][j].purchased:
                    print(f"[{i},{j}]", end="")
                else:
                    print("[*]", end="")
            print()

    def create_matrix(self):
        self.matrix = []

        if self.row_size > 60 or self.column_size > 40:
            print("=" * 100)
            print("Invalid size")
        else:

            for _ in range(self.row_size):
                row = []

                for _ in range(self.column_size):
                    row.append(Seat())

                self.matrix.append(row)

            print("=" * 100)
            print("Created with success")

    def menu_info(self):
        print("=" * 100)
        print("1. Create theater\n2. Reserve seat\n3. Buy seat\n5. End show\n10. Exit")
        print("=" * 100)


if __name__ == "__main__":
    t = Theater()
