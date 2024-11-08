from django.shortcuts import render
from .models import AssignTravel,Division,Employee,NatureOfTravel,Office,Position,TravelOrder

# Create your views here.
def main(request):
    return render(request,'myapp/main.html')

def division(request):
    division = Division.objects.all()

    if request.method == "POST":
        if "div_add" in request.POST:    
            division_name = request.POST.get("division_name")
            Division.objects.create(
                division_name = division_name
            )
    
        elif "div_update" in request.POST:
            id = request.POST.get("id")
            division_name = request.POST.get("division_name")

            update_division = Division.objects.get(id=id)
            update_division.division_name = division_name
            update_division.save()
        
        elif "div_delete" in request.POST:
            id = request.POST.get("id")
            Division.objects.get(id=id).delete()

    context = {"division_list":division}
    return render(request,'myapp/division.html',context)

def office(request):
    division = Division.objects.all()
    office = Office.objects.all()

    if request.method == "POST":
        if "office_add" in request.POST:
            office_name = request.POST.get("office_name")
            division_id = request.POST.get("division_name")
            Office.objects.create(
                office_name = office_name,
                division_id = division_id
            )

        elif "office_update" in request.POST:
            id = request.POST.get("id")
            office_name = request.POST.get("office_name")
            division_id = request.POST.get("division_name")

            update_office = Office.objects.get(id=id)
            update_office.office_name = office_name
            update_office.division_id = division_id
            update_office.save()

        elif "office_delete" in request.POST:
            id = request.POST.get("id")
            Office.objects.get(id=id).delete()
    
    context = {"division_list":division,"office_list":office}
    return render(request,'myapp/office.html',context)

def position(request):
    position = Position.objects.all()

    if request.method == "POST":
        if "position_add" in request.POST:
            position_name = request.POST.get("position_name")
            Position.objects.create(
                position_name = position_name
            )
        
        elif "position_update" in request.POST:
            id = request.POST.get("id")
            position_name = request.POST.get("position_name")

            update_position = Position.objects.get(id=id)
            update_position.position_name = position_name
            update_position.save()

        elif "position_delete" in request.POST:
            id = request.POST.get("id")
            Position.objects.get(id=id).delete()
    
    context = {"position_list":position}
    return render(request,'myapp/position.html',context)

def employee(request):
    position = Position.objects.all()
    division = Division.objects.all()
    office = Office.objects.all()
    employee = Employee.objects.all()

    if request.method == "POST":
        if "employee_add" in request.POST:
            employee_name = request.POST.get("employee_name")
            position_id = request.POST.get("position_name")
            office_id = request.POST.get("office_name")
            Employee.objects.create(
                employee_name = employee_name,
                position_id = position_id,
                office_id = office_id
            )

        elif "employee_update" in request.POST:
            id = request.POST.get("id")
            employee_name = request.POST.get("employee_name")
            position_id = request.POST.get("position_name")
            office_id = request.POST.get("office_name")

            update_employee = Employee.objects.get(id=id)
            update_employee.employee_name = employee_name
            update_employee.position_id = position_id
            update_employee.office_id = office_id
            update_employee.save()

        elif "employee_delete" in request.POST:
            id = request.POST.get("id")
            Employee.objects.get(id=id).delete()

    context = {"position_list":position,"division_list":division,"office_list":office,"employee_list":employee}
    return render(request,'myapp/employee.html',context)

def nature_travel(request):
    nature_travel = NatureOfTravel.objects.all()

    if request.method == "POST":
        if "nature_travel_add" in request.POST:
            nature_travel_name = request.POST.get("nature_travel_name")
            NatureOfTravel.objects.create(
                nature_travel_name = nature_travel_name
            )
        
        elif "nature_travel_update" in request.POST:
            id = request.POST.get("id")
            nature_travel_name = request.POST.get("nature_travel_name")

            update_nature_travel = NatureOfTravel.objects.get(id=id)
            update_nature_travel.nature_travel_name = nature_travel_name
            update_nature_travel.save()

        elif "nature_travel_delete" in request.POST:
            id = request.POST.get("id")
            NatureOfTravel.objects.get(id=id).delete()

    context = {"nature_travel_list":nature_travel}
    return render(request,'myapp/travelnature.html',context)

def travel(request):
    travel = TravelOrder.objects.all()
    nature_travel = NatureOfTravel.objects.all()

    if request.method == "POST":
        if "travel_add" in request.POST:
            travel_number = request.POST.get("travel_number")
            destination = request.POST.get("destination")
            date_start = request.POST.get("date_start")
            date_end = request.POST.get("date_end")
            purpose = request.POST.get("purpose")
            natureoftavel_id = request.POST.get("nature_travel_name")
            file = request.FILES.get("file")
            TravelOrder.objects.create(
                travel_number = travel_number,
                destination = destination,
                date_start = date_start,
                date_end = date_end,
                purpose = purpose,
                natureoftavel_id = natureoftavel_id,
                file = file
            )
        
        elif "travel_update" in request.POST:
            id = request.POST.get("id")
            travel_number = request.POST.get("travel_number")
            destination = request.POST.get("destination")
            date_start = request.POST.get("date_start")
            date_end = request.POST.get("date_end")
            purpose = request.POST.get("purpose")
            natureoftavel_id = request.POST.get("nature_travel_name")
            file = request.FILES.get("file")

            update_travel = TravelOrder.objects.get(id=id)
            update_travel.travel_number = travel_number
            update_travel.destination = destination
            update_travel.date_start = date_start
            update_travel.date_end = date_end
            update_travel.purpose = purpose
            update_travel.natureoftavel_id = natureoftavel_id
            update_travel.file = file
            update_travel.save()

        elif "travel_delete" in request.POST:
            id = request.POST.get("id")
            TravelOrder.objects.get(id=id).delete()    

    context = {"travel_list":travel,"nature_travel_list":nature_travel}
    return render(request,'myapp/travelorder.html',context)

def assigntravel(request):
    employee = Employee.objects.all()
    travel = TravelOrder.objects.all()
    assign_travel = AssignTravel.objects.all()

    if request.method == "POST":
        if "assign_add" in request.POST:
            employee_id = request.POST.get("employee_name")
            travelorder_id = request.POST.get("travel_number")
            AssignTravel.objects.create(
                employee_id = employee_id,
                travelorder_id = travelorder_id
            )

    context = {"employee_list":employee,"travel_list":travel,"assign_travel_list":assign_travel}
    return render(request,'myapp/assigntravel.html',context)

def test(request):
    return render(request,'myapp/test.html')