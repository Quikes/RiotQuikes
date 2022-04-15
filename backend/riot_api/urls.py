from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()

router.register("solo", views.SummonerSimpleDataSoloViewset, basename="solo")
router.register("flex", views.SummonerSimpleDataFlexViewset, basename="flex")


urlpatterns = router.urls
