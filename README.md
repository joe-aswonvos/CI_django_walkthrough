# CI_django_walkthrough

## Summary

This project was developed as part of a codealong exercise during the Full-Stack Web Development Bootcamp with Code Institute and Headforwards. The primary focus of this project is to demonstrate the integration of various technologies to build and deploy a Django web application.

## Table of Contents

1. [Technologies Involved](#technologies-involved)
2. [Project Overview](#project-overview)
3. [Setup Instructions](#setup-instructions)
4. [Usage](#usage)
5. [Deployment](#deployment)
6. [Contributing](#contributing)
7. [License](#license)

## Technologies Involved

- Django
- Python
- HTML
- CSS
- JavaScript
- Bootstrap
- Heroku
- Git
- GitHub

## Project Overview

This project is a simple Django web application that includes basic views and URL routing. It serves as a foundational exercise to understand the core concepts of Django and web development.

## Setup Instructions

1. Clone the repository:
   ```sh
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```sh
   cd django_project
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Usage

- Access the home page at [http://127.0.0.1:8000/](http://_vscodecontentref_/1)
- Access the about page at [http://127.0.0.1:8000/about/](http://_vscodecontentref_/2)

## Deployment

This project is configured for deployment on Heroku. Follow these steps to deploy:

1. Create a Heroku app:
   ```sh
   heroku create
   ```
2. Push the code to Heroku:
   ```sh
   git push heroku main
   ```
3. Open the deployed app:
   ```sh
   heroku open
   ```
