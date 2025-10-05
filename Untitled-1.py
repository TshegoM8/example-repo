
class Course:
    def __init__(self, name, contact_email):
        self.name = name
        self.contact_email = contact_email

    def contact_details(self):
        print(f"Course Name: {self.name}")
        print(f"Contact Email: {self.contact_email}")

    def head_office(self):
        print("Head Office Location: Cape Town")



class OOPCourse(Course):
    def __init__(self, name="OOP", contact_email="oop@example.com"):
        super().__init__(name, contact_email)
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print(f"Course Description: {self.description}")
        print(f"Trainer: {self.trainer}")

    def show_course_id(self):
        print("Course ID: #12345")


# --- Create Object and Call Methods --- #
course_1 = OOPCourse()

course_1.contact_details()   # From base class
course_1.trainer_details()   # From subclass
course_1.show_course_id()    # From subclass
course_1.head_office()       # From base class
