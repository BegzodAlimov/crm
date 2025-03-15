from django.db import models
from education.models import Group
from tools.models import BasedModel
from users.models import User


# Create your models here.
class Payment(BasedModel):
    PAYMENT_TYPE = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('transaction', 'Transaction'),
    ]

    amount = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='payments')
    month = models.IntegerField()
    payment_date = models.DateField()
    payment_type = models.CharField(max_length=12, choices=PAYMENT_TYPE, default='cash')

    def __str__(self):
        return f'{self.student} - {self.amount} {self.payment_type}'


class Discount(BasedModel):
    amount = models.IntegerField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discounts')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='discounts')
    month = models.IntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)