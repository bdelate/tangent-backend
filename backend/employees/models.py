from django.db import models
from django.contrib.auth.models import AbstractUser


class Employee(AbstractUser):
    """
    Employee which inherits all default attributes from Django's builtin User
    """
    RANK_TYPES = (
        ('Management', 'Management'),
        ('Senior', 'Senior'),
        ('Intermediate', 'Intermediate'),
        ('Junior', 'Junior')
    )
    rank = models.CharField(max_length=12, null=True, choices=RANK_TYPES)
    cell_phone = models.CharField(max_length=10, null=True)
    salary = models.FloatField(null=True)

    class Meta:
        ordering = ['first_name']

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
