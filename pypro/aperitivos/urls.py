from django.urls import path

from pypro.aperitivos.views import video
from pypro.base import views # noqa

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),
]
