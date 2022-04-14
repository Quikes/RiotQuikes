from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("users", views.CustomUserViewset, basename="users")

urlpatterns = router.urls
