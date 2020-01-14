#################################################################
# Functions

def makePoly(row):
    import shapely.wkt
    return shapely.wkt.loads(row)


def getPolyCoords(row, coord_type, geom="geom"):
    exterior = row[geom].exterior
    if coord_type == "x":
        return list(exterior.coords.xy[0])
    if coord_type == "y":
        return list(exterior.coords.xy[1])


def conv_poly_ys(row):
    import math
    r = 6378137.0
    return [math.log(math.tan(math.pi / 4 + math.radians(x) / 2)) * r for x in row]


def conv_poly_xs(row):
    import math
    r = 6378137.0
    return [math.radians(x) * r for x in row]
