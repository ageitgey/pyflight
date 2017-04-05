# pyflight
An asynchronous Python Wrapper around the Google QPX Flights API.

### Features
- Fully asynchronous using aiohttp 2.0, or non-async using `requests`.
- Automatic saving of results in useful structures which provide easy-to-use interfaces
- Rate Limiting to your liking

### Dependencies
- Python 3.6
- aiohttp
- requests

### Tests
If you're interested in running the tests, download the two example responses given on the bottom of 
[this page](https://developers.google.com/qpx-express/v1/requests) and save them in the `tests` directory named
`response_1.json` and `response_2.json`. Afterwards, from the root directory, run `python3 -m pytest tests/`. 
You can also use the `-v` flag to enable a more detailed overview of the tests.
 
 
### Disclaimer
pyflight is not endorsed by Google and does not reflect the views or opinions of Google.