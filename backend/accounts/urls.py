from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register('accounts',views.CustomUserViewset, basename='accounts')

urlpatterns = router.urls