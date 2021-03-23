from django.db import models

# Create your models here.
class Project(models.Model):
    # attributes for each project instance of the Project model
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.TextField()
    image = models.FilePathField(path=f"static/{title}.png")
    url = models.URLField()

