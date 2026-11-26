from movie_booking.movie import Movie
from movie_booking.customer import Customer
from movie_booking.booking_system import BookingSystem


class BookingDriver:
    def __init__(self):
        self.system = BookingSystem()
        self.movie = None
        self.customer = None
        self.result = None

    def create_movie(self, title, seats):
        self.movie = Movie(title, seats)

    def create_customer(self, name, age):
        self.customer = Customer(name, age)

    def book_tickets(self, count):
        self.result = self.system.book_ticket(
            self.customer,
            self.movie,
            count
        )
        return self.result
    
    # Given
    def given_movie_has_seats(self, seats):
        self.movie = Movie("Test Movie", seats)

    def given_customer_age(self, age):
        self.customer = Customer("Test Customer", age)

    # When
    def when_customer_books(self, tickets):
        self.result = self.system.book_ticket(
            self.customer,
            self.movie,
            tickets
        )

    # Then
    def booking_succeeds(self):
        return self.result["success"]

    def booking_fails(self):
        return not self.result["success"]

    def seats_remaining(self):
        return self.movie.available_seats

    def message(self):
        return self.result["message"]
