from django.http import HttpResponse, JsonResponse
import datetime
import os
import json
import encryption.encryption as encryption

# Create your views here.
def public_key(request):
    key =  encryption.server_public_key().exportKey('PEM').decode()
    data = {'SERVER_KEY': key}
    return JsonResponse(data)

def current_datetime(request):
    now = datetime.datetime.now()
    data = {'now': now}
    return JsonResponse(data)
