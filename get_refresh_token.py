import os
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
'''
# Set up the OAuth 2.0 flow
flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/gmail.send']
)

# Generate authorization URL
auth_url, _ = flow.authorization_url(prompt='consent')

print(f'Please go to this URL: {auth_url}')

# Get the authorization code from user
code = input('Enter the authorization code: ')
flow.fetch_token(code=code)

# Get the credentials
credentials = flow.credentials

print(f'Refresh token: {credentials.refresh_token}')
'''

# Set up the OAuth 2.0 flow
flow = Flow.from_client_secrets_file(
    'client_secret.json',
    scopes=['https://www.googleapis.com/auth/gmail.send']
)

# Generate authorization URL
auth_url, _ = flow.authorization_url(prompt='consent')

print(f'Please go to this URL: {auth_url}')
print("After you've authorized, you'll be redirected to a page that says 'The authentication flow has completed.'")
print("Copy the entire URL of that page.")

# Get the authorization response from user
auth_response = input('Enter the full URL you were redirected to: ')

# Fetch the tokens
flow.fetch_token(authorization_response=auth_response)

# Get the credentials
credentials = flow.credentials

print(f'Refresh token: {credentials.refresh_token}')
print(f'Access token: {credentials.token}')
print(f'Client ID: {credentials.client_id}')
print(f'Client Secret: {credentials.client_secret}')