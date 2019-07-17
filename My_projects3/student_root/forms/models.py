from django.db import models
from django.forms import ModelForm

# Create your models here.
class Student1(models.Model):
    Students_id= models.CharField(max_length=10,null=True)
    Students_name= models.CharField(max_length=100,null=True)
    email= models.EmailField()

    #class Meta:
     #   db_table = 'student2'
    def __unicode__(self):
        return u'%d %s %s' % (self.Students_id, self.Students_name, self.email)

