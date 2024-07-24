class Customer:
    def __init__(self):
        """
        Constructor for Customer class.
        """
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = 0

    def request_car(self):
        """
        Request a car from the CarRental shop.
        """
        cars = input("How many cars would you like to rent? ")
        try:
            cars = int(cars)
        except ValueError:
            print("Number of cars should be a positive integer.")
            return -1
        if cars < 1:
            print("Number of cars should be greater than zero.")
            return -1
        else:
            self.cars = cars
        return self.cars

    def return_car(self):
        """
        Return the rented car to the CarRental shop.
        """
        if self.rental_basis and self.rental_time and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0
