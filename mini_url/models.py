from django.db import models
import random
import string

class MiniURL(models.Model):
    url = models.URLField(verbose_name="URL à réduire", unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")
    pseudo = models.CharField(max_length=225, null=True, blank=True)
    nb_acces = models.IntegerField(default=0, verbose_name="Nombre d'accès à l'URL")


    def __str__(self):
        return f"{0} {1}".format(self.code, self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generer(6)

        super(MiniURL, self).save(*args, **kwargs)


    # Fonction qui permet de generer le code
    def generer(nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
        return "".join(aleatoire)


    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"

