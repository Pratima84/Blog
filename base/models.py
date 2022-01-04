from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title= models.CharField(max_length=200)
    category= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
    content= models.TextField()
    update = models.DateTimeField(auto_now=True) #change everytime a new instance is cerated 
    created = models.DateTimeField(auto_now_add=True) #save the 1st instance created


    # class Meta:
    #     ordering=['-update','-created']

    def __str__(self):
        return self.title