from feast import FeatureStore

store = FeatureStore(repo_path="feature_store/feature_repo")


def get_features(property_id: int):

    feature_vector = store.get_online_features(
        features=[
            "house_features:property_type",
            "house_features:location",
            "house_features:city",
            "house_features:province_name",
            "house_features:latitude",
            "house_features:longitude",
            "house_features:baths",
            "house_features:purpose",
            "house_features:bedrooms",
            "house_features:area_type",
            "house_features:area_size",
            "house_features:area_category",
        ],
        entity_rows=[
            {
                "property_id": int(property_id)
            }
        ],
    )

    return feature_vector.to_dict()