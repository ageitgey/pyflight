.. currentmodule:: pyflight
   
API Reference
=============

This page shows the functions and classes exposed by pyflight.
A lot of attributes wrap the required parameters for the QPX API and thus result in documentation similiar to the one
found on `the official QPX Express API reference <https://developers.google.com/qpx-express/v1/trips/search>`_, licensed
under the `Creative Commons Attribution 3.0 License <https://creativecommons.org/licenses/by/3.0/>`_.


Basic Configuration
-------------------

.. autofunction:: pyflight.set_api_key

.. autofunction:: pyflight.set_queries_per_day


Making Requests
---------------

.. autoclass:: pyflight.Request
   :members:

.. autoclass:: pyflight.Slice
   :members:

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
