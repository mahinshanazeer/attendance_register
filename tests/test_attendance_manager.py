import unittest
import sys
import os

# Add project root to the Python path to allow importing modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Student, Teacher
from attendance_manager import AttendanceManager

class TestAttendanceManager(unittest.TestCase):

    def setUp(self):
        """Create a fresh AttendanceManager instance for each test."""
        self.manager = AttendanceManager()
        self.student1 = Student(student_id="S101", name="Alice")
        self.student2 = Student(student_id="S102", name="Charlie")
        self.teacher1 = Teacher(teacher_id="T201", name="Bob")

    def test_add_student(self):
        """Test adding a student."""
        self.manager.add_student(self.student1)
        retrieved_student = self.manager.get_student("S101")
        self.assertEqual(retrieved_student, self.student1)
        self.assertEqual(retrieved_student.name, "Alice")

    def test_add_student_duplicate(self):
        """Test adding a student with an existing ID."""
        self.manager.add_student(self.student1)
        with self.assertRaisesRegex(ValueError, "Student with ID S101 already exists."):
            self.manager.add_student(Student(student_id="S101", name="Alicia")) # Same ID, different name

    def test_add_teacher(self):
        """Test adding a teacher."""
        self.manager.add_teacher(self.teacher1)
        retrieved_teacher = self.manager.get_teacher("T201")
        self.assertEqual(retrieved_teacher, self.teacher1)
        self.assertEqual(retrieved_teacher.name, "Bob")

    def test_add_teacher_duplicate(self):
        """Test adding a teacher with an existing ID."""
        self.manager.add_teacher(self.teacher1)
        with self.assertRaisesRegex(ValueError, "Teacher with ID T201 already exists."):
            self.manager.add_teacher(Teacher(teacher_id="T201", name="Bobby")) # Same ID, different name

    def test_get_student_exists(self):
        """Test getting an existing student."""
        self.manager.add_student(self.student1)
        student = self.manager.get_student("S101")
        self.assertIsNotNone(student)
        self.assertEqual(student.student_id, "S101")

    def test_get_student_not_exists(self):
        """Test getting a non-existent student."""
        student = self.manager.get_student("S999")
        self.assertIsNone(student)

    def test_get_teacher_exists(self):
        """Test getting an existing teacher."""
        self.manager.add_teacher(self.teacher1)
        teacher = self.manager.get_teacher("T201")
        self.assertIsNotNone(teacher)
        self.assertEqual(teacher.teacher_id, "T201")

    def test_get_teacher_not_exists(self):
        """Test getting a non-existent teacher."""
        teacher = self.manager.get_teacher("T999")
        self.assertIsNone(teacher)

    def test_mark_attendance_student_valid(self):
        """Test marking valid attendance for a student."""
        self.manager.add_student(self.student1)
        self.manager.mark_attendance("S101", "2023-10-26", "present")
        records = self.manager.get_attendance_by_person("S101")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].date, "2023-10-26")
        self.assertEqual(records[0].status, "present")

    def test_mark_attendance_teacher_valid(self):
        """Test marking valid attendance for a teacher."""
        self.manager.add_teacher(self.teacher1)
        self.manager.mark_attendance("T201", "2023-10-27", "absent")
        records = self.manager.get_attendance_by_person("T201")
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].date, "2023-10-27")
        self.assertEqual(records[0].status, "absent")

    def test_mark_attendance_person_not_found(self):
        """Test marking attendance for a non-existent person ID."""
        with self.assertRaisesRegex(ValueError, "Person with ID S999 not found."):
            self.manager.mark_attendance("S999", "2023-10-26", "present")

    def test_mark_attendance_invalid_date(self):
        """Test marking attendance with an invalid date format."""
        self.manager.add_student(self.student1)
        with self.assertRaisesRegex(ValueError, "Incorrect date format, should be YYYY-MM-DD"):
            self.manager.mark_attendance("S101", "26-10-2023", "present")

    def test_mark_attendance_invalid_status(self):
        """Test marking attendance with an invalid status."""
        self.manager.add_student(self.student1)
        with self.assertRaisesRegex(ValueError, "Status must be 'present' or 'absent'"):
            self.manager.mark_attendance("S101", "2023-10-26", "late")

    def test_get_attendance_by_person_found(self):
        """Test getting attendance for a person with records."""
        self.manager.add_student(self.student1)
        self.manager.mark_attendance("S101", "2023-10-26", "present")
        self.manager.mark_attendance("S101", "2023-10-27", "absent")
        records = self.manager.get_attendance_by_person("S101")
        self.assertEqual(len(records), 2)

    def test_get_attendance_by_person_not_found(self):
        """Test getting attendance for a person with no records."""
        self.manager.add_student(self.student1) # Student exists, but no records
        records = self.manager.get_attendance_by_person("S101")
        self.assertEqual(len(records), 0)

    def test_get_attendance_by_person_id_not_exist(self):
        """Test getting attendance for a non-existent person ID."""
        records = self.manager.get_attendance_by_person("S999")
        self.assertEqual(len(records), 0) # Should return empty list

    def test_get_attendance_by_date_found(self):
        """Test getting attendance for a date with records."""
        self.manager.add_student(self.student1)
        self.manager.add_teacher(self.teacher1)
        self.manager.mark_attendance("S101", "2023-10-26", "present")
        self.manager.mark_attendance("T201", "2023-10-26", "absent")
        self.manager.mark_attendance("S101", "2023-10-27", "present") # Different date

        records = self.manager.get_attendance_by_date("2023-10-26")
        self.assertEqual(len(records), 2)
        person_ids = {record.person_id for record in records}
        self.assertEqual(person_ids, {"S101", "T201"})

    def test_get_attendance_by_date_not_found(self):
        """Test getting attendance for a date with no records."""
        self.manager.add_student(self.student1)
        self.manager.mark_attendance("S101", "2023-10-26", "present")
        records = self.manager.get_attendance_by_date("2023-10-27")
        self.assertEqual(len(records), 0)

    def test_get_attendance_by_date_invalid_format(self):
        """Test getting attendance with an invalid date format."""
        with self.assertRaisesRegex(ValueError, "Incorrect date format, should be YYYY-MM-DD"):
            self.manager.get_attendance_by_date("26-10-2023")

if __name__ == '__main__':
    unittest.main()
