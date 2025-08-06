import smtplib
import os
from email.message import EmailMessage

def send_email_with_report():
    # Sender and receiver details
    sender_email = "omkardmule@gmail.com"
    receiver_email = "omkardmule@gmail.com"  # You can also use a list here
    app_password = "yydw wasv kmsz ttoi"  # Your 16-digit App Password (Gmail)

    # Email content
    subject = "Automation Test Report"
    body = """\
Hi,

Please find the attached test execution report.

Regards,  
Automation Bot
"""

    # Path to the HTML report
    report_path = os.path.abspath("reports/report.html")

    if not os.path.exists(report_path):
        print(f"❌ Report file not found: {report_path}")
        return

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

    # Attach the report file
    with open(report_path, 'rb') as file:
        report_data = file.read()
        msg.add_attachment(report_data, maintype='text', subtype='html', filename="TestReport.html")

    try:
        # Send the email using Gmail SMTP server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, app_password)
            smtp.send_message(msg)

        print("✅ Email sent successfully with report attached.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    send_email_with_report()
