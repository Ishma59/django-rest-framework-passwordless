import africastalking
from django.conf import settings

class Sms:
    def __init__(self):

    	africastalking.initialize(settings.SMS_USERNAME, settings.SMS_API_KEY)

    	self.sms = africastalking.SMS

    def send_sms(self, message, recipient):
    	response = self.sms.send(message, ("+" + str(recipient)).split())
    	print(response)
    	if response["SMSMessageData"]["Recipients"][0]["status"]== "Success":
    		return True
    	

