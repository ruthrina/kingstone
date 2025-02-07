from django.contrib import admin
from django.contrib import admin
from .models import ContactMessage

from .models import Event, New,ExecutiveLeader, Prefect, Staff, SchoolGallery,Application, UNEBPerformance, UCEPerformance, UACEPerformance





# Register your models here.



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'link')
    search_fields = ('title',)
    list_filter = ('date',)

@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'link')
    search_fields = ('title',)
    list_filter = ('created_at',)

class ExecutiveLeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'photo')

admin.site.register(ExecutiveLeader, ExecutiveLeaderAdmin)    


admin.site.register(Prefect)

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'category')
    list_filter = ('category',)

admin.site.register(Staff, StaffAdmin)



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)



@admin.register(SchoolGallery)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at') 



@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'intended_class', 'submitted_at')
    search_fields = ('first_name', 'last_name', 'email', 'intended_class')



class UCEPerformanceInline(admin.TabularInline):
    model = UCEPerformance
    extra = 1  # Show at least 1 row for new entries

class UACEPerformanceInline(admin.TabularInline):
    model = UACEPerformance
    extra = 1  # Show at least 1 row for new entries

@admin.register(UNEBPerformance)
class UNEBPerformanceAdmin(admin.ModelAdmin):
    list_display = ('year',)
    search_fields = ('year',)
    inlines = [UCEPerformanceInline, UACEPerformanceInline]  # Display tables in admin
