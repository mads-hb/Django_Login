from django.conf.urls import url
from . import views
app_name="ula"
urlpatterns=[
    url(r'^$',views.register,name="register"),
    # url(r'^userlogin',views.userlogin,name="userlogin"),
]