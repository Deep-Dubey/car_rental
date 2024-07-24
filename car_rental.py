import datetime

class CarRental:
    def __init__(self, stock=0):
        """
        Constructor for CarRental class.
        """
        self.stock = stock

    def display_stock(self):
        """
        Display the number of available cars.
        """
        print(f"Number of cars available for rent: {self.stock}")
        return self.stock

    def rent_hourly(self, n):
        """
        Rent cars on an hourly basis.
        """
        if n <= 0:
            print("Number of cars should be positive!")
            return None
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} cars available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            rate_per_hour = 5
            estimated_cost = rate_per_hour * n
            print(f"Rented {n} car(s) on an hourly basis at {now}.")
            print(f"Calculation:")
            print(f"   Number of vehicles: {n}")
            print(f"   Rate per hour: ${rate_per_hour}")
            print(f"   Total cost: ${n} * ${rate_per_hour} = ${estimated_cost}")
            print(f"Estimated cost: ${estimated_cost} per hour.")
            self.stock -= n
            return now

    def rent_daily(self, n):
        """
        Rent cars on a daily basis.
        """
        if n <= 0:
            print("Number of cars should be positive!")
            return None
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} cars available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            rate_per_day = 20
            estimated_cost = rate_per_day * n
            print(f"Rented {n} car(s) on a daily basis at {now}.")
            print(f"Calculation:")
            print(f"   Number of vehicles: {n}")
            print(f"   Rate per day: ${rate_per_day}")
            print(f"   Total cost: ${n} * ${rate_per_day} = ${estimated_cost}")
            print(f"Estimated cost: ${estimated_cost} per day.")
            self.stock -= n
            return now

    def rent_weekly(self, n):
        """
        Rent cars on a weekly basis.
        """
        if n <= 0:
            print("Number of cars should be positive!")
            return None
        elif n > self.stock:
            print(f"Sorry! We have currently {self.stock} cars available to rent.")
            return None
        else:
            now = datetime.datetime.now()
            rate_per_week = 60
            estimated_cost = rate_per_week * n
            print(f"Rented {n} car(s) on a weekly basis at {now}.")
            print(f"Calculation:")
            print(f"   Number of vehicles: {n}")
            print(f"   Rate per week: ${rate_per_week}")
            print(f"   Total cost: ${n} * ${rate_per_week} = ${estimated_cost}")
            print(f"Estimated cost: ${estimated_cost} per week.")
            self.stock -= n
            return now

    def return_car(self, request):
        """
        Return rented cars.
        """
        rental_time, rental_basis, num_of_cars = request
        bill = 0

        if rental_time and rental_basis and num_of_cars:
            self.stock += num_of_cars
            now = datetime.datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:  # hourly
                hours = round(rental_period.total_seconds() / 3600)
                bill = hours * 5 * num_of_cars
                print(f"Rental period: {hours} hour(s)")
            elif rental_basis == 2:  # daily
                days = round(rental_period.total_seconds() / (3600 * 24))
                bill = days * 20 * num_of_cars
                print(f"Rental period: {days} day(s)")
            elif rental_basis == 3:  # weekly
                weeks = round(rental_period.total_seconds() / (3600 * 24 * 7))
                bill = weeks * 60 * num_of_cars
                print(f"Rental period: {weeks} week(s)")

            if 3 <= num_of_cars <= 5:
                print("You have an extra 30% discount")
                bill *= 0.7
            elif num_of_cars >= 6:
                print("You have an extra 50% discount")
                bill *= 0.5

            print(f"Thank you for returning your car. Hope you enjoyed our service!")
            print(f"Your bill is ${bill}")
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None
