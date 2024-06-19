# Developer Guide

## Prerequisites

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login
- SQLite
- Raspberry Pi with required sensors and actuators

## Setup Instructions

1. **Clone the Repository**:
    ```sh
    git clone <repository_url>
    cd <repository_name>
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add the following:
    ```env
    FLASK_APP=app
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    ```

5. **Initialize the Database**:
    ```sh
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the Development Server**:
    ```sh
    flask run
    ```

## Project Structure

project_root/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ ├── forms.py
│ ├── templates/
│ ├── static/
│ │ ├── css/
│ │ ├── js/
│ │ └── images/
│ └── hardware.py
├── migrations/
├── venv/
├── generate_data.py
├── config.py
├── requirements.txt
└── run.py


## Key Files

- `app/__init__.py`: Initializes the Flask application and database.
- `app/routes.py`: Contains route definitions and view functions.
- `app/models.py`: Defines the database models.
- `app/forms.py`: Contains form definitions using Flask-WTF.
- `app/hardware.py`: Interacts with the Raspberry Pi hardware.
- `generate_data.py`: Script to populate the database with sample data.

## Adding a New Feature

1. **Define Models**: Update `models.py` to include any new database tables or columns.
2. **Create Forms**: Update `forms.py` to include new forms if needed.
3. **Update Routes**: Add new route definitions and view functions in `routes.py`.
4. **Create Templates**: Add new HTML templates in the `templates` directory.
5. **Add Static Files**: Include new CSS or JavaScript files in the `static` directory.
6. **Database Migrations**:
    ```sh
    flask db migrate -m "Add description of changes"
    flask db upgrade
    ```

## Testing

1. **Run Tests**:
    - Create tests in the `tests` directory.
    - Use a testing framework like `pytest`.
    - Run tests using:
    ```sh
    pytest
    ```

## Deployment

1. **Install Production Dependencies**:
    ```sh
    pip install gunicorn
    ```

2. **Run the Application with Gunicorn**:
    ```sh
    gunicorn -w 4 run:app
    ```

3. **Set Up Reverse Proxy**: Use Nginx or Apache as a reverse proxy to forward requests to Gunicorn.

4. **Configure Environment Variables**: Set environment variables for production settings.

## Troubleshooting

- **Database Issues**: Ensure migrations are applied correctly.
- **File Uploads**: Check the permissions of the `uploads` directory.
- **Hardware Interaction**: Ensure the Raspberry Pi is properly configured and connected to the sensors and actuators.

