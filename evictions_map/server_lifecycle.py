import numpy as np
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2

import settings
import queries as q
import functions

"""
server_lifecycle.py is a magic filename recognized by the Bokeh server within the bokeh directory, containing
lifecycle hooks. 

In this case, we're using the on_server_loaded() hook to query PostGIS and cache base data for the app in the server_context,
which individual sessions have access to via curdoc().session_context.server_context.

For more, see https://docs.bokeh.org/en/latest/docs/dev_guide/server.html#lifecycle
"""

def on_server_loaded(server_context):
    # ---------------------------------------------------------------#
    # Set up a connection to the postgres server.
    if settings.PGHOST == "" or settings.PGUSER == "":
        print('No connection information found')
        exit(1)

    conn_string = f'host={settings.PGHOST} port=5432 dbname={settings.PGDATABASE} user={settings.PGUSER} password={settings.PGPASSWORD}'
    conn = psycopg2.connect(conn_string)
    print('Connected to Server')
    # create a cursor object
    cursor = conn.cursor()
    # ---------------------------------------------------------------#
    # Load Data using SQL Queries
    rental_units_query = """select data_year as year, rental_units, fips FROM housing.acs_rental_units__blockgroup"""
    blockgroup_query = """select fips, st_astext((ST_Dump(geom)).geom) AS geom, area__sqmi FROM geom.blockgroup"""
    # read queries using database
    evictions_by_month_by_blockgroup = sqlio.read_sql_query(q.evictions_by_month_by_blockgroup_2018_to_present, conn)
    rental_units_by_blockgroup = sqlio.read_sql_query(rental_units_query, conn)
    blockgroup_geometry = sqlio.read_sql_query(blockgroup_query, conn)

    # close connection
    conn = None

    # ---------------------------------------------------------------#

    # ---------------------------------------------------------------#
    # Grab and Convert Coords from Shapefile
    # TODO: Ideally, move this into happening on the PostGIS server, but works for now.
    blockgroup_geometry['geom'] = blockgroup_geometry.geom.apply(functions.makePoly)  # convert string into Polygon object
    blockgroup_geometry['poly_x'] = blockgroup_geometry.apply(functions.getPolyCoords, coord_type='x', axis=1)  # grab x coords
    blockgroup_geometry['poly_y'] = blockgroup_geometry.apply(functions.getPolyCoords, coord_type='y', axis=1)  # grab y coords
    blockgroup_geometry['xs'] = blockgroup_geometry.poly_x.map(functions.conv_poly_xs)  # convert x coords to be usable by Bokeh
    blockgroup_geometry['ys'] = blockgroup_geometry.poly_y.map(functions.conv_poly_ys)  # convert y coords to be usable by Bokeh

    # ---------------------------------------------------------------#
    # Merge Evictions Dataset with Shapefile and Rental Units data

    # TODO: Remove this -- temporary fix b/c 2019 ACS data is not in the DB yet.
    rental_units_by_blockgroup = rental_units_by_blockgroup.append(rental_units_by_blockgroup[rental_units_by_blockgroup['year'] == 2018].replace(2018, 2019))

    # Expand out rental_units_by_blockgroup to have values for each month,year pair.
    months = pd.DataFrame({'month': range(1, 13)})
    months['tempkey'] = 0
    rental_units_by_blockgroup['tempkey'] = 0
    rental_units_by_blockgroup = rental_units_by_blockgroup.merge(months, on='tempkey', how='outer')
    rental_units_by_blockgroup.drop(columns='tempkey')

    evictions_count = rental_units_by_blockgroup.merge(evictions_by_month_by_blockgroup, on=['fips', 'year', 'month'], how='left')
    evictions_count = blockgroup_geometry.merge(evictions_count, on='fips', how='left')

    # Populate evictions per 100 rental units and set NaN values to None
    evictions_count.loc[~(evictions_count['evictions'] >= 0), 'evictions'] = 0  # Set all missing or non-numeric values to 0 for evictions count
    evictions_count['evictions_per_rental_unit'] = evictions_count['evictions'] * 100 / evictions_count['rental_units']
    evictions_count.loc[~(evictions_count['rental_units'] > 0), 'evictions_per_rental_unit'] = None
    server_context.evictions_count = evictions_count
