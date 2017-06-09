import pyflight
import json

pyflight.set_api_key('<api-key>')

# Create a new request and set passenger counts
req = pyflight.Request()
req.adult_count = 2

# Add a Slice for a flight from Frankfurt to Lanzarote
req.add_slice(pyflight.Slice(
    origin='FRA',
    destination='ACE',
    date='2017-10-07'
))

# Send the request synchronously
result = req.send_sync()


with open('result.json', 'w+') as f:
    json.dump(result.as_dict(), f, sort_keys=True, indent=2)
