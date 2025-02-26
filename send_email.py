def send_email():
    import smtplib
    from email.mime.text import MIMEText 
    from datetime import datetime


    now = datetime.now()
    TimeDate = now.strftime("%A %d %B @ %H:%M:%S")

    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    EMAIL = "parsonsjohnbenjamin@gmail.com"
    PASSWORD = "afhb iwlr fwip bmnw" 
    recipent = "Sandra"

    msg = MIMEText(f"Hello {recipent},\n\nAs of {TimeDate}, someone has shown interest in joining the scout group. Please check the waiting list to verify if that is the case:\n\nThis means there is a potential new young person who has been added to the waiting list. Please check the OSM for more details.\n\nYours in Scouting,\nBenjamin Parsons\n\nThis is an automated message, please do not reply to this email.")
    msg["Subject"] = f"New Young Person - Waiting List"
    msg["From"] = "Ben Parsons"  
    msg["To"] = "Sandra Devine"

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, ["superben1506@gmail.com"], msg.as_string())
        print("Email sent")



