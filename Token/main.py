import os
from datetime import timedelta
from azure.communication.identity import CommunicationIdentityClient, CommunicationUserIdentifier

try:
   print("Azure Communication Services - Access Tokens Quickstart")
   # Quickstart code goes here
except Exception as ex:
   print("Exception:")
   print(ex)

# This code demonstrates how to retrieve your connection string
# from an environment variable.
connection_string = os.environ["COMMUNICATION_SERVICES_CONNECTION_STRING"]

# Instantiate the identity client
client = CommunicationIdentityClient.from_connection_string(connection_string)

endpoint = os.environ["COMMUNICATION_SERVICES_ENDPOINT"]
client = CommunicationIdentityClient(endpoint, DefaultAzureCredential())

identity = client.create_user()
print("\nCreated an identity with ID: " + identity.properties['id'])

# Issue an access token with a validity of 24 hours and the "voip" scope for an identity
token_result = client.get_token(identity, ["voip"])
print("\nIssued an access token with 'voip' scope that expires at " + token_result.expires_on + ":")
print(token_result.token)

# Issue an access token with a validity of an hour and the "voip" scope for an identity
token_expires_in = timedelta(hours=1)
token_result = client.get_token(identity, ["voip"], token_expires_in=token_expires_in)

# Issue an identity and an access token with a validity of 24 hours and the "voip" scope for the new identity
identity_token_result = client.create_user_and_token(["voip"])

# Get the token details from the response
identity = identity_token_result[0]
token = identity_token_result[1].token
expires_on = identity_token_result[1].expires_on
print("\nCreated an identity with ID: " + identity.properties['id'])
print("\nIssued an access token with 'voip' scope that expires at " + expires_on + ":")
print(token)

# The existingIdentity value represents the Communication Services identity that's stored during identity creation
identity = CommunicationUserIdentifier(existingIdentity)
token_result = client.get_token(identity, ["voip"])

client.revoke_tokens(identity)
print("\nSuccessfully revoked all access tokens for identity with ID: " + identity.properties['id'])

client.delete_user(identity)
print("\nDeleted the identity with ID: " + identity.properties['id'])

