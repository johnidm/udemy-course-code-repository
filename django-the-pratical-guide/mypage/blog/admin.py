from django.contrib import admin

from .models import Post, Tag, Author, Comment, Favorite
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "date")


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Favorite)

