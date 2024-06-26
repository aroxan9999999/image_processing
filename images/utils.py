import logging
from celery import shared_task
from .models import Image
from .image_utils import resize_image, upload_to_s3

logger = logging.getLogger(__name__)

@shared_task
def process_image(image_id):
    try:
        logger.info(f'Starting task to process image with ID: {image_id}')
        image = Image.objects.get(id=image_id)
        resize_image(image)
        upload_to_s3(image)
        image.state = 'processed'
        image.save()
        logger.info(f'Finished processing image with ID: {image_id}')
        return {'message': "Processing complete", 'state': image.state}
    except Exception as e:
        logger.error(f"Error processing image with ID {image_id}: {e}")
        return {'message': "Processing failed", 'error': str(e)}
