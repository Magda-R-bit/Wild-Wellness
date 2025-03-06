## Manual Testing


| #  | Test Area      | Test Description                                                  | Expected Result                             |
|----|----------------|-------------------------------------------------------------------|---------------------------------------------|
| 1  | Authentication | User can register, log in, and log out                            | Success messages and proper redirects       |
| 2  | Authentication | Invalid login shows an error message                              | Error message displayed, no login success   |
| 3  | Calendar View  | Calendar loads and displays events                                | Events visible on the correct dates         |
| 4  | Calendar View  | Navigate between months                                           | Previous and next months load correctly     |
| 5  | Booking        | User can book an available cabin                                  | Booking confirmation displayed and saved    |
| 6  | Booking        | User cannot book a fully booked cabin                             | Error message shown, no booking created     |
| 7  | Booking List   | User can check all bookings in the calendar                       | All Bookings and availability displayed in the calendar |
| 8  | Booking List   | Displays cabin image, dates, total price                          | Correct details displayed in Booking List   |
| 9  | Booking List   | User can update booking                                           | Booking is updated and success message displayed |
| 10 | Booking List   | User can delete booking                                           | Bookings is canceled and removed from the list              |
| 11 | Review         | Logged in User can leave a review under each cabin                | Review is displayed for a user and pending admin approval   |
| 12 | Admin          | Admin can create, edit, and delete booking                        | Changes are saved and reflected on site     |
| 13 | Admin          | Admin approve review, review displays for public view             | Review displayed under cabin for all users  |
| 14 | Responsive     | Mobile view displays calendar, cabins and bookings correctly      | Layout adapts and remains usable            |
| 15 | Error Handling | 404 page shows for invalid URLs                                   | Custom 404 error page displays              |
| 16 | Error Handling | Invalid form submissions show errors                              | Helpful error messages are shown            |



### Forms Testing



| #  | Test Area               | Test Case Description                                           | Expected Result                                      |
|-----|-------------------------|-----------------------------------------------------------------|------------------------------------------------------|
| 17  | Check Availability Form | Form displays date selection options                           | Form loads with all fields visible                  |
| 18  | Check Availability Form | Submit valid date and cabin name to check availability         | Shows available spots or "Full" message             |
| 19  | Check Availability Form | Submit form with missing fields                                | Error messages shown for required fields            |
| 20  | Check Availability Form | Prevent checking availability for past dates                   | Validation error; form not submitted                |
| 21  | Create Booking Form     | Form loads with correct fields (cabin name and dates)          | Fields are displayed correctly                       |
| 22  | Create Booking Form     | Submit valid data to create a booking                          | Success message and booking confirmation            |
| 23  | Create Booking Form     | Submit invalid or incomplete data (missing required fields)    | Error messages appear under invalid fields          |
| 24 | Create Booking Form      | Prevent double booking                                         | Block submission and display an error               |
| 25  | Create Booking Form     | Attempt to submit the form without being logged in             | Redirect to login or show permission error          |
| 26  | Edit/Cancel Booking     | Edit or cancel an existing booking via form                    | Success message and changes applied                 |

