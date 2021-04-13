
# Intersection Module for InnoPart API

# Purpose
# -------
# Calculating the intersection(s) of a given line feature or arc feature received by the client.
# In case of a arc it has to be sampled into line features before the calculations

from geoms import Point2D, Arc2D
import geopandas as gpd
from shapely.geometry import LineString

# Testdata represemting the relevant line geometries to be checked for intersections
df = gpd.GeoDataFrame({
    'id'      : ['1', '2'],
    'geom'    : [   LineString([(0,0), (1,0), (1,1), (2,1)]),
                    LineString([(2,3), (2,4), (3,2), (1,5)])
                ] 
})

section_geom    = LineString([(-1,-1), (5, 5)])
section_id      = 12231


"""
    Checking for type of section (Arc or LineSegment)
    ---> Arc needs to be sampled before
"""


def intersections(section_geom, section_id, features):

    # Creating empty geodataframe 
    intersections = gpd.GeoDataFrame({
    'feature_id'   : [],
    'section_id'    : [],   
    'geometry'      : []
    })

    # Checking for intersections
    for index, data in df.iterrows():
        feature = data['geom']

        # Appending intersections to gdf if intersection is found
        if feature.intersects(section_geom):
            intersections = intersections.append({'feature_id' : data['id'], 'section_id' : section_id, 'geometry' : feature.intersection(section_geom)}, ignore_index=True)


    if not intersections.empty:
        return intersections
    else:
        return None 




print(intersections(section_geom, section_id, df))