from django.urls import path
from  .import views

app_name = "elecciones"
urlpatterns = [
    path('',views.index,name="index"),
    path('<int:region_id>/', views.candidatos, name="candidatos"),
    path('<int:region_id>/detalle', views.detalle, name="detalle"),
]