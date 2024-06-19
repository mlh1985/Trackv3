# Architecture Documentation

## Overview

The Racetrack System is a web application designed to manage and track races for a troop. It uses a Raspberry Pi as the core system, with Flask as the web framework, SQLite for the database, and various sensors and actuators to manage race events.

## Components

### 1. Flask Web Framework
- **Purpose**: Handles the web server functionality and routes.
- **Key Files**:
  - `app/__init__.py`: Initializes the Flask application and database.
  - `app/routes.py`: Contains the route definitions.
  - `app/models.py`: Defines the database models.

### 2. Database (SQLite)
- **Purpose**: Stores user information, car details, race parameters, and results.
- **Key Tables**:
  - `User`: Stores user details and roles.
  - `Car`: Stores car details.
  - `Patrol`: Stores patrol details.

### 3. Sensors and Actuators
- **Purpose**: Manages physical race events (starting races, reading finish line sensors).
- **Key Components**:
  - **Finish Line Sensors**: Detects when a car crosses the finish line.
  - **Race Starter Actuator**: Initiates the start of the race.

### 4. Frontend
- **Purpose**: Provides the user interface for interacting with the system.
- **Key Technologies**: HTML, CSS, JavaScript
- **Key Files**:
  - `app/templates/`: Contains HTML templates.
  - `app/static/css/`: Contains CSS files.
  - `app/static/js/`: Contains JavaScript files.

## Application Flow

1. **User Authentication**: Users log in through the `/login` route.
2. **Dashboard Access**: Depending on the user role, they access different dashboards.
3. **Car Submission**: Trailmen submit their cars through the `/submit_car` route.
4. **Race Management**: Race officials set race parameters, approve car submissions, and start/track races.
5. **Race Execution**: The system interacts with sensors and actuators to manage race events.
6. **Data Display**: Results are displayed on various dashboards and the leaderboard.

## Key Features

- **Role-Based Access Control**: Different functionalities are accessible based on user roles (Admin, Troopmaster, Race Official, Trailman, Guest).
- **File Uploads**: Users can upload pictures of cars and boys.
- **Real-Time Race Tracking**: The system tracks races in real-time using sensors and actuators.
- **Responsive Design**: The application is designed to be accessible on tablets and mobile devices.

## Deployment

- **Development**: The system is run using Flask's development server.
- **Production**: For production, consider using a WSGI server like Gunicorn and a reverse proxy like Nginx.
- **Environment Configuration**: Store configuration settings in environment variables for security and flexibility.
