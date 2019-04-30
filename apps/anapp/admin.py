from django.contrib import admin
from .models import Doctor, Feedback


# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient_name', 'feedback_date', 'satisfied',)
    list_filter = ('doctor', 'feedback_date',)
    search_fields = ('doctor__name',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Feedback, FeedbackAdmin)
