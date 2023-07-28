import requests
from dotenv import load_dotenv
import os

load_dotenv()

# Access the environment variables
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
refresh_token = os.getenv("REFRESH_TOKEN")
organization_id = os.getenv("ORGANIZATION_ID")

refresh_token_url = f'https://accounts.zoho.in/oauth/v2/token?refresh_token={refresh_token}&client_id={client_id}&client_secret={client_secret}&redirect_uri=https://httpbin.org/anything&grant_type=refresh_token'

def create_access_token():
    """
    Creates an access token using the provided environment variables.

    Returns:
        str: The created access token.

    Raises:
        ValueError: If the access token cannot be retrieved.
    """

    try:
        access_token = refresh_access_token(refresh_token_url)
        print('Access Token:', access_token)
        return access_token
    except ValueError as e:
        print('Token refresh failed:', str(e))
        return None

def refresh_access_token(refresh_token_url):
    response = requests.post(refresh_token_url)
    token_data = response.json()
    access_token = token_data.get('access_token')
    if access_token is None:
        raise ValueError('Failed to retrieve access token')
    return access_token

def create_invoice(access_token):
    """
    Create an invoice using the Zoho Books API.

    Args:
        access_token (str): The access token used for authorization.

    Returns:
        dict or None: The created invoice data as a dictionary if successful,
        None otherwise.
    """
    create_invoice_url = f"https://www.zohoapis.com/books/v3/invoices?organization_id={organization_id}"

    payload = {
        # Invoice creation payload data
        # ...
    }

    headers = {
        'Authorization': f"Zoho-oauthtoken {access_token}",
        'Content-Type': "application/json"
    }

    response = requests.post(create_invoice_url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Invoice creation failed. Response:", response.text)
        return None


def get_invoice_details(invoice_id, access_token):
    """
    Retrieve the details of an invoice in PDF format.

    Args:
        invoice_id (str): The ID of the invoice to retrieve details for.
        access_token (str): The access token used for authorization.

    Returns:
        bytes or None: The invoice details in PDF format as bytes if successful,
        None otherwise.
    """
    get_invoice_url = f"https://www.zohoapis.com/books/v3/invoices/{invoice_id}?organization_id={organization_id}"

    headers = {
        'Authorization': f"Zoho-oauthtoken {access_token}",
        'accept': "application/pdf"
    }

    response = requests.get(get_invoice_url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to retrieve invoice details. Response:", response.text)
        return None

# Generate the access token
access_token = create_access_token()

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