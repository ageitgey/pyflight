"""
Contains the TaxPricing class
which contains information about
the taxes used to calculate the
total tax per ticket.
"""


class TaxPricing(object):
    """The taxes used to calculate the total tax per ticket.

    This extends the information being held in the :class:`Tax` objects.

    This class supports various *magic methods*:

    ``x == y``
        Check if two :class:`TaxPricing` objects are equal.
        Returns ``True`` if ``x.id == y.id``.

    ``x != y``
        Check if two :class:`TaxPricing` objects are equal.
        Returns ``True`` if ``x.id != y.id``.

    ``str(x)``
        Returns the ``id`` of this :class:`TaxPricing`

    Attributes
    ----------
        id : str
            The unique identifier for this tax in a response, which is not
            present for unnamed carrier surcharges. ``None`` if not present.
        charge_type : str
            Specifies the charge type for this :class:`Tax`
            - whether it is a government charge or a carrier surcharge.
        code : str
            The code to enter in the ticket's tax box.
        country : str
            The country issuing the charge, for government charges only.
            ``None`` (Empty string) if not a government charge.
        sale_price : str
            The price of the tax in the sales or equivalent currency.
    """

    def __init__(self, pricing_tax_data: dict):
        """Create a new :class:`TaxPricing` object.

        Args:
            pricing_tax_data : dict
                The ``pricing[].tax[]` data returned from the API.
        """
        self.id = pricing_tax_data.get('id', None)  # pylint: disable=invalid-name
        self.charge_type = pricing_tax_data['chargeType']
        self.code = pricing_tax_data['code']
        self.country = pricing_tax_data.get('country', None)
        self.sale_price = pricing_tax_data['salePrice']

    def __eq__(self, other):
        """Compare two :class:`TaxPricing` objects.

        Returns
        -------
        bool
            True or False depending on the result of the comparison
        """

        return self.id == other.id

    def __str__(self):
        """Get the ``id`` of this :class:`TaxPricing` object.

        Returns
        -------
        str
            The ``id`` of this :class:`TaxPricing`
        """

        return self.id

    def as_dict(self):
        """Get a dictionary representation of this :class:`TaxPricing`

        Returns
        -------
        dict
            A dictionary containing the attributes of this
            :class:`TaxPricing` as key / value pairs.
        """

        return self.__dict__
