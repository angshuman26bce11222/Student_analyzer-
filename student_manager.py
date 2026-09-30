class StudentManager:
    def __init__(self):
        self.students = []  # List of student records
        self.registered_ids = set()  # Set to track and prevent duplicate IDs

    def add_student(self, student_record: dict) -> bool:
        """Adds a student record if the ID is not duplicate."""
        sid = student_record["id"]
        if sid in self.registered_ids:
            print(f"Error: Duplicate Student ID {sid} detected.")
            return False
        
        self.registered_ids.add(sid)
        self.students.append(student_record)
        return True

    def remove_duplicates(self):
        """Demonstrates explicit duplicate removal from an ordered array (List)."""
        seen = set()
        unique_list = []
        for student in self.students:
            if student["id"] not in seen:
                seen.add(student["id"])
                unique_list.append(student)
        self.students = unique_list