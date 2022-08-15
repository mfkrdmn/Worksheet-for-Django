from django.db import models

# Create your models here.

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = "profile_images", null=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=50)
    lesson_teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    #Bir hoca sadece bir ders verebilir, bir derse iki hoca atanmak isterse hata verir

    def __str__(self):
        return f"{self.lesson_name}-Teacher({self.lesson_teacher})"