from django.contrib import admin
from core.models import SpeechModel
# Register your models here.
@admin.register(SpeechModel)
class SpeechModelAdmin(admin.ModelAdmin):
    list_display = ('transcription', 'created_at', 'updated_at', 'segments')