from django.db import models
# from django.contrib.auth.models import User

# class UserProfile(models.Model):
#      id = models.AutoField(primary_key=True) 
#      user = models.OneToOneField(User, on_delete=models.CASCADE)
#      bio = models.TextField(blank=True) 
#      def __str__(self):
#         return f"UserProfile(id={self.id}, user={self.user.username}, bio={self.bio or 'No bio provided'})"

class Rectangle:
     def __init__(self, length: int, width: int):
          self.length = length
          self.width = width

     def __iter__(self):
          yield {'length': self.length}
          yield {'width': self.width}

