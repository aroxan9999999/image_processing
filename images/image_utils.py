import os
import boto3
from botocore.exceptions import NoCredentialsError
from PIL import Image as PILImage
from io import BytesIO
from django.core.files.base import ContentFile
from django.conf import settings

def resize_image(image):
    pil_image = PILImage.open(image.original)

    sizes = {
        'thumbnail': (150, 120),
        'big_thumb': (700, 700),
        'big_1920': (1920, 1080),
        'd2500': (2500, 2500),
    }

    for size, dimensions in sizes.items():
        pil_resized = pil_image.copy()
        pil_resized.thumbnail(dimensions, PILImage.LANCZOS)
        buffer = BytesIO()
        pil_resized.save(buffer, format='JPEG')
        file_content = ContentFile(buffer.getvalue())
        getattr(image, size).save(f"{size}.jpg", file_content)

def upload_to_s3(image):
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_REGION')
    )
    bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')

    for field in ['original', 'thumbnail', 'big_thumb', 'big_1920', 'd2500']:
        file = getattr(image, field)
        if not file:
            continue
        file_path = file.path
        try:
            s3_client.upload_file(file_path, bucket_name, f"{field}/{image.id}.jpg")
            print(f"Uploaded {field} to S3")
        except FileNotFoundError:
            print("The file was not found")
        except NoCredentialsError:
            print("Credentials not available")
