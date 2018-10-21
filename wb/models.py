from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=70)
    sec_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def getfullname(self):
        return self.first_name + ' ' + self.last_name


class Comment(models.Model):
      comment = models.CharField(max_length=1000)

# class Photo(models.Model):
#
#
# class Contact(models.Model):
#
#
# class Message(models.Model):
#
#
# class Notification(models.Model):
#
#
# class Friend(models.Model):
#
#
# class Post(models.Model):
