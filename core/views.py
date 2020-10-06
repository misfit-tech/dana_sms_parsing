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
        if sms:
            parsed_data = bank_sms_parsing.parse_sms_data(data=sms)
            context = {
                'message': 'Parsed SMS',
                'data': parsed_data,
                'success': True
            }
            header = {
                'Content-type': 'application/json'
            }
            post_data = requests.post('http://softcell.yearstech.com/demo/dana/api/sms/parse',
                                      data=parsed_data,
                                      headers=header
                                      )
            return Response(context, status=status.HTTP_200_OK)
        else:
            context = {
                'message': 'No Content',
                'data': None,
                'success': False
            }
            return Response(context, status=status.HTTP_204_NO_CONTENT)