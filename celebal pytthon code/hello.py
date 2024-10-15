from twilio.rest import Client

# Twilio credentials
api_key = "XXXXX"
api_secret = "YYYYY"
account_sid = "RRRRRR"

# Conversation and participant SIDs
conversation_sid = 'AAAAA'
participant_sid = 'BBBBB'

# Initialize the Twilio client
client = Client(api_key, api_secret, account_sid)

# Fetch the conversation
conversation = client.conversations.v1.conversations(conversation_sid).fetch()

# Trigger the typing indicator for the participant
conversation.typing(participant_sid)
