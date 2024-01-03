import os
from veryfi import Client


class VeryfiAPI :
    
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
        response = self.client.process_document(
            file_path=file_path, delete_after_processing=self.DELETE_AFTER_PROCESSING
        )
        return response

client = VeryfiAPI()
response = client.process_document(file_path="bill_image/images.jpeg")
print(response)