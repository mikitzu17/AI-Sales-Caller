from azure.communication.identity import CommunicationIdentityClient

# Paste your actual connection string here
connection_string = "endpoint=https://YOUR_RESOURCE.communication.azure.com/;accesskey=YOUR_ACCESS_KEY"

client = CommunicationIdentityClient.from_connection_string(connection_string)
user = client.create_user()
print("ACS User ID:", user.properties['id'])
