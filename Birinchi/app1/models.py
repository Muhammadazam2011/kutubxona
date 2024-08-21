from django.db import models

class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    mualif = models.SmallIntegerField()
    janr = models.CharField(max_length=10)
    beti = models.SmallIntegerField()

    def __str__(self):
        return f"{self.nom}, {self.mualif}"

class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=30)
    yosh = models.SmallIntegerField()
    userNAME = models.CharField(max_length=30)
    password = models.SmallIntegerField()
    def __str__(self):
        return f"{self.ism}, {self.yosh}"

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    t_yili = models.SmallIntegerField()
    trik = models.BooleanField()

    def __str__(self):
        return f"{self.ism}, {self.t_yili}"

class Oquvchi(models.Model):
    ism = models.CharField(max_length=30)
    h_raqami = models.SmallIntegerField()
    sinf = models.SmallIntegerField()

    def __str__(self):
        return f"{self.ism}, {self.sinf}"

class Record(models.Model):
    oquvchi = models.ForeignKey(Oquvchi,on_delete=models.CASCADE)
    kitob_nomi = models.ForeignKey(Kitob,on_delete=models.CASCADE)
    olgan_sana = models.DateField()
    qaytarish_sana = models.DateField()
    qaytardimi = models.BooleanField()
    kutubxonachi = models.ForeignKey(Kutubxonachi,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.oquvchi}, {self.kitob_nomi}"

class Test(models.Model):
    ism = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.ism}"