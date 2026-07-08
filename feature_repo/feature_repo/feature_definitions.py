from feast import FeatureView, FileSource, Field
from feast.types import Float32
from datetime import timedelta


house_source = FileSource(
    path="data/features.parquet",
    timestamp_field="event_timestamp"
)


house_features = FeatureView(
    name="house_features",
    entities=[],
    ttl=timedelta(days=365),
    schema=[
        Field(
            name="feature_name",
            dtype=Float32
        ),
    ],
    source=house_source,
)