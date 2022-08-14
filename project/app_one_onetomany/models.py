from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=50)
    lesson_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lesson_name}-Teacher({self.lesson_teacher})"