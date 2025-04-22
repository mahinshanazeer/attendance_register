import unittest
import sys
import os

# Add project root to the Python path to allow importing modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Student, Teacher, AttendanceRecord

class TestModels(unittest.TestCase):

    def test_student_creation(self):
        """Test creating a Student instance."""
        student = Student(student_id="S123", name="Alice")
        self.assertEqual(student.student_id, "S123")
        self.assertEqual(student.name, "Alice")

    def test_teacher_creation(self):
        """Test creating a Teacher instance."""
        teacher = Teacher(teacher_id="T456", name="Bob")
        self.assertEqual(teacher.teacher_id, "T456")
        self.assertEqual(teacher.name, "Bob")

    def test_attendance_record_creation_valid(self):
        """Test creating an AttendanceRecord with valid data."""
        record = AttendanceRecord(person_id="S123", date="2023-10-26", status="present")
        self.assertEqual(record.person_id, "S123")
        self.assertEqual(record.date, "2023-10-26")
        self.assertEqual(record.status, "present")

        record_absent = AttendanceRecord(person_id="T456", date="2024-01-01", status="absent")
        self.assertEqual(record_absent.person_id, "T456")
        self.assertEqual(record_absent.date, "2024-01-01")
        self.assertEqual(record_absent.status, "absent")

    def test_attendance_record_invalid_date_format(self):
        """Test creating AttendanceRecord with invalid date formats."""
        with self.assertRaisesRegex(ValueError, "Incorrect date format, should be YYYY-MM-DD"):
            AttendanceRecord(person_id="S123", date="26-10-2023", status="present")
        with self.assertRaisesRegex(ValueError, "Incorrect date format, should be YYYY-MM-DD"):
            AttendanceRecord(person_id="S123", date="2023/10/26", status="present")
        with self.assertRaisesRegex(ValueError, "Incorrect date format, should be YYYY-MM-DD"):
            AttendanceRecord(person_id="S123", date="October 26, 2023", status="present")
        with self.assertRaisesRegex(ValueError, "Incorrect date format, should be YYYY-MM-DD"):
            AttendanceRecord(person_id="S123", date="20231026", status="present")

    def test_attendance_record_invalid_status(self):
        """Test creating AttendanceRecord with invalid status."""
        with self.assertRaisesRegex(ValueError, "Status must be 'present' or 'absent'"):
            AttendanceRecord(person_id="S123", date="2023-10-26", status="late")
        with self.assertRaisesRegex(ValueError, "Status must be 'present' or 'absent'"):
            AttendanceRecord(person_id="T456", date="2023-10-27", status="Present") # Case-sensitive
        with self.assertRaisesRegex(ValueError, "Status must be 'present' or 'absent'"):
            AttendanceRecord(person_id="T456", date="2023-10-27", status="")

if __name__ == '__main__':
    unittest.main()
