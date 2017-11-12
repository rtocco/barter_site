
from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from retail.views import ChainViewSet, StoreViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(prefix='chains', viewset=ChainViewSet)
router.register(prefix='stores', viewset=StoreViewSet)
router.register(prefix='employees', viewset=EmployeeViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
