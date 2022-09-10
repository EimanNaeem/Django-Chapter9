from django.urls import path
from rest_framework.routers import SimpleRouter # new
from .views import PostViewset, UserViewset # new

router = SimpleRouter()
router.register("users", UserViewset, basename="users")
router.register("", PostViewset, basename="posts")

urlpatterns = router.urls
