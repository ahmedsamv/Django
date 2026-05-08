from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.IntegerField(primary_key=True ,verbose_name="ID", help_text="course id")
    name = models.CharField(max_length=100, verbose_name="Course Name", help_text="course name")

    def __str__(self):
        return self.name
    

