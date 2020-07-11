from django.db import models

# Create your models here.
class Test(models.Model):
    title = models.CharField('title', max_length=100)
    content = models.TextField('content')
    url = models.URLField('url', unique=True)
 
    def __str__(self):
        return self.title

class UniInfo(models.Model):
    servey_year = models.CharField('year', max_length=40, null=True)
    uniclass = models.CharField('uni_class', max_length=100, null=True)
    estclass = models.CharField('est_class', max_length=20, null=True)
    province = models.CharField('province', max_length=40, null=True)
    city = models.CharField('city', max_length=3, null=True)
    university = models.CharField('uni_name', max_length=50, null=True)
    campus_class = models.CharField('cam_class', max_length=150, null=True)
    campus_location = models.CharField('cam_location', max_length=200, null=True)
    depart_type = models.CharField('depart_type', max_length=50, null=True)
    time = models.CharField('time', max_length=10, null=True)
    depart_state = models.CharField('depart_state',max_length=100, null=True)
    standard_max_field = models.CharField('max_field', max_length=30, null=True)
    standard_mid_field = models.CharField('mid_field', max_length=30, null=True)
    standard_min_field = models.CharField('min_field', max_length=30, null=True)
    uni_field = models.CharField('uni_field', max_length=30, null=True)
    department = models.CharField('department_name', max_length=50, null=True)
    uni_year = models.CharField('uni_year', max_length=20, null=True)
#    homepage = models.URLField('homepage', unique=True)
    uni_code = models.IntegerField('uni_code', null=True)
    def __str__(self):
        return self.university

# class DepartInfo(models.Model):
#     university = models.CharField('uni_name', max_length=50, null=True)
#     department = models.CharField('department_name', max_length=50, null=True)
#     standard_min_field = models.CharField('min_field', max_length=20, null=True)    
#     depart_state = models.CharField('depart_state',max_length=10, null=True)
#     uni_year = models.CharField('uni_year', max_length=2, null=True)
    
class StandardInfo(models.Model):
    list_max = models.CharField('max_field', max_length=20, null=True)
    standard_max_field = models.CharField('max_field', max_length=20, null=True)
    standard_mid_field = models.CharField('mid_field', max_length=20, null=True)
    standard_min_field = models.CharField('min_field', max_length=20, null=True)
       