from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import WebsiteInfo, SliderImages, WhyUs


admin.site.unregister(Group)
admin.site.site_header = 'Storm Coffee'

LogEntry.objects.all().delete()




class WebsiteInfoAdmin(admin.ModelAdmin):

	def has_add_permission(self, request):
		return False if self.model.objects.count() > 0 else super().has_add_permission(request)




class SliderImagesAdmin(admin.ModelAdmin):
	list_display = ( 'date_uploaded', 'slider_image')


class WhyUsAdmin(admin.ModelAdmin):
	list_display = ( 'title', 'content')





admin.site.register(WebsiteInfo, WebsiteInfoAdmin)
admin.site.register(SliderImages,SliderImagesAdmin)
admin.site.register(WhyUs, WhyUsAdmin)


