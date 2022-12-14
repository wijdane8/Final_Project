from django.db import models
from django.contrib.auth.models import User
from accounts.models import Specialist,Member

# Create your models here.

class Group(models.Model):
    specialist =models.ForeignKey(Specialist,on_delete=models.CASCADE,default='')
    member= models.ManyToManyField(Member)
    group_name=models.CharField(max_length=1024)
    group_info=models.TextField()
    member_number=models.IntegerField( default=0)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    created_by=models.CharField(max_length=1024)
    missions_total=models.IntegerField(default=0)
    complete_mission=models.IntegerField(default=0)
    is_active=models.BooleanField()
    chat_url=models.URLField(default="")



class Mission(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE,default='')
    member= models.ManyToManyField(Member)
    mission_name=models.CharField(max_length=1024)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    mission_check=models.BooleanField(default=0)


class Post(models.Model):

    post_type_choices = models.TextChoices("Post Type", ["Article", "story"])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    content = models.TextField()
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    is_published = models.BooleanField()
    post_type  = models.CharField(max_length=64, choices = post_type_choices.choices, default=post_type_choices.Article)

    def __str__(self) -> str:
        return f"{self.title}, {self.publish_date}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)
    name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
