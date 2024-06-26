from django.urls import path
from .views import ImageUploadView, ImageListView, upload_view, image_list_view

urlpatterns = [
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('upload-view/', upload_view, name='upload-view'),
    path('projects/<int:project_id>/images/', ImageListView.as_view(), name='images-list'),
    path('projects/<int:project_id>/images_list/', image_list_view, name='image-list-view'),
]
