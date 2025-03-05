def send_email():
    import smtplib
    from email.mime.text import MIMEText 
    from datetime import datetime
    from dotenv import load_dotenv
    import os

    load_dotenv()

    now = datetime.now()
    TimeDate = now.strftime("%A %d %B @ %H:%M:%S")

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    
    recipient_name = "Sandra"
    recipient_email = "superben1506@gmail.com"

    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")

    if not EMAIL or not PASSWORD:
        print("Error: Email credentials are missing. Check your .env file.")
        return

    msg = MIMEText(f"Hello {recipient_name},\n\nAs of {TimeDate}, someone has shown interest in joining the scout group. Please check the waiting list to verify if that is the case:\n\nThis means there is a potential new young person who has been added to the waiting list. Please check the OSM for more details.\n\nYours in Scouting,\nBenjamin Parsons\n\nThis is an automated message, please do not reply to this email.")
    msg["Subject"] = f"New Young Person - Waiting List"
    msg["From"] = "Waiting List(Automation)"  
    msg["To"] = "superben1506@gmail.com"

    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, [recipient_email], msg.as_string())
            print(f"Email sent")
    except Exception as e:
        print(f"Failed to send email: {e}")
