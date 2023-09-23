Genius-Guru
Genius-Guru is a comprehensive project designed to assist users in their career paths. It leverages the power of OpenAI and MongoDB to provide career advice based on quizzes and courses, generate quizzes for assessment, and manage user data.

Configuration
MongoDB Configuration: Set up your MongoDB connection string in Genius-Guru/configuration/config.example.ini.
OpenAI Configuration: Provide your OpenAI secret key in the same configuration file.
Modules
Database Module (Genius-Guru/database/mongodb.py):

Connects to MongoDB using the provided configuration.
Handles user data operations like adding a new user.
Endpoint Modules:

generate_career_path.py: Generates career advice based on quiz summaries and available courses.
generate_quiz.py: Generates quizzes for different majors like Machine Learning, Software Engineering, and Product Management.
Schemas (Genius-Guru/schemas/fastapi_schemas.py):

Defines the data models for the application, such as User, Quiz, Question, and Answer.
Dataset Generation (Genius-Guru/generate_dataset.py):

Uses OpenAI to generate multiple-choice questions for assessment based on given article content.
Main Application (Genius-Guru/main.py):

The core FastAPI application defines the API endpoints for the project.
.gitignore
The project's .gitignore file ensures that sensitive and unnecessary files are not tracked by Git. It includes patterns for Python byte-compiled files, distribution files, logs, environment files, and more.

CSS
The project uses Font Awesome Free 6.1.1 for icons and styling.

Getting Started.
Clone the repository.
Set up your MongoDB and OpenAI configurations.
Install the required dependencies.
Run the FastAPI application using Uvicorn.
