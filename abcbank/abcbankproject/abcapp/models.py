from django.db import models

# Create your models here.

class District(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'district'

    def _str_(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'branch'

    def _str_(self):
        return self.name


class Applicationdetails(models.Model):
    Name = models.CharField(max_length=250)
    DOB = models.CharField(max_length=250)
    Age = models.CharField(max_length=250)
    Gender = models.CharField(max_length=250)
    Phone = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
    Address = models.TextField(max_length=250)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    Account_Type = models.CharField(max_length=250)
    Materials_Provided = models.CharField(max_length=250)

    class Meta:
        db_table = 'applicationdetails'

    def _str_(self):
        return self.Name