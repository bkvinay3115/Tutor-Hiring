# Tutor Hiring System

## Overview
The Tutor Hiring System is a Django-based web application that connects students and tutors through a centralized platform. Students can search for tutors, send hire requests, and make payments, while tutors can manage their profiles, approve requests, and track student interactions.

## Features

### Student Module
- Student Registration & Login
- Search Tutors by Subject
- View Tutor Profiles
- Send Hire Requests
- Make Payments
- Manage Student Profile

### Tutor Module
- Tutor Registration & Login
- Manage Tutor Profile
- View Hire Requests
- Approve Hire Requests
- Track Student Details

### System Features
- Secure Authentication
- Dashboard Management
- Payment Management
- User-Friendly Interface
- Responsive Design

## Technology Stack

### Frontend
- HTML
- CSS
- Bootstrap
- JavaScript

### Backend
- Python
- Django Framework
- SQLite Database

### Tools Used
- VS Code
- Git
- GitHub

## Project Structure

```
tutor_hiring/
│
├── main/
├── tutor_hiring/
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Tutor-Hiring-System.git
cd Tutor-Hiring-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

## Modules

### User Authentication
Handles registration, login, and logout functionality for students and tutors.

### Tutor Management
Allows tutors to create and update profiles, including subjects, fees, and availability.

### Student Management
Allows students to search tutors, hire tutors, and manage profiles.

### Hire Management
Students can send hire requests, and tutors can approve them.

### Payment Management
Handles payment records for approved hire requests.

## Future Enhancements
- Online Payment Gateway Integration (Razorpay/Stripe)
- AI-Based Tutor Recommendation
- Live Chat System
- Video Class Integration
- Tutor Rating & Review System
- Mobile Application Support

## Conclusion
The Tutor Hiring System simplifies the process of connecting students and tutors through a secure and efficient online platform. It reduces manual effort, improves communication, and provides an organized tutor hiring experience.

