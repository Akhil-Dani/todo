from django.db import models

class TodoItem(models.Model):
    item = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.item


