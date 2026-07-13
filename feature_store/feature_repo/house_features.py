from datetime import timedelta

from feast import Entity, FeatureView, FileSource, Field
from feast.types import Int64, Float32
from feast.value_type import ValueType

# ----------------------------
# Entity
# ----------------------------
property_entity = Entity(
    name="property",
    join_keys=["property_id"],
    value_type=ValueType.INT64,
)

# ----------------------------
# Data Source
# ----------------------------
house_source = FileSource(
    path="data/house_features.parquet",
    timestamp_field="event_timestamp",
)

# ----------------------------
# Feature View
# ----------------------------
house_features = FeatureView(
    name="house_features",
    entities=[property_entity],
    ttl=timedelta(days=365),

    schema=[
        Field(name="property_type", dtype=Int64),
        Field(name="location", dtype=Int64),
        Field(name="city", dtype=Int64),
        Field(name="province_name", dtype=Int64),
        Field(name="latitude", dtype=Float32),
        Field(name="longitude", dtype=Float32),
        Field(name="baths", dtype=Int64),
        Field(name="purpose", dtype=Int64),
        Field(name="bedrooms", dtype=Int64),
        Field(name="area_type", dtype=Int64),
        Field(name="area_size", dtype=Float32),
        Field(name="area_category", dtype=Int64),
    ],

    source=house_source,
)