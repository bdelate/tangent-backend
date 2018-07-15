from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    RANK_TYPES = (
        ('Management', 'Management'),
        ('Senior', 'Senior'),
        ('Intermediate', 'Intermediate'),
        ('Junior', 'Junior')
    )
    rank = models.CharField(max_length=12, null=True, choices=RANK_TYPES)
    cell_phone = models.CharField(max_length=10, null=True)
    salary = models.FloatField(null=True)
