from django.db import models

class Category(models.Model):
    categoryName = models.CharField(max_length=50)
    # slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.categoryName

class Card(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_live = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
            return self.title
    

class SponsorCard(models.Model):
    title = models.CharField(max_length=50)
    is_live = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class MediaCard(models.Model):
    is_live = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return "Media : "+str(self.id)
    

class ContactMessages(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.first_name +" "+ self.last_name