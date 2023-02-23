from django.db import models

# Create your models here.
class Task(models.Model):
      content = models.CharField(max_length=300)
      is_completed = models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now_add=True)

      def __str__(self):
            return str(self.content)