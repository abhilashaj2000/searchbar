
from django.urls import path,include
from web.views import index,new

app_name = "web"
urlpatterns = [
    path("",index,name="index"),
    path("add",new,name="new")
]