"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

# Initialise the instance variables for each email.

# Create the 'mark_as_read()' method to change the 'has_been_read'
# instance variable for a specific object from False to True.


# --- Functions --- #
# Build out the required functions for your program.


class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True
inbox = []

def populate_inbox():
    email = Email("tshego@gmail.com", "Meeting schedule", "Our meeting is at 5 PM SAT.")
    email1 = Email("Ole@gmail.com", "Training day", "Training is every Tuesday 10 AM")
    email2 = Email("melato@gmail.com", "Assignment due", "Here is a reminder that your assignment is due tomorrow")
    inbox.extend([email, email1, email2])
 # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
def list_emails():
    if not inbox:
        print("Inbox is empty.")
    else:
        print("\nAll Emails:")
        for e, email in enumerate(inbox):
            print(f"{e}: {email.subject_line} (Read: {'Yes' if email.has_been_read else 'No'})")

   
    pass


def read_email(index):
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()
    else:
        print("Invalid email index.")
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    pass


def view_unread_emails():
    unread_found = False
    print("\nUnread Emails:")
    for i, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{i}: {email.subject_line}")
            unread_found = True
    if not unread_found:
        print("No unread emails.")

    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
populate_inbox()


# --- Lists --- #
# Initialise an empty list outside the class to store the email objects.

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    try:
        user_choice = int(input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

Enter selection: """
        ))

        if user_choice == 1:
            list_emails()
            try:
                selected_index = int(input("Enter the index of the email you want to read: "))
                read_email(selected_index)
            except ValueError:
                print("Please enter a valid number.")
        elif user_choice == 2:
            view_unread_emails()
        elif user_choice == 3:
            print("bye!")
            break
        else:
            print("Oops - incorrect input.")
    except ValueError:
        print("Please enter a number (1-3).")
