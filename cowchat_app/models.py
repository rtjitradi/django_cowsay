from django.db import models


# Has a model that we can save the text line to
# Create your models here.


class TextLine (models.Model):
    text_line = models.CharField(max_length=150)

    def __str__(self):
        return self.text_line
