import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._list_airport = DAO.get_all_airport()
        self._idAirport = {}
        self.popolaAirport()
        self._list_flight = DAO.get_all_flights()
        self._list_flight_selected = None
        self._distanceMap = DAO.get_all_distance()

        self._graph = nx.Graph()


    def popolaAirport(self):
        for airport in self._list_airport:
            self._idAirport[airport._id] = airport

    def popolaFlight(self, min_distance):
        #self._list_flight_selected = DAO.get_flights_with_distance(min_distance)
        self.buildGrapgh(min_distance)

    def buildGrapgh(self, min_distance):
        for airport in self._list_airport:
            self._graph.add_node(airport)
        for flight in self._list_flight:
            airport_departure = self._idAirport[flight._origin_airport_id]
            airport_arrival = self._idAirport[flight._destination_airport_id]
            if self._distanceMap[airport_departure._id, airport_arrival._id] > min_distance:
                print(flight)
                self._graph.add_edge(airport_arrival, airport_departure,
                                     data=flight,
                                     weight=self._distanceMap[airport_departure._id,
                                                                airport_arrival._id])


    # Useless
    def get_avg_distance(self, departure, arrival):
        distanza_tot = 0
        num_voli = 0
        for flight in self._list_flight:
            if (flight._origin_airport_id == departure._id and
                    flight._destination_airport_id == arrival._id):
                distanza_tot += flight._distance
                num_voli += 1

        if num_voli == 0:
            media = 0
        else:
            media = distanza_tot / num_voli

        return media
