from django.db import models

# Create your models here.

class Creator(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    creator = models.OneToOneField(Creator, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
    
class Frameworks(models.Model):
    name= models.CharField(max_length=40)
    dil = models.ForeignKey(Language, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Programmer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    frameworks = models.ManyToManyField(Frameworks)
    
    def __str__(self):
        return self.first_name