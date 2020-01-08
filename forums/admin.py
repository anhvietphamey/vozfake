from django.contrib import admin

from .models import SubForum, Thread, Post

# Register your models here.
class ThreadAdmin(admin.ModelAdmin):
	pass
		

admin.site.register(Thread)
admin.site.register(SubForum)