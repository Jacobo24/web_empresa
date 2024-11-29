from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
    path('page/edit/<int:id>/', views.page_edit, name='page_edit'),
]