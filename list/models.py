from django.db import models

class list(models.Model):

    Booth = models.CharField(max_length=10,default=" ")
    section = models.IntegerField(default=0)
    center = models.CharField(max_length=100,default="  ")
    name_hindi =models.CharField(max_length=100,blank=True,default="  ")
    name_english =models.CharField(max_length=100,blank=True,default="  ")
    name_new =models.CharField(max_length=100,blank=True,default="  ")
    relation_name_hindi =models.CharField(max_length=100,blank=True,default="  ")
    relation_name_english =models.CharField(max_length=100,blank=True,default="  ")
    relation_type =models.CharField(max_length=100,blank=True,default="  ")
    address_hindi =models.CharField(max_length=100,blank=True,default="  ")
    address_english = models.CharField(max_length=100,blank=True,default="  ")
    TEHSIL =models.CharField(max_length=100,blank=True,default="  ")
    gender =models.CharField(max_length=100,blank=True,default="  ")
    dob = models.CharField(blank=True,max_length=20,default="  ")
    MOBILE = models.IntegerField(blank=True,default=0)


    def __str__(self):
        return self.name_english

class Agra(list):
     pass

class Aligarh(list):
    pass

class Auraiya(list):
    pass

class Etah(list):
    pass

class Etawah(list):
    pass

class Farrukhabad(list):
    pass

class Firozabad(list):
    pass

class Hathras(list):
    pass

class Kasganj(list):
    pass

class Kannauj(list):
    pass

class Mainpuri(list):
    pass

class Mathura(list):
    pass

class Aligarh_c(list):
    pass
