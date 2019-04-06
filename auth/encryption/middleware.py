import json
import os
from django.http import HttpResponse
from Crypto.PublicKey import RSA

import encryption.encryption as encryption

class EncryptionMiddleware(object):

    def __init__(self, arg1):
        print('arg1: ', arg1)
        self.get_response = arg1
        self.get_request_excluded_paths = []
        self.get_response_excluded_paths = ['/api/encryption/public-key',]
        self.post_request_excluded_paths = []
        self.post_response_excluded_paths = []

    def process_get_request(self, request):
        print('-* process_get_request()')
        if request.path not in self.get_request_excluded_paths:
            print('- processing...')
        else:
            print('- this is an excluded path (will not be decrypted')

    def process_get_response(self, request, response):
        print('-* process_get_response()')
        if request.path not in self.get_response_excluded_paths:
            if (response["Content-Type"]=='application/json'):
                print('- processing the response content (is json)')
                print('- server key pair: ', encryption.server_key_pair())
                new_data = {'SERVER_KEY': encryption.server_public_key().exportKey('PEM').decode(),
                            'data': encryption.encrypt(response.content, RSA.importKey(request.GET['CLIENT_KEY'])).decode()} #.decode('latin-1') #encryption.server_key_pair()
                response.content = json.dumps(new_data)
            else:
                print('- did not process the response (not json)')
        else:
            print('- this is an excluded path (will not be decrypted')
    
    def process_post_request(self, request):
        print('-* process_post_request()')
        if request.path not in self.get_request_excluded_paths:
            print('- processing...')
            if (request.META["CONTENT_TYPE"]=='application/x-www-form-urlencoded'):
                print('- processing the request content (is x-www-form-urlencoded)')
                print('- request.POST["CLIENT_KEY"]: ', request.POST['CLIENT_KEY'])
                print('- request.POST["data"]: ', request.POST['data'])
                request.POST = request.POST.copy()
                new_data = json.loads( encryption.decrypt(request.POST['data'].encode(), encryption.server_key_pair()).decode() )
                request.POST['grant_type'] = new_data['grant_type']
                request.POST['username'] = new_data['username']
                request.POST['password'] = new_data['password']

            elif (request.META["CONTENT_TYPE"]=='application/json'):
                 print('- processing the request content (is json)')

            else:
                print('- did not process the request (not json)')

        else:
            print('- this is an excluded path (will not be decrypted')

    def process_post_response(self, request, response):
        print('-* process_post_response()')
        if request.path not in self.post_response_excluded_paths:
            print('processing...')
        else:
            print('- this is an excluded path (will not be decrypted')

    def __call__(self, request):
        print('')
        print('--- EncryptionMiddleware (JSON Only) ---')
        print('- request.method: ', request.method)
        print('- request.path: ', request.path)
        print('- request.META["CONTENT_TYPE"]: ', request.META["CONTENT_TYPE"])

        # process requests
        if (request.method=='GET'):
            self.process_get_request(request)
        elif (request.method=='POST'):
            self.process_post_request(request)
        else:
            print('-X not a supported request.method type')

        # decrypt request json here
        #if (request.META["CONTENT_TYPE"]=='application/json' and request.method=='POST'):
        #    print('- request.body: ', request.body)
        #    request._body = self.unencrypt_request_data(request).encode()

        response = self.get_response(request)
        print('- response["Content-Type"]: ', response["Content-Type"])
        print('- response.content: ', response.content)

        # process responses
        if (request.method=='GET'):
            self.process_get_response(request, response)
        elif (request.method=='POST'):
            self.process_post_response(request, response)
        else:
            print('-X not a supported request.method type')

        # encrypt response json here
        #if ((request.META["CONTENT_TYPE"]==response["Content-Type"]=='application/json') or 
        #    (request.META["CONTENT_TYPE"]=='text/plain' and response["Content-Type"]=='application/json')):
        #    print('- response.content: ', response.content)
        #    response.content = self.encrypt_response_data(request, response).encode()
            

        print('----------------------------------------')
        return response
