from django.http import HttpResponse, JsonResponse
import datetime
import os
import json

# Create your views here.
def public_key(request):
    key =  open(os.path.dirname(os.path.abspath(__file__))+'/public.pem', 'r').read()
    data = {'SERVER_KEY': key}
    return JsonResponse(data)

def current_datetime(request):
    now = datetime.datetime.now()
    data = {'now': now}
    return JsonResponse(data)
