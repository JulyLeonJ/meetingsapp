from google.oauth2 import service_account
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os


credentials = service_account.Credentials.from_service_account_file('.\credentials.json')

SCOPES = ['https://www.googleapis.com/auth/calendar']

def get_credentials():
    creds = None
    if os.path.exists('token.json'):
        creds = service_account.Credentials.from_service_account_file(
            'credentials.json', scopes=SCOPES
        )
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = service_account.Credentials.from_service_account_file(
                'credentials.json', scopes=SCOPES
            )
    return creds

credentials = get_credentials()

def create_event(summary, start_datetime, end_datetime):
    service = build('calendar', 'v3', credentials=credentials)
    event

    

##______________________________________________________##


from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/calendar']

