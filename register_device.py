import sys
from rmapy.api import Client

rmapy_client = Client()
if not rmapy_client.is_auth():
    rmapy_client.register_device(sys.argv[1])
