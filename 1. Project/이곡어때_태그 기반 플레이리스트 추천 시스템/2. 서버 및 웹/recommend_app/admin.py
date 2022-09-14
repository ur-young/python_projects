from django.contrib import admin
from .models import Post

class RecommendAdmin(admin.ModelAdmin):
    readonly_fields = ('id','postdate',)
    pass
admin.site.register(Post, RecommendAdmin)
# Register your models here.
