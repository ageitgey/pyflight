# pyflight
[![Documentation Status](https://readthedocs.org/projects/pyflight/badge/?version=latest)](http://pyflight.readthedocs.io/en/latest/?badge=latest)

A Python Wrapper around the Google QPX Flights API that supports both synchronous and asynchronous operation.

## Features
- Fully asynchronous using aiohttp 2.0, or non-async using `requests`.
- Automatic saving of results in useful structures which provide easy-to-use interfaces
- Rate Limiting to your liking

## Installation
```bash
pip3 install pyflight 
python3 -m pip install pyflight

# Up-to-date version from GitHub (currently recommended):
python3 -m pip install -U git+https://github.com/Volcyy/pyflight
```  
   
## Example
**Find flights from San Francisco (SFO) to Los Angeles (LAX), limited to one solution** 

The rate limiting call is omitted here, but we keep it in mind for now. We send a request structured as
described [here](https://developers.google.com/qpx-express/v1/trips/search). We execute the API call synchronously 
and specify that we do not want to use the supplied containers and would like to receive the "raw" JSON response 
instead, to write the response to a file using Python's built-in `json` module.
To execute this call asynchronously, simply replace `send_sync` with `send_async` and 
`await` it like any coroutine. Note that asynchronous API calls are designed to be used within
asynchronous applications.
```python
import json
import pyflight

pyflight.set_api_key('<key>')
# pyflight.set_queries_per_day(<my-limit>)

flight = pyflight.Request()
flight.adult_count = 1

flight.add_slice(pyflight.Slice(
    origin='SFO',
    destination='LAX',
    date='2017-09-19'
))

with open('res.json', 'w+') as f:
    json.dump(flight.send_sync(use_containers=False), f)
```

## Dependencies
- Python 3.5+
- aiohttp
- requests


## Tests
If you're interested in running the tests, download the two example responses given on the bottom of 
[this page](https://developers.google.com/qpx-express/v1/requests) and save them in the `tests` directory named
`response_1.json` and `response_2.json`. Afterwards, from the root directory, run `python3 -m pytest tests/`. 
You can also use the `-v` flag to enable a more detailed overview of the tests.
 
 
## Disclaimer
pyflight is not endorsed by Google and does not reflect the views or opinions of Google.