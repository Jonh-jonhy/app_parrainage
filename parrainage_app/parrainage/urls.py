from django.urls import path 

from . import views 

app_name = "parrainage"
urlpatterns = [
    path("", views.acceuil_view, name="acceuil"),
    path("pdf", views.pdf, name="pdf"),
    path("tirage", views.parrainage_view, name="parrainages"),
    path("<int:filleul_id>/", views.parrainer, name="parrainer")
]
