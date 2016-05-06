from django.db import models
from django.utils import timezone
from core.models import BaseModel


class Receipt(BaseModel):
    date_entered = models.DateTimeField(default=timezone.now)
    receipt_date = models.DateTimeField()
    vendor = models.CharField(max_length=50)
    account = models.CharField(max_length=50)
    description = models.TextField()
    image = models.FileField()
