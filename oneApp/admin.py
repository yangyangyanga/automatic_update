from django.contrib import admin

# Register your models here.
from .models import Monitor, Monitor_copy1
# 注册
class MonitorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'old_id', 'sid', 'university', 'major_name', 'degree_name', 'tuition_fee', 'duration', 'state_code', 'url_now', 'url_old', 'update_time']
    list_filter = ['university']
    list_per_page = 20

admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Monitor_copy1, MonitorAdmin)