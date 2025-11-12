# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    mobile = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Portfolio(models.Model):

    #__Portfolio_FIELDS__
    sap_id = models.CharField(max_length=255, null=True, blank=True)
    circle = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    cmp = models.CharField(max_length=255, null=True, blank=True)
    sharer1 = models.BooleanField()
    sharer2 = models.BooleanField()
    rfs1_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    rfs2_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    supply = models.BooleanField()
    so_load_sharer1 = models.CharField(max_length=255, null=True, blank=True)
    so_load_sharer2 = models.BooleanField()
    sla_cat = models.CharField(max_length=255, null=True, blank=True)
    tower = models.BooleanField()

    #__Portfolio_FIELDS__END

    class Meta:
        verbose_name        = _("Portfolio")
        verbose_name_plural = _("Portfolio")


class Raw_Uptime(models.Model):

    #__Raw_Uptime_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    circle = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    sap_id = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    raw_uptime = models.CharField(max_length=255, null=True, blank=True)
    raw_down_min = models.CharField(max_length=255, null=True, blank=True)
    sla_cat = models.CharField(max_length=255, null=True, blank=True)

    #__Raw_Uptime_FIELDS__END

    class Meta:
        verbose_name        = _("Raw_Uptime")
        verbose_name_plural = _("Raw_Uptime")


class Ccp_Thin(models.Model):

    #__Ccp_Thin_FIELDS__
    sap_id = models.CharField(max_length=255, null=True, blank=True)
    downtime_start = models.DateTimeField(blank=True, null=True, default=timezone.now)
    downtime_end = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cause = models.CharField(max_length=255, null=True, blank=True)
    sub_cause = models.CharField(max_length=255, null=True, blank=True)
    raw_minutes = models.IntegerField(null=True, blank=True)
    excl_minutes = models.IntegerField(null=True, blank=True)
    comm_minutes = models.IntegerField(null=True, blank=True)
    supply = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    rca = models.ForeignKey(excl_matrix, on_delete=models.CASCADE)
    criteria = models.BooleanField()

    #__Ccp_Thin_FIELDS__END

    class Meta:
        verbose_name        = _("Ccp_Thin")
        verbose_name_plural = _("Ccp_Thin")


class Excl_Matrix(models.Model):

    #__Excl_Matrix_FIELDS__
    cause = models.TextField(max_length=255, null=True, blank=True)
    sub_cause = models.CharField(max_length=255, null=True, blank=True)
    rca = models.CharField(max_length=255, null=True, blank=True)
    criteria = models.BooleanField()

    #__Excl_Matrix_FIELDS__END

    class Meta:
        verbose_name        = _("Excl_Matrix")
        verbose_name_plural = _("Excl_Matrix")



#__MODELS__END
