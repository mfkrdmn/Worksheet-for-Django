from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = "profile_images", null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Lesson(models.Model):
    lesson_name = models.CharField(max_length=50)
    lesson_teacher = models.ManyToManyField(Teacher)
    #Bir hoca birden fazla ders verebilir, aynı zamanda bir ders birden fazla hoca tarafından verilebilir

    def __str__(self):
        return self.lesson_name
        # return f"{self.lesson_name}-Teacher({self.lesson_teacher.name})"
