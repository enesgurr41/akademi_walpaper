from django.db import models

class akadem1_Model(models.Model):
    IMAGE_CHOICES = (
        ('duz', 'Düz'),
        ('damask', 'Damask'),
        ('cizgili', 'Çizgili'),
        ('tas_desen', 'Taş Desen'),
        ('cocuk', 'Çocuk'),
        ('cicek_desen', 'Çiçek Desen'),
        ('kircilli', 'Kırçıllı'),
        ('mermer', 'Mermer'),
    )

    image = models.ImageField(upload_to='akadem1_photo/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class akadem2_Model(models.Model):
    IMAGE_CHOICES = (
        ('duz', 'Düz'),
        ('damask', 'Damask'),
        ('cizgili', 'Çizgili'),
        ('cicek_desen', 'Çiçek Desen'),
        ('kircilli', 'Kırçıllı')
    )

    image = models.ImageField(upload_to='akadem2_photo/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class akadem3_Model(models.Model):
    IMAGE_CHOICES = (
        ('duz', 'Düz'),
        ('damask', 'Damask'),
        ('cizgili', 'Çizgili'),
        ('tas_desen', 'Taş Desen'),
        ('cocuk', 'Çocuk'),
        ('cicek_desen', 'Çiçek Desen'),
        ('kircilli', 'Kırçıllı')
    )

    image = models.ImageField(upload_to='akadem3_photo/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class akadem4_Model(models.Model):
    IMAGE_CHOICES = (
        ('duz', 'Düz'),
        ('damask', 'Damask'),
        ('cizgili', 'Çizgili'),
        ('tas_desen', 'Taş Desen'),
        ('cocuk', 'Çocuk'),
        ('cicek_desen', 'Çiçek Desen'),
        ('kircilli', 'Kırçıllı')
    )

    image = models.ImageField(upload_to='akadem4_photo/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class serisonu_Model(models.Model):
    image = models.ImageField(upload_to='serisonu_photo/')
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class duvar_Paneli(models.Model):
    
    image = models.ImageField(upload_to='duvar_panelleri/')
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class aka_Kids(models.Model):

    image = models.ImageField(upload_to='akakids_photo/')
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class poster_Model(models.Model):
    
    image = models.ImageField(upload_to='poster_photo/')
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class blog_Model(models.Model):
    
    image = models.ImageField(upload_to='blog_photo/')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)

    def __str__(self):
        return self.title


class stropiyer_Model(models.Model):
    IMAGE_CHOICES = (
        ('gobek', 'Göbek'),
    )
    image = models.ImageField(upload_to='stropiyer_photo/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class tavan_Kaplama(models.Model):
    image = models.ImageField(upload_to='tavan_kaplamalari/')
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

class citalama_Dekor(models.Model):
    IMAGE_CHOICES = (
        ('salon', 'Salon Çıtası'),
        ('koridor', 'Koridor Çıtası'),
        ('yatak', 'Yatak Odası Çıtası')
    )

    image = models.ImageField(upload_to='salon_citalari/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

