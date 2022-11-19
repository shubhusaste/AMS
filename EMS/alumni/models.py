from django.db import models

# Create your models here.

class EventGallary(models.Model):
    event_name= models.CharField(max_length=100)
    event_date= models.DateField()
    event_img = models.ImageField(null=True,blank=True, upload_to='pics_event/')
    event_desc = models.TextField()


    def __str__(self):
        return self.event_name

class AlumniInfo(models.Model):
    # sr_no = models.AutoField()
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    address=models.TextField()
    about_alumni=models.TextField()
    mob1=models.IntegerField()
    mob2=models.IntegerField()
    email=models.TextField()
    passout=models.CharField(max_length=25)
    branch=models.CharField(max_length=25)
    prn_no=models.CharField(max_length=25)
    job_status=models.CharField(max_length=20)
    org_name=models.CharField(max_length=20)

    def __str__(self):
        return self.first_name+" "+self.last_name

