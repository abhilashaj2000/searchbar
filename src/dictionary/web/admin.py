from django.contrib import admin
from web.models import Word,Wordmeanig

class  WordAdmin(admin.ModelAdmin):
   word_display = ["id","word"]

admin.site.register(Word,WordAdmin)

class  WordmeanigAdmin(admin.ModelAdmin):
   meaing_display = ["id","word","property","Wordmeanig"]

admin.site.register(Wordmeanig,WordmeanigAdmin)

# Register your models here.
