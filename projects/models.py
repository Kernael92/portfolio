from django.db import models

# Create your models here.
class Developer(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    userName = models.CharField(max_length =30)
    email = models.EmailField()

    def __str__(self):
        return self.userName

class Repository(models.Model):
    title = models.CharField(max_length =30)
    description = models.CharField(max_length = 245)
    developer = models.ForeignKey(Developer)
    pub_date = models.DateTimeField(auto_now_add=True)
    