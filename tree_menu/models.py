from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    menu_name = models.CharField(max_length=100, db_index=True)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=300, blank=True)
    named_url = models.CharField(max_length=100, blank=True)

    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ['parent_id', 'id']

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except:
                return '#'
        return self.url or '#'

    def __str__(self):
        return f"{self.title} ({self.menu_name})"
