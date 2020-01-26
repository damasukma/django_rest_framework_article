from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Category

class Category(models.Model):

    category_name = models.CharField(max_length=255)

    class Meta:

        ordering = ['category_name']

    def __str__(self):

        return self.category_name

# article

class Article(models.Model):

    title = models.CharField(max_length=255, null=False)
    sub_title = models.CharField(max_length=255, null=False)
    excerpt = models.TextField(null=False) #ringkasan content
    content = models.TextField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    pub_date = models.DateField()

    class Meta:

        ordering = ['title']

    def __str__(self):

        return "%s %s" %(self.title, self.pub_date)

# TAG
class Tag(models.Model):

    tag_name = models.CharField(max_length=255, null=False)
    articles = models.ManyToManyField(Article)

    class Meta:

        ordering = ['tag_name']

    def __str__(self):

        return self.tag_name