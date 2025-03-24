from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    external_url = models.URLField()  # Course link (Udemy, Coursera, etc.)
    category = models.CharField(max_length=255)  # Example: "Visual Impairment", "Mobility Impairment"
    
    external_url = models.URLField()
    image_url = models.URLField(default="https://via.placeholder.com/150")  # Placeholder image


    def __str__(self):
        return self.title
class UserCertificate(models.Model):
    user_name = models.CharField(max_length=255)
    certificate = models.FileField(upload_to='certificates/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_name}'s Certificate"
