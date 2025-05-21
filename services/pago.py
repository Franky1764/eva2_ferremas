import os
from flask.cli import load_dotenv
from transbank.common.options import WebpayOptions
from transbank.common.integration_type import IntegrationType

load_dotenv()
options = WebpayOptions(
    commerce_code=os.getenv('WEBPAY_COMMERCE_CODE'),
    api_key=os.getenv('WEBPAY_API_KEY'),
    integration_type=IntegrationType.TEST
)
