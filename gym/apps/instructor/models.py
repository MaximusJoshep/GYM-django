from django.db import models
import uuid as uuid_lib

from ..user.models import User


class Instructor(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False,
        db_index=True, )
    instructor_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=9)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
