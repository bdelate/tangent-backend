from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    """
    Ensure Employee model is included with User details within Django admin
    """

    list_display = ('username', 'first_name', 'last_name', 'rank')

    class Meta:
        model = Employee


admin.site.register(Employee, EmployeeAdmin)
