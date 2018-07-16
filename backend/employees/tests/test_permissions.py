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

    def test_manager_can_view_another_employee(self):
        """
        Managers must be able to view other employee instances
        """
        manager, _ = employee_models.Employee.objects.get_or_create(
            username='john',
            password='p@ssw0rd',
            rank='Management'
        )
        user, _ = employee_models.Employee.objects.get_or_create(
            username='bob',
            password='p@ssw0rd',
            rank='Intermediate'
        )
        self.client.force_authenticate(manager)
        url = reverse('employees:employee-detail', args=[user.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], user.id)

    def test_manager_can_update_another_employee(self):
        """
        Managers must be able to update other employee instances
        """
        manager, _ = employee_models.Employee.objects.get_or_create(
            username='john',
            password='p@ssw0rd',
            rank='Management'
        )
        user, _ = employee_models.Employee.objects.get_or_create(
            username='bob',
            password='p@ssw0rd',
            rank='Intermediate'
        )
        self.client.force_authenticate(manager)
        url = reverse('employees:employee-detail', args=[user.id])
        data = {
            'rank': 'Senior'
        }
        response = self.client.patch(url, data, format='json')
        user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(user.rank, 'Senior')

    def test_non_manager_cannot_view_another_employee(self):
        """
        Non managers must not be able to view other employee instances
        """
        user1, _ = employee_models.Employee.objects.get_or_create(
            username='john',
            password='p@ssw0rd',
            rank='Senior'
        )
        user2, _ = employee_models.Employee.objects.get_or_create(
            username='bob',
            password='p@ssw0rd',
            rank='Intermediate'
        )
        self.client.force_authenticate(user1)
        url = reverse('employees:employee-detail', args=[user2.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_manager_cannot_update_another_employee(self):
        """
        Non managers must not be able to update other employee instances
        """
        user1, _ = employee_models.Employee.objects.get_or_create(
            username='john',
            password='p@ssw0rd',
            rank='Senior'
        )
        user2, _ = employee_models.Employee.objects.get_or_create(
            username='bob',
            password='p@ssw0rd',
            rank='Intermediate'
        )
        self.client.force_authenticate(user1)
        url = reverse('employees:employee-detail', args=[user2.id])
        data = {
            'rank': 'Senior'
        }
        response = self.client.patch(url, data, format='json')
        user2.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(user2.rank, 'Intermediate')
