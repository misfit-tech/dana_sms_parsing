from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .helpers import bank_sms_parsing
from rest_framework import status
import json


class SMSParsing(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        sms = data.get('data')
        sms_string = json.dumps(sms)
        print(sms_string)
        parsed_data = bank_sms_parsing.parse_sms_data(data=sms_string)

        context = {
            'message': 'Parsed SMS',
            'data': parsed_data,
            'success': True
        }

        return Response(context, status=status.HTTP_200_OK)
