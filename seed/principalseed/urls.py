# Added view
from django.conf.urls import url
from principalseed import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]