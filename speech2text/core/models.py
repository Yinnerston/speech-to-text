from django.db import models

class SpeechModel(models.Model):
    transcription = models.CharField(max_length=1000)
    segments = models.JSONField(null=True)
    audio_file = models.FileField(upload_to='audio_files/%Y/%m/%d', null=True, verbose_name="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
