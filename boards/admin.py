from django.contrib import admin
from .models import Board,Topic,Post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    # list_display 属性控制 Post 列表页展示的字段
    # fields 属性，用来控制表单展现的字段
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

# 后台注册之后，前端才能展示出来
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post,PostAdmin)