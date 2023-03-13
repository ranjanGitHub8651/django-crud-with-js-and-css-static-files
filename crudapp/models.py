from django.db import models


class Employee(models.Model):
    designation = (
        ('WEB DEVELOPER','WEB DEVELOPER'),
        ("PYTHON DEVELOPER", "PYTHON DEVELOPER"),
        ("DJANGO DEVELOPER", "DJANGO DEVELOPER"),
        ("PYTHON & DJANGO DEVELOPER", "PYTHON & DJANGO DEVELOPER"),
        ("FULLSTACK DEVELOPER", "FULLSTACK DEVELOPER"),
        ("JAVA DEVELOPER", "JAVA DEVELOPER"),
        ("FRONTEND DEVELOPER", "FRONTEND DEVELOPER"),
        ("OTHER DEVELOPER", "OTHER DEVELOPER"),
    )
    id = models.AutoField(primary_key=True, auto_created=True,),
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=200)
    designation = models.CharField(max_length=200,
                        choices=designation,
                        default="PYTHON DEVELOPER")
    location = models.CharField(max_length=200)
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,)

    def __str__(self):
        return str(self.id) +" "+ self.last_name +" "+ self.last_name
