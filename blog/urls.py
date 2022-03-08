from django.urls import path
from .views import Home, detail, category

app_name = 'blog'
urlpatterns = [
    path('', Home.as_view(), name="home"),
]
