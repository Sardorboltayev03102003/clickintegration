from django.db import models
from ..commans.models import BaseModel
from django.utils.translation import gettext_lazy as _


class ClickOrder(BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

#
# class ClickTransaction(BaseModel):
#     """ Класс ClickTransaction """
#     PROCESSING = 'processing'
#     WAITING = "waiting"
#     CONFIRMED = 'confirmed'
#     CANCELED = 'canceled'
#     ERROR = 'error'
#     STATUS = [
#         (WAITING, WAITING),
#         (PROCESSING, PROCESSING),
#         (CONFIRMED, CONFIRMED),
#         (CANCELED, CANCELED),
#         (ERROR, ERROR)
#     ]
#     click_paydoc_id = models.CharField(max_length=255, null=True, blank=True,
#                                        verbose_name=_('Номер платежа в системе CLICK'))
#     amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('Сумма платежа'))
#     status = models.CharField(max_length=255, choices=STATUS, default=WAITING,
#                               verbose_name=_('Статус платежа'))
#     action = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Действие'))
#     extra_data = models.TextField(blank=True, default="")
#     message = models.TextField(blank=True, default="")
#
#     def __str__(self):
#         return f"{self.click_paydoc_id}"
#
#     def change_status(self, status: str, message=""):
#         self.status = status
#         self.message = message
#         self.save(update_fields=['status', 'message'])
