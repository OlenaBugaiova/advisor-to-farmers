from typing import Literal
import re

from pydantic import Field, BaseModel, field_validator

PHONE_REGEX = r'^((0047)?|(\+47)?|(47)?)[\s]?[2-9]\d{7,8}$'
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
NO_URL_PATTERN = r'^(?i).*(https?://|www\.)'


class DataFormat(BaseModel):
    
    question: str = Field(description="Et spesifikt spørsmål om landbruk som en bonde ville stilt")
    answer: str = Field(description="Et fullstendig og nøyaktig svar")
    citations: list[str] = Field(description="Kildesitater fra dokumentet")

    
    @field_validator('question')
    @classmethod
    def validate_question(cls, v: str) -> str:
        words_to_check = [
            'nibio', 'nlr', 'plantevernleksikonet']
        
        for keyword in words_to_check:
            if keyword in v.lower():
                raise ValueError(f"Spørsmålet kan ikke nevnes '{keyword}'. Vennligst omformuler.")
        
        if re.search(PHONE_REGEX, v):
            raise ValueError('Spørsmålet kan ikke inneholder et telefonnummer')
            
        if re.search(EMAIL_REGEX, v):
            raise ValueError('Spørsmålet kan ikke inneholder en e-postadresse')
            
        if re.search(NO_URL_PATTERN, v):
            raise ValueError('Spørsmålet kan ikke inneholde hyperlenker eller URL-er.')
        
        return v
    
    
    @field_validator('answer')
    @classmethod
    def validate_answer(cls, v: str) -> str:
        words_to_check = [
            'nibio', 'nlr', 'plantevernleksikonet']
        
        for keyword in words_to_check:
            if keyword in v.lower():
                raise ValueError(f"Svaret kan ikke nevnes '{keyword}'. Vennligst omformuler.")
        
        if re.search(PHONE_REGEX, v):
            raise ValueError('Svaret kan ikke inneholder et telefonnummer')
            
        if re.search(EMAIL_REGEX, v):
            raise ValueError('Svaret kan ikke inneholder en e-postadresse')
            
        if re.search(NO_URL_PATTERN, v):
            raise ValueError('Svaret kan ikke inneholde hyperlenker eller URL-er.')
            
        return v