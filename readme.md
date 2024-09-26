# Prime Number Fetcher

CAUTION ---- If you cloned the repo. please follow the readme file to setup this project on your local machine

This project is a simple web application built with Django that allows users to input a number and receive a list of all prime numbers up to that number. The limit of the input number is 100 you can change it by updating the LIMIT in .env file

## Features

- Input a number to find all prime numbers up to that number.
- Responsive design using Bootstrap.
- Asynchronous form submission using AJAX.
- Dynamic response display without reloading the page.

## Technologies Used

- **Backend**: Django
- **Frontend**: HTML, CSS, Bootstrap
- **AJAX**: jQuery

## Installation

### Prerequisites

- Python 3.x

### Steps to Run the Application

1. **Clone the Repository**
   ```bash
   git clone https://github.com/codewithmanuu/prime-number-fetcher.git
   cd prime-number-fetcher

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install Required Packages Install Django if you haven't already**
   ```bash
   pip install -r requirements.txt

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate

5. **Start the Development Server**
   ```bash
   python manage.py runserver

- Access the Application: Open your web browser and go to http://127.0.0.1:8000/ to view the application.

   

### Contact

If you have any questions, suggestions, or feedback, please reach out:

- Name: Manukrishna S
- Email: <mailto:manukrishna.s2001@gmail.com>


