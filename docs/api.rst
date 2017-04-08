.. currentmodule:: pyflight
   
API Reference
=============

This page shows the functions and classes exposed by pyflight.


Basic Configuration
-------------------

.. autofunction:: pyflight.set_api_key

.. autofunction:: pyflight.set_queries_per_day


Making Requests
---------------

.. autofunction:: pyflight.send_async

.. autofunction:: pyflight.send_sync

.. autoclass:: pyflight.APIException


Working with the Response
-------------------------

.. automodule:: pyflight.results

.. autoclass:: pyflight.results.Result
   :members:

.. autoclass:: pyflight.results.FlightData
   :members:

.. autoclass:: pyflight.results.Carrier
   :members:

.. autoclass:: pyflight.results.City
   :members:

.. autoclass:: pyflight.results.Tax
   :members:

.. autoclass:: pyflight.results.Airport
   :members:

.. autoclass:: pyflight.results.Trip
   :members:

.. autoclass:: pyflight.results.Route
   :members:

.. autoclass:: pyflight.results.Segment
   :members:

.. autoclass:: pyflight.results.Flight
   :members:

.. autoclass:: pyflight.results.Pricing
   :members:

.. autoclass:: pyflight.results.Fare
   :members:

.. autoclass:: pyflight.results.SegmentPricing
   :members:

.. autoclass:: pyflight.results.BagDescriptor
   :members:

.. autoclass:: pyflight.results.FreeBaggageOption
   :members:

.. autoclass:: pyflight.results.BagDescriptor
   :members:
