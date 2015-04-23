from django.contrib import admin
from blog.models import *

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    pass



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass