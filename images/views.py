from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Image
from .forms import ImageUploadForm
from .serializers import ImageUploadSerializer
from .tasks import process_image

class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            process_image.delay(image.id)
            return JsonResponse({'success': True, 'image_id': image.id}, status=status.HTTP_201_CREATED)
        return JsonResponse({'success': False, 'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)

class ImageListView(APIView):
    def get(self, request, project_id, *args, **kwargs):
        images = Image.objects.filter(project_id=project_id)
        serializer = ImageUploadSerializer(images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

def upload_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            process_image.delay(image.id)
            return JsonResponse({'success': True, 'image_id': image.id})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def image_list_view(request, project_id):
    images = Image.objects.filter(project_id=project_id)
    return render(request, 'image_list.html', {'images': images})
