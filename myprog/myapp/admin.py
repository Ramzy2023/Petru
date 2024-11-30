from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Division, Office, Position,Employee

# Create a resource class for Division
class DivisionResource(resources.ModelResource):
    class Meta:
        model = Division
        fields = ('id', 'division_name')  # Specify the fields you want to import/export

# Create a resource class for Office
class OfficeResource(resources.ModelResource):
    class Meta:
        model = Office
        fields = ('id', 'division', 'office_name')  # Include division relationship

class PositionResource(resources.ModelResource):
    class Meta:
        model = Position
        fields = ('id', 'position_name')

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        fields = ('id','employee_name','position','office')


# Register the admin class for Division
@admin.register(Division)
class DivisionAdmin(ImportExportModelAdmin):
    resource_class = DivisionResource
    list_display = ['id', 'division_name']

# Register the admin class for Office
@admin.register(Office)
class OfficeAdmin(ImportExportModelAdmin):
    resource_class = OfficeResource
    list_display = ['id', 'division', 'office_name']

@admin.register(Position)
class PositionAdmin(ImportExportModelAdmin):
    resource_class = PositionResource
    list_display = ['id','position_name']

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource
    list_display = ['id','employee_name','position','office']