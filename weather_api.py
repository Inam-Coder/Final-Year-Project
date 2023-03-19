"""Weather_api script get the data of astronomy from weather api and save the
final result into db. After saving recoreds in db it runs the downstream store procedures
to populate warehouse tables."""

from __future__ import print_function
import datetime
import swagger_client
from swagger_client.rest import ApiException
import psycopg2
import psycopg2.extras as psyex


def get_astronomy_data(cities: list, date: str = "2023-01-02") -> list:
    """This function return astronomy data of cities provided in parameter."""

    # Configure API key authorization: ApiKeyAuth
    configuration = swagger_client.Configuration()
    configuration.api_key['key'] = '09a60917fc2349a3bb2224747230102'

    # create an instance of the API class
    api_instance = swagger_client.APIsApi(
        swagger_client.ApiClient(configuration))

    objects = []
    for city in cities:
        query = city
        try:
            # Astronomy API
            api_response = api_instance.astronomy(query, date)
            objects.append(api_response.__dict__)

        except ApiException as error:
            print(f"""Exception when calling APIsApi->astronomy: {error}\n""")

    return objects


def format_tuple(api_data: list):
    """Formating the data object for psycopg2 function to inserting the rows into db"""
    data_tuples = []

    for data in api_data:
        location_obj = data['_location'].__dict__
        astronomy_obj = data['_astronomy'].__dict__
        astronomy_astro_obj = astronomy_obj['_astro'].__dict__

        row = (location_obj['_name'], location_obj['_region'],
               location_obj['_tz_id'], location_obj['_country'], location_obj['_localtime'],
               astronomy_astro_obj['_moon_illumination'], astronomy_astro_obj['_moon_phase'],
               location_obj['_lat'], astronomy_astro_obj['_moonrise'],
               astronomy_astro_obj['_moonset'], astronomy_astro_obj['_sunrise'], astronomy_astro_obj['_sunset']
               )
        data_tuples.append(row)

    return tuple(data_tuples)


def make_db_call(data_tuples):
    """todoo"""

    # Connect to your postgres DB
    conn = psycopg2.connect(
        """dbname=postgres user=inam_admin host=postgres22.postgres.database.azure.com
        port=5432 password=postgres_24_FEB_23@""")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    psyex.execute_values(cur, """INSERT INTO raw_astronomy (city_name,region,tz_id,country,
    local_time,moon_illumination,moon_phase,lat,
    moonrise,moonset,sunrise,sunset) VALUES %s""", data_tuples)

    # Execute a query
    cur.execute("SELECT * FROM raw_astronomy limit 10")
    # conn.commit()
    # Retrieve query results
    records = cur.fetchall()
    print(records)

    cur.execute(""" call raw_clean_astronomy_sp();
                    call dim_country_sp();
                    call dim_city_sp();
                    call dim_date_sp();
                    call fact_astronomy_sp();""")
    conn.commit()
    conn.close()


# UK and France city names:
uk_cities = ["London", "Bristol", "Manchester",
             "Liverpool", "Birmingham", "Oxford", "Edinburgh", "Paris", "Marseille", "Nice"]


utc_time = datetime.datetime.utcnow()
current_utc_date = utc_time.strftime('%Y-%m-%d')


data_object = get_astronomy_data(uk_cities, current_utc_date)
print(data_object)
##data_tuple = format_tuple(data_object)
##make_db_call(data_tuple)
