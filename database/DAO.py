from database.DB_connect import DBConnect
from model.airport import Airport
from model.flight import Flight


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def get_all_flights():
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        result = []

        query = """select *
                from extflightdelays.flights f 
                """
        cursor.execute(query)
        for row in cursor:
            result.append(Flight(row['ID'],
                                 row['AIRLINE_ID'],
                                 row['FLIGHT_NUMBER'],
                                 row['TAIL_NUMBER'],
                                 row['ORIGIN_AIRPORT_ID'],
                                 row['DESTINATION_AIRPORT_ID'],
                                 row['SCHEDULED_DEPARTURE_DATE'],
                                 row['DEPARTURE_DELAY'],
                                 row['ELAPSED_TIME'],
                                 row['DISTANCE'],
                                 row['ARRIVAL_DATE'],
                                 row['ARRIVAL_DELAY']))

        cursor.close()
        connection.close()

        return result


    @staticmethod
    def get_flights_with_distance(min_distance):
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        result = []

        query = """select *
            from extflightdelays.flights f 
            where DISTANCE > %s"""
        cursor.execute(query, (min_distance,))
        for row in cursor:
            result.append(Flight(row['ID'],
                                 row['AIRLINE_ID'],
                                 row['FLIGHT_NUMBER'],
                                 row['TAIL_NUMBER'],
                                 row['ORIGIN_AIRPORT_ID'],
                                 row['DESTINATION_AIRPORT_ID'],
                                 row['SCHEDULED_DEPARTURE_DATE'],
                                 row['DEPARTURE_DELAY'],
                                 row['ELAPSED_TIME'],
                                 row['DISTANCE'],
                                 row['ARRIVAL_DATE'],
                                 row['ARRIVAL_DELAY']))

        cursor.close()
        connection.close()

        return result

    @staticmethod
    def get_all_airport():
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        result = []

        query = """select *
                    from extflightdelays.airports a """
        cursor.execute(query)
        for row in cursor:
            result.append(Airport(row['ID'],
                                  row['AIRPORT'],
                                  row['CITY'],
                                  row['STATE'],
                                  row['COUNTRY']
                                  ))

        cursor.close()
        connection.close()

        return result

    @staticmethod
    def get_all_distance():
        connection = DBConnect.get_connection()
        cursor = connection.cursor(dictionary=True)

        result = {}

        query = """ select avg(f.DISTANCE), f.ORIGIN_AIRPORT_ID , f.DESTINATION_AIRPORT_ID
                    from flights f
                    group by f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID 
                    """
        cursor.execute(query)
        for row in cursor:
            result[(row['ORIGIN_AIRPORT_ID'], row['DESTINATION_AIRPORT_ID'])] = row['avg(f.DISTANCE)']

        cursor.close()
        connection.close()

        return result


