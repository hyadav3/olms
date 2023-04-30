
# Online Library Management System

This project aim is to create a website that will help faculty members at university to manage existing books efficiently. The problem that this project aiming to solve is the difficulty that faculty members face in managing library books. This can be due to various reasons such as having a large number of books to manage, difficulty in keeping track of book availability, and time-consuming processes to add or remove books in their websites. Thus, this website will provide an intuitive platform for faculty members to manage their books. Members can easily add new books to their library, view available books, and update or remove books that are no longer required. 


## Website: 
http://malsaegh.pythonanywhere.com/
## Home Page: 

![Home Pagel](https://github.com/hyadav3/olms/blob/main/librarymanagement/static/homepage.png)

## View Book

![View Book](https://github.com/hyadav3/olms/blob/main/librarymanagement/static/view%20book.png)

## View: 
The views are developed using Django as web framework in Python which having inbuilt features for creating web applications including a powerful template engine for generating HTML views for the front end. Django widget tweaks is used to render form fields in templated with HTML, CSS, Chart-JS 
## Model

![App Model](https://github.com/hyadav3/olms/blob/main/librarymanagement/static/model.png)


## Controller
The controllers are developed using Django which having powerful ORM (Object-Relational Mapping) for interacting with databases, and a robust system for handling URL routing, request handling, and middleware. sqlparse a non-validating SQL parser for Python is used to provide support for parsing, splitting, and formatting SQL statements.
## Deployment Platform
Python Anywhere
## Deployment

Install Python (3.7.6)

Open Terminal and Run below Command:

```bash
  python -m pip install -r requirements. txt
```

Download and unzip the project

Move to project folder in Terminal. Then run following Commands:

```bash
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
Access the local deployment in your browser

http://127.0.0.1:8000/
## Tools Used

Front End: Django/HTML/CSS

Back End: Python with Django ORM, Views, Sqlparse

Database: Sqlite3 

Tools: Visual Studio Code, Draw.io, Spyder Python, Postman 


## User Functionalities
Application supports following functionalities to manage the books lifecycle for IU faculty. 

•	Onboarding new user 

•	Login  

•	Create new book record.       
            
•	View, Update and Delete existing record.  
                
•	About Us  

•	Logout 

## Technical Writing - Summary

Our website is an excellent platform for efficient book management. We have divided the project into 2 main parts: designing a user-friendly website for IU faculty to manage books and robust database to store the book data.  

The website design process started with define the project goal and requirements like ability to add, delete and modify the books. Based on these requirements, a website design was created that is easy to navigate and understand, with a clean and modern interface.    

A web designing and database project for library management using a book dataset from Kaggle can be an excellent tool for efficient book management. The project can be divided into two main parts: designing a user-friendly website that will allow librarians to manage books efficiently and developing a robust database to store book data.  

After that, we focused to develop a robust database to store book data which is lightweight and easy to integrate with our application. We decided to use the out of the box Python Django with SQLite database and created model for different tables and relationship.   

In addition to the basic functionalities of adding, removing, and modifying books, our website can be enhanced with additional features, such as the ability to generate reports on the library's book collection, or to recommend books to users based on their reading history. Integration with external APIs can also be explored to provide additional information about books or authors.  

In summary, our web designing and database project for library management using a book dataset from Kaggle has the potential to be a highly effective tool for IU faculty to manage their collections efficiently. 

## Demo

https://youtu.be/QhVvMky-Ad8

