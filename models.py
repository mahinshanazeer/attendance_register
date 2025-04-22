import datetime

class Student:
    """Represents a student with an ID and name."""
    def __init__(self, student_id: str, name: str):
        self.student_id = student_id
        self.name = name

class Teacher:
    """Represents a teacher with an ID and name."""
    def __init__(self, teacher_id: str, name: str):
        self.teacher_id = teacher_id
        self.name = name

class AttendanceRecord:
    """Represents an attendance record for a person on a specific date."""
    def __init__(self, person_id: str, date: str, status: str):
        self.person_id = person_id
        # Validate date format
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")
        self.date = date
        # Validate status
        if status not in ['present', 'absent']:
            raise ValueError("Status must be 'present' or 'absent'")
        self.status = status
