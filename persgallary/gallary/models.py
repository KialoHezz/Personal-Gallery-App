from django.db import models

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=50)
    Description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()


    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images/')
    updateAt = models.DateTimeField(auto_now_add= True)
    '''
    location and category are foreign keys or one to many relationships
    '''
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name



