import json
import os
from django.http import HttpResponse
from Crypto.PublicKey import RSA

import encryption

class EncryptionMiddleware(object):

    def __init__(self, arg1):
        print('arg1: ', arg1)
        self.get_response = arg1
        self.get_request_excluded_paths = [] #['/api/encryption/public-key',]
        self.get_response_excluded_paths = []
        self.post_request_excluded_paths = []
        self.post_response_excluded_paths = []

    def unencrypt_request_data(self, request):
        print('* unencrypt_request_data()')
        json_data = json.loads(request.body)
        key =  open(os.path.dirname(os.path.abspath(__file__))+'/pair.pem', 'r').read()
        print('- json_data: ', json_data)
        return encryption.decrypt(json_data['data'], key) if 'data' in json_data else "{}"

    def encrypt_response_data(self, request, response):
        print('* encrypt_response_data()')
        print('- request.body: ', request.body)
        request_data = json.loads(request.body)

        if ('CLIENT_KEY' in request_data):
            json_data = json.loads(response.content)
            new_data = {'SERVER_KEY': key_string,
                        'data': encryption.encrypt(response.content, request_data['CLIENT_KEY'])}
            return json.dumps(new_data)
        else:
            return "{}"

    def process_get_request(self, request):
        print('-* process_get_request()')
        if request.path not in self.get_request_excluded_paths:
            print('- processing...')
        else:
            print('- this is an excluded path (will not be decrypted')

    def process_get_response(self, request, response):
        print('-* process_get_response()')
        if request.path not in self.get_response_excluded_paths:
            print('- processing...')
        else:
            print('- this is an excluded path (will not be decrypted')
    
    def process_post_request(self, request):
        print('-* process_post_request()')
        if request.path not in self.get_request_excluded_paths:
            print('- processing...')
        else:
            print('- this is an excluded path (will not be decrypted')

    def process_post_response(self, request, response):
        print('-* process_post_response()')
        if request.path not in self.post_response_excluded_paths:
            print('- processing...')
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
