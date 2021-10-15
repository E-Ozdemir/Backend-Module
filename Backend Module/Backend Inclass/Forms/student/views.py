from django.shortcuts import render,redirect
from .forms import StudentForm
from django.contrib import messages
from student.models import Student

def index(request):
    return render(request, 'student/index.html')

def student_page(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        
        
    form = StudentForm()
    context = {
        	'form': form
    	}
    
    return render(request,'student/student.html',context)