
from django.conf.urls import url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from barter.views import user_list, user_detail, user_signin, item_list, user_items

# router = DefaultRouter()
# router.register(prefix='chains', viewset=ChainViewSet)
# router.register(prefix='stores', viewset=StoreViewSet)
# router.register(prefix='employees', viewset=EmployeeViewSet)
# router.register(prefix='users', viewset=UserViewSet)

urlpatterns = [
    url(r'^users/$', user_list),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail),
    url(r'^users/signin/$', user_signin),
    url(r'^items/$', item_list),
    url(r'^items/(?P<fk>[0-9]+)/$', user_items),
]

# urlpatterns += router.urls
