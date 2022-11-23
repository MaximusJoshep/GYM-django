# Generated by Django 4.1.3 on 2022-11-23 02:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=30)),
                ('membership_period', models.CharField(max_length=30)),
                ('membership_amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('member_id_nro', models.CharField(max_length=15)),
                ('member_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=9)),
                ('email', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=10)),
                ('joining_date', models.DateField()),
                ('end_of_membership_date', models.DateField()),
                ('membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.membershiptype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]