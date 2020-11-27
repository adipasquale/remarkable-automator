import sys
from rmapy.document import ZipDocument
from rmapy.api import Client

rmapy_client = Client()
rmapy_client.renew_token()
doc = ZipDocument(doc=sys.argv[1])
rmapy_client.upload(doc)
