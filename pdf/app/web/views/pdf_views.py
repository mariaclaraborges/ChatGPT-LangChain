from flask import Blueprint, g, jsonify
from werkzeug.exceptions import Unauthorized
from app.web.hooks import login_required, handle_file_upload, load_model
from app.web.db.models import Pdf
from app.web.tasks.embeddings import process_document
from app.web import files
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bp = Blueprint("pdf", __name__, url_prefix="/api/pdfs")


@bp.route("/", methods=["GET"])
@login_required
def list():
    pdfs = Pdf.where(user_id=g.user.id)

    return Pdf.as_dicts(pdfs)


@bp.route("/", methods=["POST"])
@login_required
@handle_file_upload
def upload_file(file_id, file_path, file_name):
    res, status_code = files.upload(file_path)
    if status_code >= 400:
        return res, status_code

    pdf = Pdf.create(id=file_id, name=file_name, user_id=g.user.id)
    logger.info("PDF created with ID: %s", pdf.id)

    # TODO: Defer this to be processed by the worker
    process_document.delay(pdf.id)
    logger.info("status_code: %s", status_code)

    return pdf.as_dict()


@bp.route("/<string:pdf_id>", methods=["GET"])
@login_required
@load_model(Pdf)
def show(pdf):
    return jsonify(
        {
            "pdf": pdf.as_dict(),
            "download_url": files.create_download_url(pdf.id),
        }
    )
