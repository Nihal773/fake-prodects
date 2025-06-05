import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'mhdnihal4343@gmail.com'
receiver_email = 'mhdnihal4343@gmail.com'
password = 'aqmt iffd gwiy xgee'

msg = MIMEText('This is a test email from Python script.')
msg['Subject'] = 'Test Email'
msg['From'] = sender_email
msg['To'] = receiver_email

try:
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        print("✅ Test email sent!")
except Exception as e:
    print("❌ Test failed:", e)
