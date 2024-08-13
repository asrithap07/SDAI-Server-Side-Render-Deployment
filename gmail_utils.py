from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google.auth.exceptions import RefreshError
from email.mime.text import MIMEText
import base64
from googleapiclient.discovery import build
from django.conf import settings

def get_gmail_service():
    creds = Credentials.from_authorized_user_info(
        {
            "client_id": settings.GMAIL_CLIENT_ID,
            "client_secret": settings.GMAIL_CLIENT_SECRET,
            "refresh_token": settings.GMAIL_REFRESH_TOKEN,
        },
        ["https://www.googleapis.com/auth/gmail.send"]
    )

    if not creds.valid:
        if creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError:
                print("Refresh token is invalid or expired. Please obtain a new one.")
                return None
        else:
            print("Credentials are invalid. Please obtain new credentials.")
            return None

    return build('gmail', 'v1', credentials=creds)

def send_email(to, subject, body):
    service = get_gmail_service()
    if not service:
        return False

    message = MIMEText(body)
    message['to'] = to
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

    try:
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False