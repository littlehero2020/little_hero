from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    site_domain = models.IntegerField(default=1) # 1: 1365, 2: vms look _db_utils.py
    regist_no = models.BigIntegerField(default=0)
    url = models.TextField(default='https://www.1365.go.kr/vols/1572247904127/partcptn/timeCptn.do', max_length=500)
    title = models.CharField(max_length=300)
    address_city = models.CharField(max_length=100, default='')
    address_gu = models.CharField(max_length=100, default='')
    address_remainder = models.CharField(max_length=200, default='')
    recruit_status = models.BooleanField(default=True) # true if recruiting now
    adult_status = models.BooleanField(default=True) # true if adult and false if student
    domain = models.TextField(default='')
    telephone = models.CharField(max_length=200, default='')
    text = models.TextField(default='')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    do_date_extra = models.CharField(default='', max_length=200)
    recruit_company = models.CharField(default='', max_length=300)
    recruit_member = models.CharField(default='0 명 / 일', max_length=200)
    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title