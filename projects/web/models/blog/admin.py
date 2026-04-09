from django.contrib import admin
from blog.models import Student


# Register your models here.
# admin.site.register(Student)


@admin.register(Student)
class adminn(admin.ModelAdmin):   #create class then use admin.model.admin keyword

    list_display = ('name','age','company')
    search_fields = ('name','company',)
    list_filter=('age','city')
    ordering = ('name',)
