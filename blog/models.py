from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=255, help_text="Reklama nomi")
    description = models.TextField(blank=True, null=True, help_text="Reklama tavsifi")
    video = models.FileField(upload_to='videos/', help_text="Reklama uchun video")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, help_text="Yangilangan vaqt")
    is_active = models.BooleanField(default=True, help_text="Reklama faolmi?")

    def __str__(self):
        return self.title
