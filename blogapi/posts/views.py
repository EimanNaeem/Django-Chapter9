from django.contrib.auth import get_user_model
from rest_framework import viewsets # new
from rest_framework.permissions import IsAdminUser # new
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerailizer, UserSerializer


class PostViewset(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerailizer


class UserViewset(viewsets.ModelViewSet): # new
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
