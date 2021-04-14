
# Intersection Module for InnoPart API

# Purpose
# -------
# Calculating the intersection(s) of a given line feature or arc feature received by the client.
# In case of a arc it has to be sampled into line features before the calculations

from geoms import Point2D, Arc2D
import geopandas as gpd
from shapely.geometry import LineString


def intersections(section:Section,  features:GeoDataFrame):

    # Checking for if section is arc or line
    if section.is_arc:
        section_geom = Arc2D( Point2d(section.startpoint.x, section.startpoint.y), Point2d(section.endpoint.x, section.endpoint.y), Point2d(section.controlpoint.x, section.controlpoint.y), section.height).sample()
    else:
        section_geom = LineString([(self.startpoint.x, self.startpoint.y), (self.endpoint.x, self.endpoint.y)])
    
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