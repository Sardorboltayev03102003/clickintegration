from django.shortcuts import render, redirect
from pyclick.utils import PyClickMerchantAPIView
from rest_framework.generics import CreateAPIView


from apps.orders.models import ClickOrder
from apps.orders.serializers import ClickSerializers


class CreateClickOrderView(CreateAPIView):
    serializer_class = ClickSerializers

    def post(self, request, *args, **kwargs):
        amount = request.POST.get('amount')
        order = ClickOrder.objects.create(amount=amount)
        return_url = 'http://127.0.0.1:8000/'
        url = PyClickMerchantAPIView.generate_url(order_id=order.id, amount=str(amount), return_url=return_url)
        return redirect(url)


class OrderCheckAndPayment(PyClickMerchantAPIView):
    def check_order(self, order_id: str, amount: str):
        if order_id:
            try:
                order = ClickOrder.objects.get(id=order_id)
                if order.amount == int(amount):
                    return self.ORDER_FOUND
                else:
                    return self.INVALID_AMOUNT
            except ClickOrder.DoesNotExist:
                return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        try:
            order = ClickOrder.objects.get(id=order_id)
            order.is_paid = True
            order.save()
        except ClickOrder.DoesNotExist:
            print(f"no order object not found:{order_id}")


class OrderTestView(PyClickMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment
