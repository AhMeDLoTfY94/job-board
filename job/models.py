from django.db import models

class Category(models.Model):
          name=models.CharField(max_length=25)
          
          def __str__(self):
                    return self.name
          


def image_upload(instance,filename):
          imagename,extension=filename.split(".")
          return "jobs/%s/%s.%s"%(instance.id,instance.id,extension)

class Job(models.Model):
          JOB_TYPE=[
                    ('Full Time','Full Time'),
                    ("Part Time","Part Time"),
          ]
          title=models.CharField(max_length=100)
          job_type=models.CharField(max_length=30,choices=JOB_TYPE)
          description=models.TextField(max_length=1000)
          puplished_at=models.DateTimeField(auto_now=True)
          vecancy=models.IntegerField(default=1)
          salary=models.IntegerField(default=0)
          experience=models.IntegerField(default=1)
          category=models.ForeignKey(Category,on_delete=models.CASCADE)
          image=models.ImageField(upload_to=image_upload)
          
          def __str__(self):
                    return self.title