from django.db import models

class Testers(models.Model):
    tester_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tester_name