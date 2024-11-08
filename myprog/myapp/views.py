from django.shortcuts import render
from .models import AssignTravel,Division,Employee,NatureOfTravel,Office,TravelOrder,Position

# Create your views here.
def main(request):
    return render(request,'myapp/main.html')

def division(request):
    division = Division.objects.all()

    if request.method == "POST":
        division_name = request.POST.get("division_name")
        Division.objects.create(
            division_name = division_name
        )
    
    context = {"division_list":division}
    return render(request,'myapp/division.html',context)

