import pyotp
import smtplib
from email.message import EmailMessage
from configparser import ConfigParser
import os

class OtpAuth:
    def __init__(self):
        self.config = ConfigParser()
        config_path = os.path.join(os.path.join(os.path.dirname(__file__), 'config.ini'))
        self.config.read(config_path)
        self.otp_secret = pyotp.random_base32()
        self.otp = pyotp.TOTP(self.otp_secret, interval=120)
        self.email = 'manan.abbottt@gmail.com'
        self.smtp_server = 'smtp.gmail.com'
        self.smtp_port = 587
        self.smtp_user = 'manan.abbottt1902@gmail.com'
        print(self.config['confidential'])
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

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(self.smtp_user, self.smtp_password)
            server.send_message(msg)

    def verify_otp(self, totp):
        return self.otp.verify(totp)