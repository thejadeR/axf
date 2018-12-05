from django.db import models

# Create your models here.
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)
    class Meta:
        abstract = True


class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'

    def __str__(self):
        return '{}-{}-{}'.format(self.name,self.trackid,self.img)