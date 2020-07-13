import datetime
from django.contrib.auth import get_user_model
from django.db.models.functions import TruncDay
from django.db.models import Count, Q

from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from posts.models import Post, Ratio
from . import serializers

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the User model
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )


class PostViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the Post model
    """
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (AllowAny,)


class RatioViewSet(viewsets.ModelViewSet):
    """
    Provides basic CRUD functions for the Ratio model
    """
    queryset = Ratio.objects.all()
    serializer_class = serializers.RatioSerializer
    permission_classes = (AllowAny,)


@api_view(['GET'])
def ratio_analitics(request):
    date_from = datetime.datetime.strptime(request.query_params.get('Date_from'), '%Y-%m-%d')
    date_to = datetime.datetime.strptime(request.query_params.get('date_to'), '%Y-%m-%d')

    ratio = Ratio.objects\
        .filter(created__gte=date_from, created__lte=date_to)\
        .annotate(day=TruncDay('created'))\
        .values('day')\
        .annotate(likes=Count('id', filter=Q(opinion='like')), dislikes=Count('id', filter=Q(opinion='dislike')))\
        .values('day', 'likes', 'dislikes')

    return Response(ratio, status=status.HTTP_200_OK)