import numpy as np
import pandas as pd
import pandas.io.sql as sqlio
import psycopg2
from bokeh.models import ColumnDataSource

import settings
import queries as q
import functions


def on_server_loaded(server_context):
    # ---------------------------------------------------------------#
    # Set up a connection to the postgres server.
    if settings.PGHOST == "" or settings.PGUSER == "":
        print('No connection information found')
        exit(1)

    conn_string = 'host=' + settings.PGHOST + ' port=' + '5432' + ' dbname=' + settings.PGDATABASE + ' user=' + settings.PGUSER + ' password=' + settings.PGPASSWORD
    conn = psycopg2.connect(conn_string)
    print('Connected to Server')
    # create a cursor object
    cursor = conn.cursor()
    # ---------------------------------------------------------------#
    # Load Data using SQL Queries
    ebm_2018_2019 = q.ebm_2018oct_2019oct
    rental_units = """select CAST(geoid10 as NUMERIC) as fips, acs16_rent as rental_units, acs16_tota as total_units FROM staging.evictions_per_bg"""
    blockgroup = """select fips, st_astext((ST_Dump(geom)).geom) AS geom, area__sqmi FROM geom.blockgroup"""
    # read queries using database
    df_blockg_m = sqlio.read_sql_query(ebm_2018_2019, conn)
    df_rental = sqlio.read_sql_query(rental_units, conn)
    gdf_bg = sqlio.read_sql_query(blockgroup, conn)

    # close connection
    conn = None
    # ---------------------------------------------------------------#
    # Manipulate Data for Plotting
    df_rental['rental_units'] = df_rental['rental_units'].replace([0, 0, 0, 0], [33.0, None, None, None])
    # Convert FIPS column into INT
    df_blockg_m['fips'] = df_blockg_m['fips'].astype(np.int64)
    gdf_bg['fips'] = pd.to_numeric(gdf_bg.fips)
    # ---------------------------------------------------------------#
    # Grab and Convert Coords from Shapefile
    gdf_bg['geom'] = gdf_bg.geom.apply(functions.makePoly)  # convert string into Polygon object
    gdf_bg['poly_x'] = gdf_bg.apply(functions.getPolyCoords, coord_type='x', axis=1)  # grab x coords
    gdf_bg['poly_y'] = gdf_bg.apply(functions.getPolyCoords, coord_type='y', axis=1)  # grab y coords
    gdf_bg['xs'] = gdf_bg.poly_x.map(functions.conv_poly_xs)  # convert x coords to be usable by Bokeh
    gdf_bg['ys'] = gdf_bg.poly_y.map(functions.conv_poly_ys)  # convert y coords to be usable by Bokeh

    # ---------------------------------------------------------------#
    # Merge Evictions Dataset with Shapefile
    mdf3 = gdf_bg.merge(df_blockg_m, right_on='fips', left_on='fips', how='outer')
    mdf3 = df_rental.merge(mdf3, right_on='fips', left_on='fips', how='outer')
    server_context.mdf3 = mdf3
