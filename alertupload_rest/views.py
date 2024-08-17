from multiprocessing.connection import Client
from alertupload_rest.serializers import UploadAlertSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import JsonResponse
from threading import Thread
from django.core.mail import send_mail
import re
import logging

from wd_ss import settings
import requests
import json

from sinch import SinchClient

logger = logging.getLogger(__name__)

def start_new_thread(function):
    def decorator(*args, **kwargs):
        t = Thread(target = function, args = args, kwargs = kwargs)
        #t.daemon = True.start()
        t.daemon = True
        t.start()
    return decorator

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def post_alert(request):

    serializer = UploadAlertSerializer(data=request.data)

    if serializer.is_valid():
        try:
            alert = serializer.save()
            #added with sinch 
            identify_sms(serializer)
            #end of add
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Unable to save data!', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response({'error': 'Invalid data!', 'details': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
def identify_sms(serializer):
    if re.compile(r"^\+?1?\s*\(?[2-9][0-9]{2}\)?[-.\s]?[0-9]{3}[-.\s]?[0-9]{4}$").match(serializer.data['alert_receiver']):
        print("Valid Mobile Number")
        send_sms(serializer)
    else:
        print("Invalid Mobile Number")

#TWILIO FUNCTION
'''
@start_new_thread
def send_sms(serializer):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messagesz.create(body=prepare_alert_message(serializer),
                                      from_=settings.TWILIO_NUMBER,
                                      to=serializer.data['alert_receiver'])
'''

@start_new_thread
def send_sms(serializer):
    logger.info("send_sms function called")
    try:
        #print(f"Attempting to send SMS to {serializer.data['alert_receiver']}")
        logger.info(f"Attempting to send SMS to {serializer.data['alert_receiver']}")
        sinch_client = SinchClient(
            key_id=settings.SINCH_KEY_ID,
            key_secret=settings.SINCH_KEY_SECRET,
            project_id=settings.SINCH_PROJECT_ID
        )

        message = prepare_alert_message(serializer)
        #print(f"Message to be sent: {message}")
        logger.info(f"Message to be sent: {message}")
        
        send_batch_response = sinch_client.sms.batches.send(
            body=message,
            to=[serializer.data['alert_receiver']],
            from_=settings.SINCH_NUMBER,
            delivery_report="none"
        )

        #print(f"SMS sent successfully. Response: {send_batch_response}")
        logger.info(f"SMS sent successfully. Response: {send_batch_response}")
    except Exception as e:
        #print(f"An error occurred while sending SMS: {str(e)}")
        #print(f"Serializer data: {serializer.data}")
        logger.error(f"An error occurred while sending SMS: {str(e)}", exc_info=True)
        logger.error(f"Serializer data: {serializer.data}")
                                      
def prepare_alert_message(serializer):
    #image_data = split(serializer.data['image'], ".")
    #uuid = split(uuid_with_slashes[3], "/")
    #url = 'hhtp://127.0.0.1:8000/alert' + uuid

    alert_id = serializer.data['id']  # Assuming the serializer includes the alert's ID
    url = f'https://sdai-server-side-render-deployment.onrender.com/alert/{alert_id}'

    return f'Weapon Detected! View alert at {url}'

#def split(value, key):
    #return str(value).split(key)