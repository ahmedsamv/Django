from django.db import models
from course.models import Course

# Create your models here.
class Traniee(models.Model):
    id = models.IntegerField(primary_key=True ,verbose_name="ID", help_text="traniee id")
    name = models.CharField(max_length=100, verbose_name="Traniee Name", help_text="traniee name")
    email = models.EmailField(verbose_name="Traniee Email", help_text="traniee email")
    fees=models.DecimalField(decimal_places=2,max_digits=10)
    create_date=models.DateField(auto_now_add=True,verbose_name='Insert Date')
    update_date=models.DateTimeField(auto_now=True,verbose_name='Update Date')
    Traniee_image=models.ImageField(upload_to='trainee_cover',null=True, blank=True)
    Course=models.ForeignKey(Course,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name