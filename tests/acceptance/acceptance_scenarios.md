Feature: Movie Ticket Booking
Scenario: Successful booking
Given a movie has 20 seats
And a customer is 25 years old
When 2 tickets are booked
Then booking succeeds

Scenario: Book Last Tickets
Given a movie has 5 available seats
And customer age is 18
When customer books 5 tickets
Then booking succeeds
And 0 seats remain

Scenario: Underage customer
Given a movie has 20 seats
And customer age is 10
When customer books 2 tickets
Then booking fails

Scenario: Invalid ticket quantity
Given a movie has 20 seats
And customer age is 25
When customer books 0 tickets
Then booking fails

Scenario: Insufficient seats
Given a movie has 10 seats
And customer age is 25
When customer books 20 tickets
Then booking fails

Scenario: Sold out movie
Given a movie has 0 seats
And customer age is 25
When customer books 1 ticket
Then booking fails
