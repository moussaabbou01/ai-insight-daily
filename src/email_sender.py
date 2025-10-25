"""
Email Sender module for sending emails via SMTP.
Handles Gmail SMTP configuration and email delivery.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    """Class to send emails using Gmail SMTP"""
    
    def __init__(self, smtp_server: str, smtp_port: int, from_email: str, app_password: str):
        """
        Initialize email sender
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            from_email: Sender email address
            app_password: Gmail app password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.from_email = from_email
        self.app_password = app_password
    
    def send_html_email(self, to_email: str, subject: str, html_content: str):
        """
        Send HTML email
        
        Args:
            to_email: Recipient email address
            subject: Email subject line
            html_content: HTML content of the email
            
        Raises:
            Exception: If email sending fails
        """
        # Create message
        msg = MIMEMultipart('alternative')
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        # Attach HTML content
        html_part = MIMEText(html_content, 'html')
        msg.attach(html_part)
        
        try:
            # Connect to SMTP server and send
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as smtp:
                smtp.login(self.from_email, self.app_password)
                smtp.sendmail(self.from_email, to_email, msg.as_string())
        except smtplib.SMTPException as e:
            raise Exception(f"Failed to send email: {str(e)}")
    
    def send_plain_email(self, to_email: str, subject: str, text_content: str):
        """
        Send plain text email
        
        Args:
            to_email: Recipient email address
            subject: Email subject line
            text_content: Plain text content
            
        Raises:
            Exception: If email sending fails
        """
        msg = MIMEText(text_content)
        msg['From'] = self.from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        try:
            with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as smtp:
                smtp.login(self.from_email, self.app_password)
                smtp.sendmail(self.from_email, to_email, msg.as_string())
        except smtplib.SMTPException as e:
            raise Exception(f"Failed to send email: {str(e)}")
