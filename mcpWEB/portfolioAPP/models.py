from django.db import models
# Create your models here.

class SongInfo(models.Model):
    title   =   models.CharField(max_length=50)
    artist  =   models.CharField(max_length=50)
    price   =   models.IntegerField(default=0)
    album   =   models.CharField(max_length=50)
    genre   =   models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    writer  =   models.TextField(null = True)
    composer = models.TextField(null = True)
    fee_near_year =  models.IntegerField(default=0)
    img_url_txt = models.TextField(null = True)
    pub_date =  models.DateField(auto_now_add=True)
    img_url = models.ImageField(upload_to='static/img/title_img',default='None.jpg')
    cluster_a =  models.TextField(null = True)
    cluster_bs =  models.TextField(null = True)
    cluster_bl =  models.TextField(null = True)
    def __str__(self):
        return self.title
