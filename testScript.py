import base64

# Replace with your actual ACS connection string
connection_string = "endpoint=https://YOUR_RESOURCE.communication.azure.com/;accesskey=YOUR_ACCESS_KEY"

# Extract the access key from the connection string
try:
    access_key = connection_string.split("accesskey=")[1]
    decoded_key = base64.b64decode(access_key)  # Try decoding the key
    print("✅ Connection string is correctly formatted!")
except Exception as e:
    print("❌ Invalid access key format:", e)
