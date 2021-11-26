from django.forms import ModelForm
from .models import Student

# Add islemi icin form olusturmak gerekir , bu yüzden form olusturduk.
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"