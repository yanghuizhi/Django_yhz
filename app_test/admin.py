from django.contrib import admin

# Register your models here.

from .models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    # 若在后台中展示其他字段，需此配置
    # 定义 AuthorAdmin 类。它是 django.contrib.admin.ModelAdmin 的子类，存放指定模型在管理后台中的 自定义配置。我们只做了一项定制，list_display，把它的值设为一个元组，指定要在修改列表页面 显示的字段名称。当然，模型中必须有这些字段。
    # 修改 admin.site.register() 调用，在 Author 后面添加 AuthorAdmin。你可以把这行代码理解为“以 Au- thorAdmin 中的选项注册 Author 模型”。admin.site.register() 函数的第二个参数可选，其值是一个 ModelAdmin 子类。如果不指定第二个参数(Publisher 和 Book 模型就是这样)，Django 使用默认选项 注册模型。

    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher','publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',) # 减号为倒叙
    filter_horizontal = ('authors',)  # js效果，动态搜索作者
    raw_id_fields = ('publisher',)  # 出版社的搜索，解决数据量大的问题

# 下列代码告诉 Django 管理后台，为这几个模型提供界面。
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)


