from django.db import models
import uuid as uuid_lib

from ..user.models import User


class MembershipType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False,
        db_index=True, )
    type_name = models.CharField(max_length=30)
    membership_period = models.CharField(max_length=30)
    membership_amount = models.FloatField()


class Member(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False,
        db_index=True, )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(MembershipType, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=10)  # [0] female, [1] male
    joining_date = models.DateField()
    end_of_membership_date = models.DateField()
