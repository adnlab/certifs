from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    class Meta:
        db_table = 'cert"."person'