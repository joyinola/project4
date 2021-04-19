from django.contrib.auth.models import AbstractUser
from django.db import models




class User(AbstractUser):
	
	Following=models.IntegerField(blank=True,default=0)
	Follower=models.IntegerField(blank=True,default=0)
	profile_img=models.ImageField(upload_to='profile_pics', default='profile.png')
	def __str__(self):
		return(f'{self.username}')
class Follows(models.Model):
	User_involved=models.ForeignKey(User,on_delete=models.CASCADE)
	Follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follow')
	# def __str__(self):
	# 	return(f'{self.Follower}')
class Posts(models.Model):
 	User=models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
 	Img=models.ImageField(upload_to='Post_img',blank=True)
 	Caption=models.TextField(blank=True)
 	Timestamp=models.DateTimeField(auto_now_add=True)
 	Likes=models.IntegerField(default=0)
 	def count(self):
 		return Like.objects.filter(Post=self).all().count()
 	def __str__(self):
 		return(f'{self.User} posted {self.Caption} on {self.Timestamp}')
class Like(models.Model):
	Post=models.ForeignKey(Posts, on_delete=models.CASCADE)
	User=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return f'{self.User} liked {self.Post}'
	