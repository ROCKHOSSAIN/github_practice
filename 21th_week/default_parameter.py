def send_email(recipient, subject, cc=None, priority="normal"):
    """Send an email - cc and priority have sensible defaults"""

    print(f"To: {recipient} | Subject: {subject}")
    print(f"CC: {cc} | Priority: {priority}")


send_email("bob@example.com", "Meeting Notes")

send_email(
    "alice@example.com",
    "Urgent",
    priority="medium"
)