from django.urls import path
from . import views
from .views import signindataget,signindataput,signindatadelete,logindatalist

urlpatterns = [
    path('signindatalist/',views.signindatalist,name='signindatalist'),
    path('signindataget/<int:id>/',signindataget.as_view(),name='signindataget'),
    path('signindataput/<int:id>/',signindataput.as_view(),name='signindataput'),
    path('signindatadelete/<int:id>/',signindatadelete.as_view(),name='signindatadelete'),
    path('logindatalist/',logindatalist.as_view(),name='logindatalist'),
]
