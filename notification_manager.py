from twilio.rest import Client
import smtplib

TWILIO_SID = "AC6543470a6fbaa12fd733787fbf771082"
TWILIO_AUTH_TOKEN = "fff26567a4a1381783f118fd026b62a7"
TWILIO_VIRTUAL_NUMBER = "+13612825803"
TWILIO_VERIFIED_NUMBER = "+16475620216"
EMAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "zanechan136@gmail.com"
MY_PASSWORD = "lxikjnaxdqgvykpp"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )

    def send_emails(self, emails, message):
        with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS, 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
