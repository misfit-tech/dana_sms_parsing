from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers import bank_sms_parsing
from rest_framework import status
import json
import requests



class SMSParsing(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        sms = data.get('data')
        authorization = request.META.get('HTTP_AUTHORIZATION')
        if authorization:
            try:
                token = authorization.split()[0]
            except ValueError:
                token = None
        else:
            context = {
                'message': 'Please provide authorization',
                'data': None,
                'success': False
            }
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        if token == 'Bearer':
            if sms:
                try:
                    parsed_data = bank_sms_parsing.parse_sms_data(data=sms)
                    header = {
                        'Content-type': 'application/json',
                        'Authorization': authorization
                    }
                    post_data = requests.post('http://softcell.yearstech.com/demo/dana/api/sms/parse',
                                              json=json.loads(parsed_data),
                                              headers=header
                                              )
                    return Response(post_data.json(), status=status.HTTP_200_OK)
                except ValueError:
                    context = {
                        'message': 'Bad Format',
                        'data': None,
                        'success': False
                    }
                    return Response(context, status=status.HTTP_400_BAD_REQUEST)
            else:
                context = {
                    'message': 'No Content',
                    'data': None,
                    'success': False
                }
                return Response(context, status=status.HTTP_204_NO_CONTENT)
        else:
            context = {
                'message': 'Please provide valid authorization',
                'data': None,
                'success': False
            }
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)
