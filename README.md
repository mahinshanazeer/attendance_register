# Simple Attendance Logger

This is a basic command-line application for logging and viewing attendance for students and teachers. It uses in-memory storage, meaning data persists only while the application is running.

## Usage

To run the application, navigate to the project's root directory in your terminal and execute:

```bash
python main.py
```

This will start the command-line interface (CLI) where you can interact with the system.

### CLI Menu Options

The application presents the following menu:

1.  **Add Student**: Prompts for a student ID and name, then adds the student to the system.
2.  **Add Teacher**: Prompts for a teacher ID and name, then adds the teacher to the system.
3.  **Mark Attendance**: Prompts for a person ID (student or teacher), date (YYYY-MM-DD), and status (present/absent), then records the attendance.
4.  **View Attendance by Person**: Prompts for a person ID and displays all attendance records for that individual.
5.  **View Attendance by Date**: Prompts for a date (YYYY-MM-DD) and displays all attendance records for that date, showing the person's ID, name (if available), and status.
6.  **Exit**: Terminates the application.

## Running Tests

Unit tests are provided to verify the functionality of the data models and the attendance manager logic. To run the tests, execute the following command from the project's root directory:

```bash
python -m unittest discover tests
```

This command will automatically discover and run all tests within the `tests` directory.


## Running with Docker

You can also build and run this application using Docker.

1.  **Build the Docker image:**
    ```bash
    docker build -t attendance-app .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -it --rm attendance-app
    ```
    This will start the application in interactive mode.
