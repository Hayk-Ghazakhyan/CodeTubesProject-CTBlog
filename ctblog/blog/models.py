from django.db import models
import pytz

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_posts/", default=None, null=True, blank=True)
    def __str__(self):
        return self.title

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + "-" + self.last_name + " - " + self.timestamp.strftime('%Y-%m-%d %H:%M:%S')


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="blog_comment", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.blog.title + "  -  " + self.message
