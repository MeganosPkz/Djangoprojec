from django.contrib import admin
from.models import livros

# Register your models here.
class livrosAdmin(admin.ModelAdmin):
    list_display=["titulo"]

admin.site.register(livros, livrosAdmin)