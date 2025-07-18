import boto3
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
S3_REGION = os.getenv('S3_REGION')

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=S3_REGION
)

def subir_a_s3(file):
    """Sube una imagen a S3 y devuelve la URL pública"""
    filename = secure_filename(file.filename)
    s3.upload_fileobj(
        file,
        S3_BUCKET_NAME,
        filename,
        ExtraArgs={'ContentType': file.content_type}
    )
    url = f"https://{S3_BUCKET_NAME}.s3.{S3_REGION}.amazonaws.com/{filename}"
    return url
