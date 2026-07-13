from pydantic import BaseModel

class PredictionResponse(BaseModel):
    property_id: int
    predicted_price: float