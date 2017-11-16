# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Base1M(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.TextField(blank=True, null=True)
    domain_type = models.ForeignKey('DomainType', models.DO_NOTHING, db_column='domain_type', blank=True, null=True)
    domain_owner = models.CharField(max_length=20, blank=True, null=True)
    charge_type = models.IntegerField(blank=True, null=True)
    charge_cycle = models.IntegerField(blank=True, null=True)
    charge_cycle_order = models.IntegerField(blank=True, null=True)
    peak = models.IntegerField(blank=True, null=True)
    valley = models.IntegerField(blank=True, null=True)
    requst = models.IntegerField(blank=True, null=True)
    flow = models.IntegerField(blank=True, null=True)
    bandwidth = models.IntegerField(blank=True, null=True)
    page_view = models.IntegerField(blank=True, null=True)
    http_code_20x = models.IntegerField(blank=True, null=True)
    http_code_30x = models.IntegerField(blank=True, null=True)
    http_code_40x = models.IntegerField(blank=True, null=True)
    http_code_50x = models.IntegerField(blank=True, null=True)
    http_code_0 = models.IntegerField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    miss = models.IntegerField(blank=True, null=True)
    hit_flow = models.IntegerField(blank=True, null=True)
    miss_flow = models.IntegerField(blank=True, null=True)
    miss_bandwidth = models.IntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_1m'


class Base5M(models.Model):
    domain = models.TextField(blank=True, null=True)
    domain_type = models.ForeignKey('DomainType', models.DO_NOTHING, db_column='domain_type', blank=True, null=True)
    domain_owner = models.CharField(max_length=20, blank=True, null=True)
    peak = models.IntegerField(blank=True, null=True)
    requst = models.IntegerField(blank=True, null=True)
    flow = models.IntegerField(blank=True, null=True)
    bandwidth = models.FloatField(blank=True, null=True)
    page_view = models.IntegerField(blank=True, null=True)
    http_code_20x = models.IntegerField(blank=True, null=True)
    http_code_30x = models.IntegerField(blank=True, null=True)
    http_code_40x = models.IntegerField(blank=True, null=True)
    http_code_50x = models.IntegerField(blank=True, null=True)
    http_code_0 = models.IntegerField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    miss = models.IntegerField(blank=True, null=True)
    hit_flow = models.IntegerField(blank=True, null=True)
    miss_flow = models.IntegerField(blank=True, null=True)
    miss_bandwidth = models.FloatField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_5m'


class Base5MDomainCom(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.TextField(blank=True, null=True)
    peak = models.IntegerField(blank=True, null=True)
    requst = models.IntegerField(blank=True, null=True)
    flow = models.IntegerField(blank=True, null=True)
    page_view = models.IntegerField(blank=True, null=True)
    http_code_20x = models.IntegerField(blank=True, null=True)
    http_code_30x = models.IntegerField(blank=True, null=True)
    http_code_40x = models.IntegerField(blank=True, null=True)
    http_code_50x = models.IntegerField(blank=True, null=True)
    http_code_0 = models.IntegerField(blank=True, null=True)
    hit = models.IntegerField(blank=True, null=True)
    miss = models.IntegerField(blank=True, null=True)
    hit_flow = models.IntegerField(blank=True, null=True)
    miss_flow = models.IntegerField(blank=True, null=True)
    miss_bandwidth = models.IntegerField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_5m_domain_com'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DomainInfo(models.Model):
    domain = models.TextField(blank=True, null=True)
    domain_type = models.ForeignKey('DomainType', models.DO_NOTHING, db_column='domain_type', blank=True, null=True)
    charge_type = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    domain_owner = models.CharField(max_length=20, blank=True, null=True)
    cname = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)
    https = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    charge_cycle = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domain_info'


class DomainType(models.Model):
    name = models.TextField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domain_type'


class IpCity(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey('ShArea', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_city'


class Log(models.Model):
    domain = models.CharField(max_length=50)
    date = models.DateTimeField()
    size = models.CharField(max_length=15, blank=True, null=True)
    logtype = models.CharField(max_length=20, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    domain_type = models.ForeignKey('self', models.DO_NOTHING, db_column='domain_type')

    class Meta:
        managed = False
        db_table = 'log'


class RequestRecord(models.Model):
    client_ip = models.CharField(max_length=20)
    source_ip = models.CharField(max_length=20)
    request_number = models.IntegerField()
    log_type = models.CharField(max_length=20)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'request_record'


class RequestTest(models.Model):
    client_ip = models.CharField(max_length=20)
    source_ip = models.CharField(max_length=20)
    request_number = models.IntegerField()
    log_type = models.CharField(max_length=20)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'request_test'


class ShArea(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    merger_name = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    pinyin = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    first = models.CharField(max_length=50, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sh_area'


class TblEventsLog(models.Model):
    pro_name = models.CharField(max_length=50)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_events_log'
