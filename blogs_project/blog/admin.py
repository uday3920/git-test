from django.contrib import admin
from blog.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    #it fetches automatic text from one field to another

    list_filter=('status','author')
    #a filter pane is available in the admin page

    search_fields=('title','body')
    #it searches the content in the given fields and a search box is available in the admin page

    raw_id_fields=('author',)
    # it simple shows a 'search icon' beside of the author field in the admin page

    date_hierarchy='publish'
    # it shows a nav bar to the specified fields

admin.site.register(Post,PostAdmin)
