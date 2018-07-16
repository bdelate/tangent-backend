from employees import models as employee_models
from rest_framework import serializers


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='employees:employee-detail'
    )

    class Meta:
        model = employee_models.Employee
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'is_staff',
            'is_superuser',
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

    def create(self, validated_data: dict) -> employee_models.Employee:
        """
        Create an employee and encode password using set_password

        Args:
            validated_data: validated serializer data

        Returns:
            Employee instance
        """
        password = validated_data.pop('password')
        user_instance = employee_models.Employee(**validated_data)
        user_instance.set_password(password)
        user_instance.save()
        return user_instance

    def update(self,
               instance: employee_models.Employee,
               validated_data: dict) -> employee_models.Employee:
        """
        Update an employee and encode updated password if present

        Args:
            instance: existing employee instance
            validated_data: validated serializer data

        Returns:
            the updated employee instance
        """
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)

        for field, value in validated_data.items():
            setattr(instance, field, value)

        instance.save()
        return instance


class EmployeeSerializer(ManagerSerializer):
    """Employees inherit from Managers but cannot edit all fields"""
    class Meta(ManagerSerializer.Meta):
        read_only_fields = (
            'rank',
            'salary',
            'is_active',
            'is_staff',
            'is_superuser'
        )
