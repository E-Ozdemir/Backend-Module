from django.shortcuts import redirect, render
from .forms import StudentForm
from .models import Student

# Create your views here.

def home(request):
    return render(request, "fscohort/home.html")

#------------------
def student_list(request):
    
    students = Student.objects.all()
    
    # >>>>> students verisini template göndermek icin bunu context icerisine koymak gerekir!!!!
    context = {
        "students":students
    }
    
    return render(request, "fscohort/student_list.html", context)
#---------------------------------
def student_add(request):
    form = StudentForm()
    
    #Formdan gelen veriyi kontrol edilmesi gerekir!
    if request.method == "POST":
        form = StudentForm(request.POST)# request.POST > bize gelen datayi al ilgili yerlere koy!
        # , request.FILES 
        if form.is_valid():
            form.save()
            # return redirect("list")
            
    
    context = {
       
       "form":form     
    }
    
    return render(request, "fscohort/student_add.html", context)

#------------------------

# DETAIL, UPDATE VE DELETE YUKARIDAKI IKI FONKSIYONDAN FARKLI
#Fark; db de olan veriyi cagircaz,istek atcaz, istek atarken primary key ile istek atacagiz!

def student_detail(request,pk):
    
    student = Student.objects.get(id=pk) # id ye göre git ve ilgili veriyi get et, AL !
    context = {
        "student":student
    }
    
    return render(request, "fscohort/student_detail.html", context)

#------------------------------------------
    
def student_update(request, pk):
    
    # Creating a form to change an existing article.
    student = Student.objects.get(id=pk) #Veriyi id ye göre cek!
    form = StudentForm(instance=student) #yukarida cektigimiz veriyi instance'a esitliyoruz!BU sayede student verilerini form daki kutucuklara yerlestiriyor!
    
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("list")
       
    context= {
        
        "student":student,
        "form":form 
    }
    
    return render(request, "fscohort/student_update.html", context)

def student_delete(request, id):
    
    student = Student.objects.get(id=id)
   
    if request.method == "POST":

    
        student.delete()
        return redirect("list")
    
    context= {
        "student":student
    }
    return render(request, "fscohort/student_delete.html",context)