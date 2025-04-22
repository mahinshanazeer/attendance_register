from models import Student, Teacher, AttendanceRecord
import datetime

class AttendanceManager:
    """Manages students, teachers, and attendance records."""

    def __init__(self):
        """Initializes the AttendanceManager with empty storage."""
        self._students = {}  # {student_id: Student object}
        self._teachers = {}  # {teacher_id: Teacher object}
        self._attendance_records = []  # List of AttendanceRecord objects

    def add_student(self, student: Student):
        """Adds a student to storage. Raises ValueError if student ID already exists."""
        if student.student_id in self._students:
            raise ValueError(f"Student with ID {student.student_id} already exists.")
        self._students[student.student_id] = student

    def add_teacher(self, teacher: Teacher):
        """Adds a teacher to storage. Raises ValueError if teacher ID already exists."""
        if teacher.teacher_id in self._teachers:
            raise ValueError(f"Teacher with ID {teacher.teacher_id} already exists.")
        self._teachers[teacher.teacher_id] = teacher

    def mark_attendance(self, person_id: str, date: str, status: str):
        """Marks attendance for a student or teacher.

        Args:
            person_id: The ID of the student or teacher.
            date: The date of attendance in 'YYYY-MM-DD' format.
            status: The attendance status ('present' or 'absent').

        Raises:
            ValueError: If the person ID does not exist, or if the date or status is invalid.
        """
        if person_id not in self._students and person_id not in self._teachers:
            raise ValueError(f"Person with ID {person_id} not found.")

        # Validation for date and status is handled by AttendanceRecord constructor
        try:
            record = AttendanceRecord(person_id=person_id, date=date, status=status)
            self._attendance_records.append(record)
        except ValueError as e:
            # Re-raise the validation error from AttendanceRecord
            raise e

    def get_student(self, student_id: str) -> Student | None:
        """Retrieves a student by ID. Returns None if not found."""
        return self._students.get(student_id)

    def get_teacher(self, teacher_id: str) -> Teacher | None:
        """Retrieves a teacher by ID. Returns None if not found."""
        return self._teachers.get(teacher_id)

    def get_attendance_by_person(self, person_id: str) -> list[AttendanceRecord]:
        """Returns a list of attendance records for a specific person."""
        return [record for record in self._attendance_records if record.person_id == person_id]

    def get_attendance_by_date(self, date: str) -> list[AttendanceRecord]:
        """Returns a list of attendance records for a specific date.

        Args:
            date: The date in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the date format is incorrect.
        """
        # Validate date format before filtering
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYY-MM-DD")
        return [record for record in self._attendance_records if record.date == date]
