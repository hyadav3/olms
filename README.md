Online Library Management System
This project aim is to create a website that will help faculty members at university to manage existing books efficiently. The problem that this project aiming to solve is the difficulty that faculty members face in managing library books. This can be due to various reasons such as having a large number of books to manage, difficulty in keeping track of book availability, and time-consuming processes to add or remove books in their websites. Thus, this website will provide an intuitive platform for faculty members to manage their books. Members can easily add new books to their library, view available books, and update or remove books that are no longer required. 
Here is the web: http://malsaegh.pythonanywhere.com/
Home Page: 
 
Admin Page : 
 
View Book : 
 
Data: The books.csv dataset consists of book’s information like title, isbn, and authors is downloaded from Kaggle. This dataset was created on May 25, 2019, from Goodreads API .  The objective of this dataset was in good faith to help bibliophiles by having a good clean dataset of books.
Tools: 
We have implemented entire application with MVC (Model View Controller) architecture pattern and Python language for server-side programming. 
Model: The model is developed using Django's ORM to define database schema and create model for book management.
 
View: The views are developed using Django as web framework in Python which having inbuilt features for creating web applications including a powerful template engine for generating HTML views for the front end. Django widget tweaks is used to render form fields in templated with HTML, CSS, Chart-JS 
Controller: The controllers are developed using Django which having powerful ORM (Object-Relational Mapping) for interacting with databases, and a robust system for handling URL routing, request handling, and middleware. sqlparse a non-validating SQL parser for Python is used to provide support for parsing, splitting, and formatting SQL statements.
Deployment Platform: Python Anywhere
How to deploy application at local system
•	Install Python (3.7.6)
•	Open Terminal and Execute Following Commands:
python -m pip install -r requirements. txt
Download This Project Zip Folder and Extract it
•	Move to project folder in Terminal. Then run following Commands:
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
•	Now enter following URL in Your Browser Installed On Your Pc

http://127.0.0.1:8000/
Tools Used: 
Front End: Django/HTML/CSS /  
Back End: Python with Django ORM, Views, Sqlparse
Database: Sqlite3 
Tools: Visual Studio Code, Draw.io, Spyder Python, Postman 

User Functionalities: 
Application supports following functionalities to manage the books lifecycle for IU faculty. 
•	Onboarding new user
•	Login
•	Create new book record. 
             To create a record, we follow the data integrity rules. 
•	View, Update and Delete existing record.
            Can view all the available books in a click.
            Can delete any book record in a click. 
            Can inline update of individual book record. 
•	About Us 
•	Logout
