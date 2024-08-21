from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Muallif/', views.salom),
    path('task2/<int:son>/', views.key),
    path('Kitob/', views.kitob),
    path('Kitob-2/<int:a>/', views.kitob2),
    path('Record/',views.record),
    path('tmuallif/',views.Tmuallif),
    path('Bkitob/', views.bkitob),
    path('T_ochir/<int:son>',views.ochir),
    path('Talaba/',views.Talaba),
]

