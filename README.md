# pyflight
[![Documentation Status](https://readthedocs.org/projects/pyflight/badge/?version=latest)](http://pyflight.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/Volcyy/pyflight.svg?branch=master)](https://travis-ci.org/Volcyy/pyflight)

A Python Wrapper around the Google QPX Flights API that supports both synchronous and asynchronous operation.

## Features
- Fully asynchronous using `aiohttp`, or synchronous using `requests`.
- Easy control over the formatting of requests and results
- Powerful functions to work with API results

## Installation
```bash
pip3 install pyflight 
```  
A Google API Key is required. You can obtain one at the [Google API Dev Console](https://console.developers.google.com/apis).
   
## Example
**Find flights from San Francisco (SFO) to Los Angeles (LAX), limited to one solution** 

We create a request and set the adult count, then add a slice to send with the request. We execute the API call synchronously 
and specify that we do not want to use the supplied containers and would like to receive the "raw" JSON response 
instead, to write the response to a file using Python's built-in `json` module. Note that asynchronous API calls are designed to be used within
asynchronous applications, thus we use a synchronous request here.
```python
import json
import pyflight

pyflight.set_api_key('<key>')

flight = pyflight.Request()
flight.adult_count = 1

flight.add_slice(pyflight.Slice(
    origin='SFO',
    destination='LAX',
    date='2017-09-19'
))

result = flight.send_sync(use_containers=False)

with open('res.json', 'w+') as f:
    json.dump(result, f)
```

## Dependencies
- Python 3.5+
- aiohttp
- requests


## Tests
If you're interested in running the tests,  run `python3 -m pytest`.
If required files for testing are not found in the directory, they will be downloaded
automatically and saved for the next testing runs.
You can also use the `-v` flag to enable a more detailed overview of the tests.
 
 
## Disclaimer
pyflight is not endorsed by Google and does not reflect the views or opinions of Google.
