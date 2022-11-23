from django.db import models
from datetime import datetime
import uuid as uuid_lib

from ..instructor.models import Instructor
from ..member.models import Member


class Workout(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False,
        db_index=True, )
    workout_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)


class WorkoutPlan(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        editable=False,
        db_index=True, )
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    work_out_date_time = models.DateTimeField(default=datetime.now())
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
