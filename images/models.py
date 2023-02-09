from django.db import models

# Create your models here.


class AiAnalysisLog(models.Model):

    id = models.AutoField(primary_key=True)
    image_path = models.CharField(max_length=255, null=True)
    success = models.CharField(max_length=255, null=True)
    message = models.CharField(max_length=255, null=True)
    class_number = models.IntegerField(db_column='class', null=True)
    confidence = models.DecimalField(max_digits=5, decimal_places=4, null=True)
    request_timestamp = models.PositiveIntegerField(null=True)
    response_timestamp = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = 'ai_analysis_log'
