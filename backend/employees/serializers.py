from employees import models as employee_models
from rest_framework import serializers


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='employees:employee-detail')

    class Meta:
        model = employee_models.Employee
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'rank',
            'cell_phone',
            'salary',
            'url'
        )

        extra_kwargs = {
            'password': {'write_only': True,
                         'style': {'input_type': 'password'}}
        }
