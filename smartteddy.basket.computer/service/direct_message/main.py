# Source: https://www.twilio.com/docs/conversations/using-whatsapp-conversations
# Select Python
# Warning: Twilio is a commercial product and costs money per message when not unsandboxed
import environ
from twilio.rest import Client

environ.Env.read_env()

env = environ.Env(
    # set casting, default value
    IS_WHATSAPP_BUSINESS=(bool, False)
)

is_business_whatsapp = env('IS_WHATSAPP_BUSINESS')
account = env('TWILIO_ACCOUNT_SID')
token = env('TWILIO_AUTH_TOKEN')
phone_from = env('TWILIO_PHONE_FROM')
phone_to = env('TWILIO_PHONE_TO')
twilio_client = Client(account, token)

"""Quickstart"""
message = twilio_client.messages.create(
                              body='Smart Teddy is awesome!',
                              from_=f'whatsapp: {phone_from}',
                              to=f'whatsapp:{phone_to}'
                          )

print(message.sid)  # send message
