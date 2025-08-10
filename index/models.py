from django.db import models
from django.contrib.auth.models import User


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

    class Meta:
        verbose_name_plural = 'News'


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Комментарий от {self.author.username} к {self.news.title}"