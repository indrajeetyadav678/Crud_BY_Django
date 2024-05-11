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
    emailmatch=EmplayeeModel.objects.filter(Email=email)
    if emailmatch:
        msg="Data already exist"
        return redirect('/')
    else:
        EmplayeeModel.objects.create(
            Name= name,
            Email=email,
            Number=number,
            Position=position,
            Sallary=sallary
            )
        msg="Your Data Inserted Successfully"
        return redirect('/')
    
def display(request):
    all_data=EmplayeeModel.objects.all()
    print(all_data)
    return render(request,'display.html', {'key2':all_data})


def edit(request, pk):
    try:
        Data=EmplayeeModel.objects.get(id=pk)
    except:
        print(Data)
        print(Data.id)
        print(Data.Sallary)
        return redirect('display')
    return render(request, 'updateform.html',{'data':Data})


def update(request, pk):
    employee=EmplayeeModel.objects.get(id=pk)
    if request.method == 'POST':
        employee.Name = request.POST.get('Name')
        employee.Email = request.POST.get('Email')
        employee.Number = request.POST.get('Number')
        employee.Position = request.POST.get('Position')
        employee.Sallary = request.POST.get('Sallary')
        employee.save()
        msg = "Data updated successfully"
        return redirect('display') 
     # Redirect to display page after updating
    
    return render(request, 'updateform.html', {'employee': employee})
    

def delet(request, pk):
    EMP_data=EmplayeeModel.objects.get(id=pk)
    EMP_data.delete()
    msg="Date deleted "
    # return render(request,'display.html',{'key3':msg})
    return redirect('display')