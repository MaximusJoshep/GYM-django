from django.db import models
import uuid as uuid_lib


class User(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False,
        db_index=True, )
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
