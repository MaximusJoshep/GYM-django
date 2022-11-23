from datetime import datetime

from django.db import models
import uuid as uuid_lib

from ..member.models import Member


class Payment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False,
        db_index=True, )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_datetime = models.TimeField(default=datetime.now())
