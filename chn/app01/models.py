from django.db import models


class BaiduNews(models.Model):
    news_rank = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    crawling_time = models.DateTimeField()
    link = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

