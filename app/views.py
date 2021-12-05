from django.shortcuts import render,redirect
from .forms import StudentForm
from django.contrib import messages

def index(request):
    return render(request, 'app/index.html')

def student_page(request):
    form = StudentForm() 
    if request.method =="POST":
       form = StudentForm(request.POST, request.FILES)
       if form.is_valid(): 
           form.save()
           messages.success(request,"başarıyla güncellenmiştir")         
           return redirect('student')
    
           
    context = {
        'form': form
    }
    return render(request,'app/student.html', context)
    
