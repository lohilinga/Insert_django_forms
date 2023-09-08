from django.shortcuts import render


# Create your views here.
from app.forms import *
from app.models import *

def insert_student(request):
    SFEO=Student_form()
    d={'SFEO':SFEO}
    if request.method == 'POST':
        SFDO=Student_form(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sid=SFDO.cleaned_data['Sid']
            Semail=SFDO.cleaned_data['Semail']
            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Semail=Semail)[0]
            SO.save()
            QSSO=Student.objects.all()
            d1={'QSSO':QSSO}

            return render(request,'submitdata.html',d1)
        
    return render(request,'insert_student.html',d)



 
 



