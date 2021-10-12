1- python --version
2- pip --version
3- py -m venv clenv yada env 
4- Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
5- .\clenv\Scripts\activate
6- pip install django (py -m pip install --upgrade pip)
7- django-admin startproject projectname
 >> cd projectname(Oncesinde proje file'in icerisine cd yapiyoruz, manage.py directory'sinde olmaliyiz)
 8- py manage.py startapp fscohort
   INSTALLED_APPS a projeyi ekle! >>> settings.py icerisine
9- py manage.py runserver
10- py manage.py createsuperuser #>>to login admin panel! Burda hata verebilir migrate hatasi verebilir , bu durumda # py manage.py migrate # komutunu calistir. Sonra tekrardan createsuperuser ...
11- py manage.py makemigrations (Form ve database degisiklikleri)
12- py manage.py migrate (Form ve database degisiklikleri)
13- py manage.py shell

# from fscohort.models import Student
s1 = Student(first_name="Henry", last_name="Forester", number=123)
s1.save()

# hem olusturup hem kaydetmek icin >>>
s5 = Student.objects.create(first_name="Adam", last_name="Flyer", number=789) 