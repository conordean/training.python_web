from django.contrib import admin
from djangor.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'title',
                    'published_today')
    list_filter = ('pub_date', )
    ordering = ('pub_date', )

admin.site.register(Post, PostAdmin)
