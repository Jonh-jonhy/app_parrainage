from django.urls import path 

from . import views 

app_name = "Parrainage"
urlpatterns = [
    path("", views.parrainage_view, name="parrainages"),
    path("<int:filleul_id>/", views.parrainer, name="parrainer")
]
