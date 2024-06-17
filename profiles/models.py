from django.db import models

# Create your models here.
class Portfolio(models.Model):
    
    name=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="profile_pic/")
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=100)
    marital_status=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    skills=models.TextField()
    address=models.TextField()
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=100)
    about=models.TextField()
    experience=models.TextField()
    education=models.TextField()
    certification=models.TextField()
    project_title=models.CharField(max_length=100)
    project_description=models.TextField()
    project_img=models.ImageField(upload_to="project_pics/")
    project_link=models.CharField(max_length=100)
    def __str__(self):
        return self.name