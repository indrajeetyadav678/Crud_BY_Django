from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import*

# Create your views here.
def home(request):
    Context={}
    Context['form']=Emplayeeform
    return render(request, 'home.html', Context)

def insert(request):
    name=request.POST['Name']
    email=request.POST['Email']
    number=request.POST['Number']
    position=request.POST['Position']
    sallary=request.POST['Sallary']
    emailmatch=EmplayeeModel.objects.filter(Name=name)
    if emailmatch:
        msg="Data already exist"
        return redirect('/', {'key1':msg})
    else:
        EmplayeeModel.objects.create(
            Name= name,
            Email=email,
            Number=number,
            Position=position,
            Sallary=sallary
            )
        msg="Your Data Inserted Successfully"
        return redirect('/', {'key1':msg})
    
def display(request):
    all_data=EmplayeeModel.objects.all()
    print(all_data)
    return render(request,'display.html', {'key2':all_data})


def edit(request, pk):
    data=EmplayeeModel.objects.filter(id=pk)
    Name=request.POST.get(Name)
    Email=request.POST.get(Email)
    Number=request.POST.get(Number)
    Position=request.POST.get(Position)
    Sallary=request.POST.get(Sallary)