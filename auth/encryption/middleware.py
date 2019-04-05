import json
from django.http import HttpResponse
from Crypto.PublicKey import RSA

import encryption

class EncryptionMiddleware(object):

    def __init__(self, arg1):
        print('arg1: ', arg1)
        self.get_response = arg1

    def unencrypt_request_data(self, request):
        print('* unencrypt_request_data()')
        json_data = json.loads(request.body)

        if ('CLIENT_KEY' in json_data):
            key =  RSA.importKey(json_data['CLIENT_KEY'].encode())
            print('- json_data: ', json_data)
            json_data['data'] = json.loads(encryption.decrypt(json_data['data'], key))
            return json.dumps(json_data)
        else:
            return json_data

    def __call__(self, request):
        print('--- EncryptionMiddleware (JSON Only) ---')
        print('- request.META["CONTENT_TYPE"]: ', request.META["CONTENT_TYPE"])
        if (request.META["CONTENT_TYPE"]=='application/json'):
            print('- request.body: ', request.body)
            request._body = self.unencrypt_request_data(request).encode()
            self.unencrypt_request_data(request)

        response = self.get_response(request)

        if (request.META["CONTENT_TYPE"]=='application/json'):
            print('- response.content: ', response.content)
            print('- response["Content-Type"]: ', response["Content-Type"])

        print('----------------------------------------')
        return response
