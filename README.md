# Delayed Queue Application

## Description

This application allows users to add tasks to a queue with a specified delay. The tasks will only become available after the specified delay has passed. The application consists of a Flask backend and an HTML/CSS/JavaScript frontend served by Nginx.

## Folder Structure

Assignment_Response_Premagic/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── index.html
│ ├── styles.css
│ └── Dockerfile
├── docker-compose.yml
└── README.md


## Project Components
# Backend
Language: Python 3.8
Framework: Flask
Dependencies: Listed in backend/requirements.txt
Dockerfile: Located in backend/Dockerfile
# Frontend
Languages: HTML, CSS, JavaScript
Dockerfile: Located in frontend/Dockerfile

## Prerequisites

- Python
- Flask
- Nginx
- Docker
- Docker Compose

## Setup

1. **Clone the Repository**

   ```bash
   git clone <your-repository-url>
   cd Assignment_Response_Premagic


docker-compose up --build


Access the Application

Frontend: Open your web browser and go to http://localhost
Backend: The backend is accessible at http://localhost:5000


## Usage
# Add Tasks
Enter the task name and delay time in seconds in the frontend form.
Click "Submit" to add the task to the queue.

# Run Tasks
Click "Run" to start processing tasks.
The tasks will be displayed in the order they are processed based on their delay times.