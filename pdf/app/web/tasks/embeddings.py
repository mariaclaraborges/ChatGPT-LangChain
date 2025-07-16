from celery import shared_task

from app.web.db.models import Pdf
from app.web.files import download
from app.chat import create_embeddings_for_pdf
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@shared_task()
def process_document(pdf_id: int):
    pdf = Pdf.find_by(id=pdf_id)
    with download(pdf.id) as pdf_path:
        create_embeddings_for_pdf(pdf.id, pdf_path)
        logger.info("Processed PDF: %s", pdf.id)
