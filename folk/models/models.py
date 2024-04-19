from django.db import models

class Lesson(models.Model):
    category = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
            return f'{self.title}'

class Useful(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
            return f'{self.title}'
    
class Parsing(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
            return f'{self.title}'
    
class Image(models.Model):
      title = models.CharField(max_length=150)
      image = models.ImageField(upload_to='images')

      def __str__(self):
            return f'{self.title}'