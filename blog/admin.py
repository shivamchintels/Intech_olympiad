from django.contrib import admin

# Register your models here.

from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["vehicle_type", "manufacturer","model","year_of_purchase","place","distance_travelled","price", "mileage"]
	list_filter = ["vehicle_type", "manufacturer","model","year_of_purchase","place","distance_travelled","price", "mileage"]
	search_fields = ["vehicle_type", "manufacturer","model","year_of_purchase","place","distance_travelled","price", "mileage"]
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
