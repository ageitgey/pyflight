"""
This File exposes the Functions offered by the package to ease its usage.
"""
from pyflight.rate_limiter import set_queries_per_day
from pyflight.requester import set_api_key, send_async, send_sync, Request, Slice
from pyflight.api import APIException

__version__ = '0.1.2'
