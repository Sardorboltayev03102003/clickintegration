from rest_framework import serializers

from .models import ClickOrder


class ClickSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClickOrder
        fields = ('amount',)

#

# class ClickTransactionSerializers(serializers.Serializer):
#     click_trans_id = serializers.CharField(max_length=255, required=True, allow_blank=True)
#     service_id = serializers.CharField(max_length=255, required=True, allow_blank=True)
#     merchant_trans_id = serializers.CharField(max_length=255, required=True, allow_blank=True)
#     merchant_prepare_id = serializers.CharField(max_length=255, required=False,allow_null=True,allow_blank=True)
#     amount = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
#     action = serializers.CharField(allow_blank=True)
#     error = serializers.CharField(allow_blank=True)
#     error_note = serializers.CharField(allow_blank=True)





#     sign_time = serializers.CharField()
#     sign_string = serializers.CharField(allow_blank=True)
#     click_paydoc_id = serializers.CharField(allow_blank=True)
