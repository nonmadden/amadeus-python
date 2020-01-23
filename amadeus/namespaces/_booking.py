from amadeus.booking._flight_orders import FlightOrders
from amadeus.booking._flight_order import FlightOrder
from amadeus.client.decorator import Decorator


class Booking(Decorator, object):
    def __init__(self, client):
        Decorator.__init__(self, client)
        self.flight_orders = FlightOrders(client)

    def flight_order(self, flight_order_id):
        return FlightOrder(self.client, flight_order_id)


__all__ = ['FlightOrders', 'FlightOrder']