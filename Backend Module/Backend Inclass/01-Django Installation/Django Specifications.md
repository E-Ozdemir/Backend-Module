-A free and open source web framework.
-Thousands of additional packages

Model View Template:
-Model work with data
>>>>





-Views will work with logic
-template  will work with layouts.

Models: Database'i kullanacagimiz tablolarin olusturuldugu yer.
-Djangoda sql yerine orm kullanacagiz.


__init__.py  :>>>> O projenin bir package oldugunu pythona söylemenin yolu!
wsgi.py ve asgi.py  to serve your project in web servers.

Project ve App in farki;
-Project appdan olusur. app lar birlesip projecti olusturur. Mesela projeninn auth kismi bir app dir. 









<<<<<Installation>>>>>
1- py -m venv clenv(clenv yerine istedigimiz ismi girebiliriz mesela env)
2- Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted (activate etmezse hata verirse)
3- .\clenv\Scripts\activate
4- pip install django
- python -m pip install --upgrade pip
<!-- 5- pip install python-decouple (env dosyasi icin) -->
5- django-admin startproject projectname
7- cd projectname(oncesinde proje file in icerisine cd yapiyoruz, manage.py directorysinde olmaliyiz)
8- py manage.py startapp appname
   INSTALLED_APPS a projeyi ekle! >>> settings.py icerisine
9- py manage.py runserver

10- py manage.py migrate (database kurar)
11- py manage.py createsuperuser???????
12- py manage.py makemigrations (Form ve database degisiklikleri)
13- py manage.py migrate (Form ve database degisiklikleri)
14- py manage.py shell
--------------------------------------------
