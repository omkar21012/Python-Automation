import smtplib
import os
from email.message import EmailMessage

def send_email_with_report():
    sender_email = "omkardmule@gmail.com"
    receiver_email = "omkardmule@gmail.com"
    subject = "Automation Test Report"
    body = "Hi,\n\nPlease find the attached test report.\n\nRegards,\nAutomation Bot"
    app_password = "your_app_password"  # 16-digit App Password from Gmail

    report_path = os.path.abspath("reports/report.html")

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(body)

    # Attach report.html
    with open(report_path, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(report_path)
        msg.add_attachment(file_data, maintype='text', subtype='html', filename=file_name)

    # Connect to Gmail SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print("✅ Email sent with report attached.")

if __name__ == "__main__":
    send_email_with_report()
