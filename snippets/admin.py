from snippets.models import Snippet
from django.contrib import admin


# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'title', 'code', 'linenos', 'language', 'style', 'created'
    ]


admin.site.register(Snippet, SnippetAdmin)
