from rest_framework import generics, permissions
from .models import Enroll
from .serializers import EnrollSerializer
from rest_framework.decorators import api_view
from sslcommerz_lib import SSLCOMMERZ 
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.conf import settings as main_settings


class EnrollCreateView(generics.CreateAPIView):
    serializer_class = EnrollSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

@api_view(['POST'])
def initiate_payment(request):
    # user=request.user
    # print(user)
    settings = { 'store_id': 'alo682e1dbdb5d29', 'store_pass': 'alo682e1dbdb5d29@ssl', 'issandbox': True }
    sslcz = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = 6500
    post_body['currency'] = "BDT"
    post_body['tran_id'] = f"txn_12df33adh5"
    post_body['success_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/success/"
    post_body['fail_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/fail/"
    post_body['cancel_url'] = f"{main_settings.BACKEND_URL}/api/v1/payment/cancel/"
    post_body['emi_option'] = 0
    post_body['cus_name'] = "user.first_nameuser.last_name"
    post_body['cus_email'] = 'user.email'
    post_body['cus_phone'] = 'user.phone_number'
    post_body['cus_add1'] = 'user.address'
    post_body['cus_city'] = "Dhaka"
    post_body['cus_country'] = "Bangladesh"
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"


    response = sslcz.createSession(post_body) 
    print(response)
    if response.get("status") == 'SUCCESS':
        return Response({"payment_url": response['GatewayPageURL']})
    return Response({"error": "Payment initiation failed"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def payment_success(request):
    print("Inside success")
    order_id = request.data.get("tran_id").split('_')[1]
    order = Order.objects.get(id=order_id)
    order.status = "Ready To Ship"
    order.save()
    return HttpResponseRedirect(f"{main_settings.FRONTEND_URL}/")



@api_view(['POST'])
def payment_cancel(request):
    return HttpResponseRedirect(f"{main_settings.FRONTEND_URL}/")


@api_view(['POST'])
def payment_fail(request):
    print("Inside fail")
    return (f"{main_settings.FRONTEND_URL}/")