from django.db import models

# Create your models here.
class Monitor(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    sid = models.IntegerField(blank=True, null=True)
    major_name = models.CharField(max_length=255, blank=True, null=True)
    degree_name = models.CharField(max_length=255, blank=True, null=True)
    tuition_fee = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    state_code = models.IntegerField(blank=True, null=True)
    url_now = models.CharField(max_length=255, blank=True, null=True)
    url_old = models.CharField(max_length=255, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'monitor'

class Monitor_copy1(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    sid = models.IntegerField(blank=True, null=True)
    major_name = models.CharField(max_length=255, blank=True, null=True)
    degree_name = models.CharField(max_length=255, blank=True, null=True)
    tuition_fee = models.CharField(max_length=255, blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)
    state_code = models.IntegerField(blank=True, null=True)
    url_now = models.CharField(max_length=255, blank=True, null=True)
    url_old = models.CharField(max_length=255, blank=True, null=True)
    university = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'monitor_copy1'