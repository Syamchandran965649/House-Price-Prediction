from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource
from feast.types import Int64, Float64

# Entity
property_entity = Entity(
    name="property",
    join_keys=["property_id"],
)

# Source
house_source = FileSource(
    path="../../../data/processed/processed_data.parquet",
    timestamp_field="event_timestamp",
    
)

# Feature View
house_features = FeatureView(
    name="house_features",
    entities=[property_entity],
    ttl=timedelta(days=365),
    schema=[
        Field(name="property_type", dtype=Int64),
        Field(name="location", dtype=Int64),
        Field(name="city", dtype=Int64),
        Field(name="province_name", dtype=Int64),
        Field(name="latitude", dtype=Float64),
        Field(name="longitude", dtype=Float64),
        Field(name="baths", dtype=Int64),
        Field(name="purpose", dtype=Int64),
        Field(name="bedrooms", dtype=Int64),
        Field(name="Area Type", dtype=Int64),
        Field(name="Area Size", dtype=Float64),
        Field(name="Area Category", dtype=Int64),
    ],
    source=house_source,
    online=True,
)