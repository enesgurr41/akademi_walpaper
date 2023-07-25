from django.db import models

class duvar_Kagidi(models.Model):
    IMAGE_CHOICES = (
        ('duz', 'Düz'),
        ('damask', 'Damask'),
        ('cizgili', 'Çizgili'),
        ('tas_desen', 'Taş Desen'),
        ('cocuk', 'Çocuk'),
        ('cicek_desen', 'Çiçek Desen'),
        ('kircilli', 'Kırçıllı')
    )

    image = models.ImageField(upload_to='duvar_kagitlari/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class duvar_Paneli(models.Model):
    
    image = models.ImageField(upload_to='duvar_panelleri/')
    price = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class stropiyer(models.Model):
    IMAGE_CHOICES = (
        ('dufghfgz', 'Düfghz'),
        ('dafghmask', 'Dafghmask'),
        ('csfghizgili', 'Çizgfghili'),
        ('tas_sfghdesen', 'Taş gfhDesen'),
        ('cocgsdfuk', 'Çofgscuk'),
        ('cicek_sdfgdesen', 'Çiçek sdfgDesen'),
    )

    image = models.ImageField(upload_to='stropiyerler/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class tavan_Kaplama(models.Model):
    IMAGE_CHOICES = (
        ('ddsfgz', 'Dsdfgüz'),
        ('damsdfgask', 'Damsfgask'),
        ('cizggsili', 'Çizgsgili'),
        ('tas_gdesen', 'Taşsfg Desen'),
        ('cocsguk', 'Çocusgk'),
        ('cicekfg_desen', 'Çiçekag Desen'),
    )

    image = models.ImageField(upload_to='tavan_kaplamalari/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class citalama_Dekor(models.Model):
    IMAGE_CHOICES = (
        ('duafdgz', 'Düafgz'),
        ('dafagmask', 'Damafask'),
        ('cizfgili', 'Çiagzgili'),
        ('tas_agagdesen', 'Taş agDesen'),
        ('cocaguk', 'Çoafcuk'),
        ('cicek_afdgdesen', 'Çiçekag Desen'),
    )

    image = models.ImageField(upload_to='salon_citalari/')
    category = models.CharField(choices=IMAGE_CHOICES, max_length=20)
    price = models.CharField(max_length=10)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
