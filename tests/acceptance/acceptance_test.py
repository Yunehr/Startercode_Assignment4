from drivers.booking_driver import BookingDriver


def test_successful_booking():
    # Given
    driver = BookingDriver()
    driver.given_movie_has_seats(20)
    driver.given_customer_age(25)

    # When
    driver.when_customer_books(2)

    # Then
    assert driver.booking_succeeds()
    assert driver.seats_remaining() == 18


def test_book_last_tickets():
    # Given
    driver = BookingDriver()
    driver.given_movie_has_seats(5)
    driver.given_customer_age(18)

    # When
    driver.when_customer_books(5)

    # Then
    assert driver.booking_succeeds()
    assert driver.seats_remaining() == 0


def test_underage_customer():
    # Given
    driver = BookingDriver()
    driver.given_movie_has_seats(20)
    driver.given_customer_age(10)

    # When
    driver.when_customer_books(2)

    # Then
    assert driver.booking_fails()
    assert driver.message() == "Customer does not meet age requirement"


def test_invalid_ticket_quantity():
    # Given
    driver = BookingDriver()
    driver.given_movie_has_seats(20)
    driver.given_customer_age(25)

    # When
    driver.when_customer_books(0)

    # Then
    assert driver.booking_fails()
    assert driver.message() == "Invalid ticket quantity"


def test_insufficient_seats():
    # Given
    driver = BookingDriver()
    driver.given_movie_has_seats(10)
    driver.given_customer_age(25)

    # When
    driver.when_customer_books(20)

    # Then
    assert driver.booking_fails()
    assert driver.message() == "Not enough seats available"


def test_sold_out_movie():
    # Given
    driver = BookingDriver()
    driver.given_movie_has_seats(0)
    driver.given_customer_age(25)

    # When
    driver.when_customer_books(1)

    # Then
    assert driver.booking_fails()
    assert driver.message() == "Movie sold out"