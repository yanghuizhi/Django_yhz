from django.db import models

# Create your models here.

# 图书-作者-出版社 布局

class Publisher(models.Model):
    # 出版社有名称、街道地址、所在城市、州(省)、国家和网站。
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        # 这里出现了一个新概念，内嵌在Publisher类定义体中的 class Meta。任何模型都可以使用 Meta 类指定多个针对所在模型的选项。现在我们关注的是排序选项。指定这个选项后，使用 Django 数据库 API 检索 Publisher 对象时，如果没有明确调用 or-der_by()，都按照 name 字段排序。
        ordering = ['name']




class Author(models.Model):
    # 作者有名字、姓和电子邮件地址。
    # blank 允许为空
    first_name = models.CharField(max_length=30,verbose_name='姓氏')
    last_name = models.CharField(max_length=40,verbose_name='名字')
    email = models.EmailField(blank=True, verbose_name='邮箱')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        ordering = ['first_name']

class Book(models.Model):
    # 书有书名和出版日期，还有一位或多位作者(与作者是多对多关系)，以及一个出版社〔出版社(外 键)与书是一对多关系〕。
    # verbose_name 自定义字段名
    title = models.CharField(max_length=100, verbose_name='书名')
    authors = models.ManyToManyField(Author, verbose_name='作者')
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


#  all() 方法。这是 objects 管理器的一个方法，返回数据库中的所有行
#  filter() 示例都返回一个查询集合(可视作列表)
# get() 方法。更适合获取单个对象
# order_by() 方法: 特定值排序结果，还可以反向排序。方法是在字段名称前面加上“-”(减号):
# filter(country="U.S.A.").order_by("-name")  链式查找
# order_by('name')[0] 切片数据
# save() 方法更新一行中的所有列

# 能想把 Apress 出版社的名称由 'Apress' 改为 'Apress Publishing'。使用 save() 的代码如下:
# >>> p = Publisher.objects.get(name='Apress')
# >>> p.name = 'Apress Publishing'
# >>> p.save()

# 若想从数据库中删除一个对象，只需在对象上调用 delete() 方法:
# >>> p = Publisher.objects.get(name="O'Reilly") >>> p.delete()
# >>> Publisher.objects.all()
# [<Publisher: Apress Publishing>]