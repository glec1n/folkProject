from django.db import models
from django.contrib.auth.models import User

class Lesson(models.Model):
    category = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
            return f'{self.title}'

class Useful(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
            return f'{self.title}'
    
class Parsing(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
            return f'{self.title}'
    
class Practice(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
            return f'{self.title}'
    
class Image(models.Model):
      title = models.CharField(max_length=150)
      image = models.ImageField(upload_to='images')

      def __str__(self):
            return f'{self.title}'
      
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]
    
class CommentUseful(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    useful = models.ForeignKey(Useful, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.comment[0:50]