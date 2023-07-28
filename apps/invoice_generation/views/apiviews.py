from rest_framework.views import APIView
from rest_framework.response import Response
from ..utils import create_access_token, create_invoice, get_invoice_details

class AccessToken(APIView):
    def get(self,request):
        token=create_access_token()
        return Response({"token":token},status=200)
    


class InvoicePDF(APIView):
    def post(self, request):
        # Get the access token from the request data
        access_token = request.data.get('access_token')

        if access_token:
            # Create the invoice
            invoice_data = create_invoice(access_token)
            if invoice_data is not None and 'invoice' in invoice_data:
                invoice_id = invoice_data['invoice']['invoice_id']
                print("Invoice created with ID:", invoice_id)

                # Retrieve the invoice details in PDF format
                invoice_details_pdf = get_invoice_details(invoice_id, access_token)

                if invoice_details_pdf is not None:
                    # Write the PDF content to a file or do any other processing
                    with open("invoice_details.pdf", "wb") as file:
                        file.write(invoice_details_pdf)

                    return Response({"message": "Invoice details saved as invoice_details.pdf"}, status=200)
                else:
                    return Response({"error": "Failed to retrieve invoice details"}, status=500)
            else:
                return Response({"error": "Failed to create invoice"}, status=500)
        else:
            return Response({"error": "Access token not provided"}, status=400)