import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))
import app


class AppTest(unittest.TestCase):
    def test_default_student(self):
        student = app.get_student()
        self.assertEqual(student["Surname"], "Ablekimov")
        self.assertEqual(student["Student ID"], "37637")

    def test_message_text(self):
        text = app.build_message(app.get_student())
        self.assertIn("DevOps Student Application", text)
        self.assertIn("Group: IT2-2312", text)
        self.assertTrue(text.endswith("Application is running successfully!"))

    def test_env_variable(self):
        os.environ["STUDENT_GROUP"] = "TEST-GROUP"
        self.assertEqual(app.get_student()["Group"], "TEST-GROUP")
        del os.environ["STUDENT_GROUP"]


if __name__ == "__main__":
    unittest.main()
