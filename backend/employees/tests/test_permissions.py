from django.urls import reverse
from employees import models as employee_models
from rest_framework import status
from rest_framework.test import APITestCase


class EmployeePermissionTests(APITestCase):

    def test_manager_can_list(self):
        """
        Managers must be able to request a list of all employees
        """
        user, _ = employee_models.Employee.objects.get_or_create(
            username='john',
            password='p@ssw0rd',
            rank='Management'
        )
        self.client.force_authenticate(user)
        url = reverse('employees:employee-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_non_manager_cannot_list(self):
        """
        Non managers must not be able to request a list of all employees
        """
        user, _ = employee_models.Employee.objects.get_or_create(
            username='john',
            password='p@ssw0rd',
            rank='Senior'
        )
        self.client.force_authenticate(user)
        url = reverse('employees:employee-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
