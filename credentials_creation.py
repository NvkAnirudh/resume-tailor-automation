import os
import json

def create_credentials():
    # Read Google OAuth credentials from environmental variables
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    
    # The credentials.json structure expected by Google's OAuth
    credentials_data = {
        "web":{
            "client_id":GOOGLE_CLIENT_ID,
            "project_id":"resume-tailoring-436517",
            "auth_uri":"https://accounts.google.com/o/oauth2/auth",
            "token_uri":"https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
            "client_secret":GOOGLE_CLIENT_SECRET
        }
    }
    
    # Write the credentials data to a temporary JSON file
    with open('credentials.json', 'w') as credentials_file:
        json.dump(credentials_data, credentials_file)
    
    # Now, this generated credentials.json file can be used for the OAuth flow in the app