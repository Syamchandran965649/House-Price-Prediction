from datetime import timedelta

from feast import Entity, FeatureView, Field, FileSource, FeatureService
from feast.types import String, Float32, Int64

# -------------------------
# Entity
# -------------------------
property_entity = Entity(
    name="property",
    join_keys=["property_id"],
)

# -------------------------
# Data Source
# -------------------------
house_source = FileSource(
    name="house_source",
    path="data/house_features.parquet",
    timestamp_field="event_timestamp",
)

# -------------------------
# Feature View
# -------------------------
house_features = FeatureView(
    name="house_features",
    entities=[property_entity],
    ttl=timedelta(days=365),
    schema=[
        Field(name="property_type", dtype=String),
        Field(name="location", dtype=String),
        Field(name="city", dtype=String),
        Field(name="province_name", dtype=String),
        Field(name="latitude", dtype=Float32),
        Field(name="longitude", dtype=Float32),
        Field(name="baths", dtype=Int64),
        Field(name="purpose", dtype=String),
        Field(name="bedrooms", dtype=Int64),
        Field(name="Area Type", dtype=String),
        Field(name="Area Size", dtype=Float32),
        Field(name="Area Category", dtype=String),
    ],
    online=True,
    source=house_source,
)

# -------------------------
# Feature Service
# -------------------------
house_feature_service = FeatureService(
    name="house_feature_service",
    features=[house_features],
)