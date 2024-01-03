from veryfi import Client
from django.shortcuts import render
from rest_framework.response import Response
from .serializers import VeryfiAPISerializer
from rest_framework.decorators import api_view


class VeryfiAPI :
    """
    Wrapper for accessing the Veryfi API's
    API documentation: https://veryfi.github.io/veryfi-python/reference/veryfi/#client
    """

    VERYFI_CLIENT_ID = 'vrfP7DKJEop9FK9g3HbyjvfxsxPhddoHMN9ysl0'
    VERYFI_CLIENT_SECRET = 'eKdok3MYgY7Unv2TLaBLLonBOEY3O29f7nHocTBZzYpXNo32Y9bWyRKrYAxCrFHEnHCSxrP6VaVx669PE9CUlYz3asWDWr1ffAyysoHli6rAo6YS2pC67e9y4fkvHIfr'
    VERYFI_USERNAME = 'manu.benny'
    VERYFI_API_KEY = '1732f703294df7e246086e8e0593df47'

    DELETE_AFTER_PROCESSING = True

    def __init__(self):
        self.client = Client(
            self.VERYFI_CLIENT_ID,
            self.VERYFI_CLIENT_SECRET,
            self.VERYFI_USERNAME,
            self.VERYFI_API_KEY,
        )

    def process_document(
        self,
        file_path,
    ):
        """
        sends the document to veryfi and receives the process OCR data in response
        """
        processed_data  = self.client.process_document(
            file_path=file_path, delete_after_processing=self.DELETE_AFTER_PROCESSING
        )

        return processed_data

@api_view(['GET'])
def my_view(request):
    # Instantiate VeryfiAPI and call process_document
    client = VeryfiAPI()
    processed_data= client.process_document(file_path="bill_image/images.jpeg")
    serializer = VeryfiAPISerializer(processed_data)
    print(serializer.data)
    return Response(serializer.data, status=201)