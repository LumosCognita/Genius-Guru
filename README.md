# Genius-Guru

Genius-Guru is a versatile and comprehensive project developed to assist users in navigating their career paths. It harnesses the capabilities of OpenAI and MongoDB to furnish career guidance based on quizzes and courses, create quizzes for assessment, and manage user data efficiently.

## Configuration
### MongoDB Configuration
- Refer to `Genius-Guru/configuration/config.example.ini` to set up your MongoDB connection string.

### OpenAI Configuration
- Provide your OpenAI secret key in the same configuration file.

## Modules

### Database Module
- **File**: `Genius-Guru/database/mongodb.py`
- Connects to MongoDB using the provided configuration and manages user data operations like adding a new user.

### Endpoint Modules
- **generate_career_path.py**: Offers career advice based on quiz summaries and available courses.
- **generate_quiz.py**: Creates quizzes focusing on different majors such as Machine Learning, Software Engineering, and Product Management.

### Schemas
- **File**: `Genius-Guru/schemas/fastapi_schemas.py`
- Defines the data models for the application, including User, Quiz, Question, and Answer.

### Dataset Generation
- **File**: `Genius-Guru/generate_dataset.py`
- Utilizes OpenAI to fabricate multiple-choice questions for assessments based on provided article content.

### Main Application
- **File**: `Genius-Guru/main.py`
- The core FastAPI application that houses the API endpoints for the project.

## .gitignore
The .gitignore file of the project ensures that sensitive and unnecessary files are not tracked by Git. It encompasses patterns for Python byte-compiled files, distribution files, logs, environment files, etc.

## CSS
Genius-Guru incorporates Font Awesome Free 6.1.1 for icons and stylings.

## Getting Started
1. **Clone the Repository**
   ```
   git clone <repository-url>
   ```

2. **Set Up Configurations**
   - Configure your MongoDB and OpenAI as per the instructions in the Configuration section.

3. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```
   uvicorn Genius-Guru.main:app --reload
   ```

## Contribution
Feel free to contribute to Genius-Guru. Create a pull request, and our team will review it promptly.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any queries or further information, please contact: [Contact Information].

Remember to replace the placeholders like `<repository-url>` and `[Contact Information]` with actual values.
