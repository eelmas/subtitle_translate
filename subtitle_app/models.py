from django.db import models

# Create your models here.



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
    	return self.document.name

class Translate(models.Model):
    document = models.ForeignKey('subtitle_app.Document', related_name='doct', null=True, on_delete=models.CASCADE)
    suggestion = models.CharField(max_length = 250, blank=True, null=True)
    sentence=models.CharField(max_length = 250, blank=True, null=True)

    def _str_(self):
	    return self.suggestion


