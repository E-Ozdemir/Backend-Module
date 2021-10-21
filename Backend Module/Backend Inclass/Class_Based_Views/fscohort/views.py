from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
from django.views.generic import TemplateView,ListView, DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy



# Create your views here.

def home(request):
    return render(request, "fscohort/home.html")

class HomeView(TemplateView):
    template_name = 'fscohort/home.html'


def student_list(request):
    
    students = Student.objects.all()
    
    context = {
        "students":students
    }
    
    return render(request, "fscohort/student_list.html", context)

class StudentListView(ListView):
    model = Student
    # default name app/modelname_List.html
    # template_name = 'fscohort/student_list.html'
    context_object_name = 'students' #default name object_list
    paginate_by = 5

def student_add(request):
    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("list")
            
    
    context = {
       
       "form":form     
    }
    
    return render(request, "fscohort/student_add.html", context)

class StudentCreateView(CreateView):
    model = Student  
    form_class = StudentForm
    template_name = 'fscohort/student_add.html' # default name 
    success_url =  '/student_list/'   #reverse_lazy('list')
    



def student_detail(request,id):
    student = Student.objects.get(id=id)
    context = {
        "student":student
    }
    
    return render(request, "fscohort/student_detail.html", context)

class StudentDetailView(DetailView):
    model = Student
    pk_url_kwarg = 'id'
    
def student_update(request, id):
    
    student = Student.objects.get(id=id)
    
    form = StudentForm(instance=student)
    
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
       
    context= {
        
        "student":student,
        "form":form 
    }
    
    return render(request, "fscohort/student_update.html", context)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_update.html" #defaul name app/modelname_form.html
    success_url = reverse_lazy('list') # fonksiyondaki redirect islemini class yapisinda böyle yapiyoruz
    

def student_delete(request, id):
    
    student = Student.objects.get(id=id)
   
    if request.method == "POST":

    
        student.delete()
        return redirect("list")
    
    context= {
        "student":student
    }
    return render(request, "fscohort/student_delete.html",context)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = "fscohort/student_delete.html" #default name app/modelname_confirm_delete.html
    success_url =  reverse_lazy('list')