from django.contrib import admin
from core.models import WorkshopRepair, Rating, Sale, Product, Order, Comment
from django.contrib.contenttypes.admin import GenericTabularInline


# Register your models here.
class CommentInline(GenericTabularInline):
    model = Comment
    max_num = 1


class WorkshoprepairAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    inlines = [CommentInline]

class RatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'rating']

class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'text', 'object_id', 'content_type', 'content_object'
    ]


admin.site.register(WorkshopRepair, WorkshoprepairAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Sale)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Comment, CommentAdmin)