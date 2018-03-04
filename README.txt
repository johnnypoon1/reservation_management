Django version: 1.10
Superuser = admin/ABC123456

Requirement: Django 1.10
Startup instruction
No additional or non-built-in library used. Install Django 1.10 and "perform a python manage.py runserver" to start.
front page URL is <localhost>:<port>/reservation
admin page URL is <localhost>:<port>/admin

Note/enhancement:
This program has been designed and written for easy and quick review.
Below are what I think are good to include in the program but have not implemented.

1. Check in and check out attribute best to be have date time.
2. Ideally users shall be able to login to make reservation. This is skipped to keep it short.
3. Class based view will be a much better fit for this project.
4. As number of templates grows, we shall separate out templates into different folders and organize common use template.
5. Price of room shall be able to change depending on date, this is not included in this program.
6. Action taken to the reservation shall have history tracking
7. An available room shall be reserved once the form loads up and released if timeout from the form
8. avoid hidden field as much as possible
9. Use a base html for common area of web page if contains menu
10. include css and js files instead of inline css and js
11. option to book more than one room at the same time, this program is designed to book one at a time to keep it simple.
12. Create a log file to record all the errors and activity.
13. Traffic control function in view should be a decorator instead.
14. Traffic control should take last action taken time as reference instead of room modification time.
15. User shall not be able to check in until the date of arrival, but since check in supposed to be a staff control, I will leave this alone.