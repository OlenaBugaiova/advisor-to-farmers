from typing import Literal
from pydantic import Field, BaseModel, field_validator


class DataFormat(BaseModel):

    question: str = Field(description="Et spesifikt spørsmål om landbruk som en bonde ville stilt")
    answer: str = Field(description="Et fullstendig svar")
    
    difficulty: Literal["nybegynner", "mellomnivå", "avansert"] = Field(
        description="Vanskelighetsgrad som kreves for et svar"
    )
    citations: list[str] = Field(description="Kildesitater fra dokumentet")