from django.db import models

# Create your models here.

# 文章分类
class Category(models.Model):
    caption = models.CharField(max_length=16)

#  标签
class ArticleType(models.Model):
    caption = models.CharField(max_length=16)

#  文章表
class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=255)

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    article_type = models.ForeignKey(ArticleType,on_delete=models.CASCADE)

    # type_choice = (
    #     (1, 'Python'),
    #     (2, 'OpenStack'),
    #     (3, 'Linux'),
    # )
    # article_type_id = models.IntegerField(choices=type_choice)


