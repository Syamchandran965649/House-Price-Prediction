from pydantic import BaseModel


class HouseData(BaseModel):
    property_type: int
    location: int
    city: int
    province_name: int
    latitude: float
    longitude: float
    baths: int
    purpose: int
    bedrooms: int
    Area_Type: int
    Area_Size: float
    Area_Category: int