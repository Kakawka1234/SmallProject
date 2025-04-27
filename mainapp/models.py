from django.db import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новий'),
        ('in_progress', 'В процесі'),
        ('completed', 'Виконано'),
    ]
    
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    def get_status_display(self):
        return dict(self.STATUS_CHOICES).get(self.status, self.status)