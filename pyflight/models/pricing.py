"""
Contains the Pricing class,
which is used to represent
information about the pricing
of the route this is stored
in on a per-passenger basis.
"""

from .fare import Fare
from .segment_pricing import SegmentPricing


class Pricing(object):  # pylint: disable=too-many-instance-attributes
    """
    Contains Information about the pricing of the given Route, per passenger.

    Attributes
    ----------
        fares : List[:class:`Fare`]
            A list of :class:`Fare` objects used to price one or more segments.
        segment_pricing : List[:class:`SegmentPricing`]
            A list of :class:`SegmentPricing` objects
            used to price one segment.
        base_fare_total : str
            The total fare in the currency of the country of origin.
            ``None`` when the sales currency and the currency
            of the country of commencement are not different.
        sale_fare_total : str
            The total fare in the sale or equivalent currency.
        sale_tax_total : str
            The taxes in the sale or equivalent currency.
        sale_total : str
            The total per-passenger price (fare + tax)
            in the sale of equivalent currency.
        adults : int
            The amount of passengers that are adults.
        children : int
            The amount of passengers that are children.
        infants_in_lap : int
            The amount of passengers that are infants
            travelling in the lap of an adult.
        infants_in_seat : int
            The amount of passengers that are infants assigned to a seat.
        seniors : int
            The amount of passengers that are senior citizens.
        fare_calculation : str
            The horizontal fare calculation. On a ticket,
            this is a field that displays all of the relevant
            items that go into the calculation of the fare.
        latest_ticketing_time : str
            The latest ticketing time for this pricing assuming
            there is no change in fares / rules
            and the reservation occurs at ticketing time.
        for_passenger_type : str
            Specifies the passenger type code for this pricing,
            used by a carrier to restrict fares to certain categories
            of passengers (for example, a fare might be valid only
            for senior citizens).
        refundable : bool
            Specifies whether the fares on this pricing are refundable.
            If the API does not specify this explicitly in the response,
            it defaults to ``None``.

    """

    def __init__(self, pricing_data: dict):
        """
        Create a new Pricing object from fare data.

        Parameters
        ----------
            pricing_data : dict
                The Pricing Data Object as returned from the API in an Array
        """

        self.fares = [Fare(f) for f in pricing_data['fare']]

        self.segment_pricing = [
            SegmentPricing(sp) for sp in pricing_data['segmentPricing']
        ]

        self.base_fare_total = pricing_data.get('baseFareTotal')
        self.sale_fare_total = pricing_data['saleFareTotal']
        self.sale_tax_total = pricing_data['saleTaxTotal']
        self.sale_total = pricing_data['saleTotal']
        self.adults = pricing_data['passengers'].get('adultCount', 0)
        self.children = pricing_data['passengers'].get('childCount', 0)
        self.infants_in_lap = pricing_data['passengers'].get(
            'infantInLapCount', 0)
        self.infants_in_seat = pricing_data['passengers'].get(
            'infantInSeatCount', 0)
        self.seniors = pricing_data['passengers'].get('seniorCount', 0)
        self.fare_calculation = pricing_data['fareCalculation']
        self.latest_ticketing_time = pricing_data['latestTicketingTime']
        self.for_passenger_type = pricing_data['ptc']
        self.refundable = pricing_data.get('refundable', None)

    def as_dict(self):
        """Get a dictionary representing this :class:`Pricing`.

        Returns
        -------
        dict
            A dictionary containing the attributes of this
            :class:`Pricing` as key / value pairs.
        """

        return {
            'fares': [f.as_dict() for f in self.fares],
            'segment_pricing': [sp.as_dict() for sp in self.segment_pricing],
            'base_fare_total': self.base_fare_total,
            'sale_fare_total': self.sale_fare_total,
            'sale_tax_total': self.sale_tax_total,
            'sale_total': self.sale_total,
            'adults': self.adults,
            'children': self.children,
            'infants_in_lap': self.infants_in_lap,
            'infants_in_seat': self.infants_in_seat,
            'seniors': self.seniors,
            'fare_calculation': self.fare_calculation,
            'latest_ticketing_time': self.latest_ticketing_time,
            'for_passenger_type': self.for_passenger_type,
            'refundable': self.refundable
        }
