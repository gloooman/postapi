from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(max_length=200, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_likes(self):
        return self.ratio_set.filter(opinion='like').count()

    def get_dislikes(self):
        return self.ratio_set.filter(opinion='dislike').count()

    def get_ratio(self):
        return self.get_likes() - self.get_dislikes()


class Ratio(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    NONE = None
    ACTIONS = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NONE, 'No opinion')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    opinion = models.CharField(max_length=7, choices=ACTIONS, default=NONE, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.opinion} (Post: {self.post}, User: {self.user})'
