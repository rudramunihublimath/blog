from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline =models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    pub_date = models.DateField()
    author = models.ManyToManyField(Author)
    def __str__(self):
        return self.headline


class PetModel(models.Model):
    name = models.CharField(max_length=20,primary_key=True)
    owner = models.CharField(max_length=20)
    species = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    birth = models.DateField()
    death = models.DateField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'pet'




