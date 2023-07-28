from django.urls import path
from ..views  import AccessToken, InvoicePDF

urlpatterns = [
    path('access-token/', AccessToken.as_view(), name='access-token'),
    path('invoice-pdf/', InvoicePDF.as_view(), name='invoice-pdf'),
]

