from django.urls import path

from apps.orders.views import *

urlpatterns = [
    path('', CreateClickOrderView.as_view(), name='create-click-order'),
    path('click/transaction/', OrderTestView.as_view(), name='check-order'),
]
