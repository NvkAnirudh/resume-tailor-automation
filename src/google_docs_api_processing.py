from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

# SCOPES for Google Docs API
SCOPES = ['https://www.googleapis.com/auth/documents']

# Authenticate and create Google Docs API service
def google_docs_auth():
    creds = None

    # Check if token.json exists (for existing OAuth tokens)
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no valid credentials, go through the flow to get new ones
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES
            )
            creds = flow.run_local_server(port=8502)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('docs', 'v1', credentials=creds)

# Functions to create a Google doc with formatted text
def create_google_doc(service, text):
    # Request body for creating a new document
    doc = {
        'title': 'Updated Resume'
    }
    doc = service.documents().create(body=doc).execute()

    # Document ID
    doc_id = doc.get('documentId')

    # Insert text into the document with:
    # - Times New Roman
    # - Font size of 10
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': text
            }
        },
        {
            'updateTextStyle': {
                'range': {
                    'startIndex': 1,
                    'endIndex': len(text) + 1
                },
                'textStyle': {
                    'fontSize': {
                        'magnitude': 10,
                        'unit': 'PT'
                    },
                    'weightedFontFamily': {
                        'fontFamily': 'Times New Roman'
                    }
                },
                'fields': 'fontSize,weightedFontFamily'
            }
        }
    ]

    # Send the requests to the Google Docs API
    service.documents().batchUpdate(documentId=doc_id, body={'requests': requests}).execute()

    # Return the document URL
    return f'https://docs.google.com/document/d/{doc_id}/edit'