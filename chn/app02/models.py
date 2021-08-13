from django.db import models


class AdminDivisions(models.Model):
    code = models.CharField(max_length=6)
    admin_name = models.CharField(max_length=60)
    province_code = models.CharField(max_length=2)
    province_name = models.CharField(max_length=60)
    city_code = models.CharField(max_length=2)
    city_name = models.CharField(max_length=60)
    county_code = models.CharField(max_length=2)
    county_name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
