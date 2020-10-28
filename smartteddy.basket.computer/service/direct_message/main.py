# Source: https://www.twilio.com/docs/conversations/using-whatsapp-conversations
# Select Python
# Warning: Twilio is a commercial product and costs money per message

from twilio.rest import Client
import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

is_business_whatsapp = False
account = ""
token = ""
phone_from = ""
phone_to = ""
twilio_client = Client(account, token, region="NL")
twilio_client.messages()

# create an new conversation with a person
conversation = twilio_client.conversations.conversations.create()
conversation_id = conversation.sid

# Add participants to the conversation
if not is_business_whatsapp:
    participant = twilio_client.conversations \
        .conversations(conversation_id) \
        .participants \
        .create(messaging_binding_address=phone_from, messaging_binding_proxy_address=phone_to)
    print(participant.sid)
else:
    participant = twilio_client.conversations \
        .conversations(conversation_id) \
        .participants \
        .create(messaging_binding_address=phone_from, messaging_binding_proxy_address=phone_to)
    print(participant.sid)

# Send a message to the participant of the conversation
message = twilio_client.conversations \
    .conversations(conversation_id) \
    .messages \
    .create(
         author='whatsapp:COURIER_WA_NUMBER',
         body='Smart Teddy is being smart?'
     )

