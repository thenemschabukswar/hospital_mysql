from django.db import models
from django.core.validators import  MinValueValidator

STATUS_CHOICES = (
    ('Primary', 'Primary Checkup'),
    ('Admitted', 'Admitted'),
    ('Discharged', 'Discharged')
)
'''
class rooms(models.Model):
    single = models.IntegerField(default=1)
    double = models.IntegerField(default=1)
    triple = models.IntegerField(default = 1)
'''
# Create your models here.

class hosp(models.Model):
    r_id = models.AutoField(primary_key=True)
    single = models.IntegerField(default=1, blank=True)
    double = models.IntegerField(default=1, blank=True)
    triple = models.IntegerField(default=1, blank=True, validators=[MinValueValidator(0)])
    def __str__(self):
        return str(self.id)


class patient(models.Model):
    p_id = models.AutoField(primary_key = True)
    room = models.ForeignKey(hosp, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length = 40)
    hospital = models.CharField(max_length = 30)
    disease = models.CharField(max_length=40)
    status = models.CharField(max_length = 20, choices=STATUS_CHOICES, default='Primary')
    allergies = models.CharField(max_length=50, blank=True)
    remarks = models.CharField(max_length=500, blank=True)
    def __str__(self):
        return self.name + ' - ' + self.status

