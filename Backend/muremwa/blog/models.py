from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# author
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    image = models.FileField()
    bio = models.TextField()

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)


# tags
class Tags(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField()

    def __str__(self):
        return self.title


# blog
class Blog(models.Model):
    name = models.CharField(max_length=500)
    lead_text = models.TextField(default="To be added")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    image = models.FileField()
    tags = models.ManyToManyField(Tags, help_text="Enter as many tags")

    def get_absolute_url(self):
        return reverse('blog', args=[str(self.id)])

    def __str__(self):
        return "{} by {}".format(self.name, self.author)

    class Meta:
        ordering = ['date']


# entries
class Entry(models.Model):
    id = models.IntegerField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    image = models.FileField()

    def __str__(self):
        return "{} from the blog '{}'".format(self.title, self.blog)


# comments
class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "comment by {} on the blog '{}'".format(self.user, self.blog)

    class Meta:
        ordering = ['time']
