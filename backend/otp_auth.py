import pyotp
import smtplib
from email.message import EmailMessage
from configparser import ConfigParser
import os

class OtpAuth:
    def __init__(self):
        self.config = ConfigParser()
        # get path to read config.ini
        config_path = os.path.join(os.path.join(os.path.dirname(__file__), 'config.ini'))
        print(config_path)
        self.config.read(config_path)
        self.otp_secret = pyotp.random_base32()
        self.otp = pyotp.TOTP(self.otp_secret, interval=120)
        self.email = 'manan.abbottt@gmail.com'
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587  # Correct for STARTTLS
        self.smtp_user = 'manan.abbottt1902@gmail.com'
        self.smtp_password = self.config['confidential']['sender_password']

    def generate_password(self):
        return self.otp.now()
    
    def send_otp(self):
        otp = self.generate_password()
        msg = EmailMessage()
        msg.set_content(f'Your OTP is {otp}')
        msg['Subject'] = 'OTP for authentication'
        msg['From'] = self.smtp_user
        msg['To'] = self.email

        # Use SMTP (not SMTP_SSL) with starttls()
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.ehlo()  # Can be omitted, smtplib does it automatically
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(msg)

    def verify_otp(self, totp):
        return self.otp.verify(totp)