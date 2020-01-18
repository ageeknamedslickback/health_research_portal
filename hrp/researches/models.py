"""Research models."""
from django.db import models
from django.utils import timezone


class Research(models.Model):
    """Create the model for research."""

    url = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    scraped_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Rep title into a human readable form."""
        return self.title
