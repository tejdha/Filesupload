from django.db import models

# Create your models here.
import datetime
class info(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40, blank=True)
    tech = models.CharField(max_length=30)
    email = models.EmailField(default=None,unique=True)
    photo = models.FileField()
    date = models.DateField(default=datetime.date.today())

    class Meta :
        db_table = 'profileinfo'