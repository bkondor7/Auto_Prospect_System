import smtplib
from email.mime.text import MIMEText

# Auto Outreach
def send_email(to_address, subject, message):
    from_address = 'myEmail@somewhere.com'
    password = 'password'
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address
    
    server = smtplib.SMTP_SSL('smtp.somehwere.com', 465)
    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string())
    server.quit()
    
    def send_prospecting_emails(listings):
        for listing in listings:
            contact_email = listing[3]
            subject = f"Interest in your property: {listing[1]}"
            message = f"Hello,\n\nI am interested in your property listed at {listing[1]} for {listing[2]}"
            send_email(contact_email, subject, message)