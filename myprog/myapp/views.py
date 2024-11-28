from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.db.models import Q
from django.contrib import messages

from .models import AssignTravel,Division,Employee,NatureOfTravel,Office,Position,TravelOrder

# Create your views here.
@login_required
def main(request):
    return render(request,'myapp/main.html')
@login_required
def division(request):
    division = Division.objects.all()

    if request.method == "POST":
        try:
            if "div_add" in request.POST:    
                division_name = request.POST.get("division_name")
                Division.objects.create(
                    division_name = division_name
                )
                messages.success(request,"Division added successfully")
        
            elif "div_update" in request.POST:
                id = request.POST.get("id")
                division_name = request.POST.get("division_name")

                update_division = Division.objects.get(id=id)
                update_division.division_name = division_name
                update_division.save()

                messages.success(request,"Division updated successfully")

            elif "div_delete" in request.POST:
                id = request.POST.get("id")
                Division.objects.get(id=id).delete()

                messages.success(request,"Division deleted successfully")
        except Exception as e:
            messages.error(request,f"An error occured: {str(e)}")

    context = {"division_list":division}
    return render(request,'myapp/division.html',context)

@login_required
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

            messages.success(request,"Office added successfully")

        elif "office_update" in request.POST:
            id = request.POST.get("id")
            office_name = request.POST.get("office_name")
            division_id = request.POST.get("division_name")

            update_office = Office.objects.get(id=id)
            update_office.office_name = office_name
            update_office.division_id = division_id
            update_office.save()

            messages.success(request,"Office updated successfully")

        elif "office_delete" in request.POST:
            id = request.POST.get("id")
            Office.objects.get(id=id).delete()

            messages.success(request,"Office deleted successfully")
    
    context = {"division_list":division,"office_list":office}
    return render(request,'myapp/office.html',context)

@login_required
def position(request):
    position = Position.objects.all()

    if request.method == "POST":
        if "position_add" in request.POST:
            position_name = request.POST.get("position_name")
            Position.objects.create(
                position_name = position_name
            )

            messages.success(request,"Position added successfully")
        
        elif "position_update" in request.POST:
            id = request.POST.get("id")
            position_name = request.POST.get("position_name")

            update_position = Position.objects.get(id=id)
            update_position.position_name = position_name
            update_position.save()

            messages.success(request,"Position updated successfully")

        elif "position_delete" in request.POST:
            id = request.POST.get("id")
            Position.objects.get(id=id).delete()

            messages.success(request,"Position deleted successfully")
    
    context = {"position_list":position}
    return render(request,'myapp/position.html',context)

@login_required
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

            messages.success(request,"Employee added successfully")

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

            messages.success(request,"Employee updated successfully")

        elif "employee_delete" in request.POST:
            id = request.POST.get("id")
            Employee.objects.get(id=id).delete()

            messages.success(request,"Employee deleted successfully")

    context = {"position_list":position,"division_list":division,"office_list":office,"employee_list":employee}
    return render(request,'myapp/employee.html',context)

@login_required
def training_list(request):
    position = Position.objects.all()
    division = Division.objects.all()
    office = Office.objects.all()
    employee = Employee.objects.all()
    query = ""

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

        elif "employee_search" in request.POST:
            query = request.POST.get("searchquery")
            employee = Employee.objects.filter(Q(employee_name__icontains=query) | Q(position__position_name__icontains=query) | Q(office__office_name__icontains=query))


        
    context = {"position_list":position,"division_list":division,"office_list":office,"employee_list":employee,"query":query}
    return render(request,'myapp/training_list.html',context)

@login_required
def nature_travel(request):
    nature_travel = NatureOfTravel.objects.all()

    if request.method == "POST":
        if "nature_travel_add" in request.POST:
            nature_travel_name = request.POST.get("nature_travel_name")
            NatureOfTravel.objects.create(
                nature_travel_name = nature_travel_name
            )

            messages.success(request,"Nature of Travel added successfully")
        
        elif "nature_travel_update" in request.POST:
            id = request.POST.get("id")
            nature_travel_name = request.POST.get("nature_travel_name")

            update_nature_travel = NatureOfTravel.objects.get(id=id)
            update_nature_travel.nature_travel_name = nature_travel_name
            update_nature_travel.save()

            messages.success(request,"Nature of Travel updated successfully")

        elif "nature_travel_delete" in request.POST:
            id = request.POST.get("id")
            NatureOfTravel.objects.get(id=id).delete()

            messages.success(request,"Nature of Travel deleted successfully")

    context = {"nature_travel_list":nature_travel}
    return render(request,'myapp/travelnature.html',context)

@login_required
def travel(request):
    travel = TravelOrder.objects.all()
    nature_travel = NatureOfTravel.objects.all()
    query = ""
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

            messages.success(request,"Travel Order added successfully")
        
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

            messages.success(request,"Travel Order updated successfully")

        elif "travel_delete" in request.POST:
            id = request.POST.get("id")
            TravelOrder.objects.get(id=id).delete()

            messages.success(request,"Travel Order deleted successfully")
        
        elif "travel_search" in request.POST:
            query = request.POST.get("searchquery")
            travel = TravelOrder.objects.filter(Q(travel_number__icontains=query) | Q(purpose__icontains=query) | Q(destination__icontains=query) | Q(date_start__icontains=query) | Q(date_end__icontains=query) | Q(natureoftavel__nature_travel_name__icontains=query))

    context = {"travel_list":travel,"nature_travel_list":nature_travel,"query":query}
    return render(request,'myapp/travelorder.html',context)

@login_required
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

            messages.success(request,"Employee Travel added successfully")

        elif "assign_update" in request.POST:
            id = request.POST.get("id")
            employee_id = request.POST.get("employee_name")
            travelorder_id = request.POST.get("travel_number")

            update_assign_travel = AssignTravel.objects.get(id=id)
            update_assign_travel.employee_id = employee_id
            update_assign_travel.travelorder_id = travelorder_id
            update_assign_travel.save()

            messages.success(request,"Employee Travel updated successfully")
        
        elif "assign_delete" in request.POST:
            id = request.POST.get("id")
            AssignTravel.objects.get(id=id).delete()  

            messages.success(request,"Employee Travel deleted successfully")


    context = {"employee_list":employee,"travel_list":travel,"assign_travel_list":assign_travel}
    return render(request,'myapp/assigntravel.html',context)

def test(request):
    return render(request,'myapp/test.html')

@login_required
def view_trainings(request, employee_id):
    # Fetch trainings for the given employee_id from the database
    trainings = AssignTravel.objects.filter(employee_id=employee_id)
    employee = get_object_or_404(Employee, id=employee_id)
    context = {'trainings': trainings, 'employee_id': employee_id,'employee':employee}
    return render(request, 'myapp/trainings.html', context)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')  # Replace 'home' with your target URL
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    
    return render(request, 'myapp/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')