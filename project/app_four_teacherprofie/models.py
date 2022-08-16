from django.db import models
# Create your models here.

class TeacherProfile(models.Model):
    name = models.CharField(max_length=50)
    lectures = models.CharField(max_length=50, null=True)
    picture = models.ImageField(upload_to = "profile_images", null=True)

    def __str__(self):
        return self.name

class Lecture(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
