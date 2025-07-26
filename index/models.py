from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    category_name = models.CharField(max_length=32)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'News Categories'

class News(models.Model):
    title = models.CharField(max_length=128)
    main_content = models.TextField()
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title