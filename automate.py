import requests
from pymongo import MongoClient
import schedule
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["store_db"]
collection = db["products"]

# Email setup (configure your sender & receiver details)
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'mhdnihal4343@gmail.com'
SENDER_PASSWORD = 'aqmt iffd gwiy xgee'  # Use app password, NOT your Gmail password
RECEIVER_EMAIL = 'mhdnihal4343@gmail.com'

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("✅ Email sent successfully")
    except Exception as e:
        print("❌ Failed to send email:", e)

def fetch_and_save_data():
    try:
        print("Starting data fetch...")
        api_url = "https://fakestoreapi.com/products"
        response = requests.get(api_url)
        product_data = response.json()

        # Clear old data (optional)
        collection.delete_many({})

        # Insert new data
        collection.insert_many(product_data)
        print("✅ Product data saved to MongoDB")

        # Send success email
        send_email(
            subject="ETL Job Success",
            body="Product data was successfully fetched and saved to MongoDB."
        )
    except Exception as e:
        print("❌ Error during ETL job:", e)
        send_email(
            subject="ETL Job Failed",
            body=f"ETL job failed with error:\n{e}"
        )

# Schedule the job (every 60 seconds)
schedule.every(60).seconds.do(fetch_and_save_data)

print("Scheduler started. Waiting for next run...")

while True:
    schedule.run_pending()
    time.sleep(1)  # check every second
