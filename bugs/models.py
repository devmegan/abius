from django.db import models
# from django.contrib.auth.models import User

from django.utils import timezone

# Bug App models go here


class Bug(models.Model):
    """ model for the bugs """
    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    urgency = models.IntegerField(range(1, 4), default=1, blank=False)
    # user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(default=timezone.now, blank=False)
    assigned_to = models.CharField(
        max_length=40, blank=False, default="unclaimed"
    )
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
