from typing import Literal
import re

from pydantic import Field, BaseModel, field_validator

PHONE_REGEX = r'^((0047)?|(\+47)?|(47)?)[\s]?[2-9]\d{7,8}$'
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
NO_URL_PATTERN = r'^(?i).*(https?://|www\.)'


class QuestionRow(BaseModel):

    thought_process: str = Field(description="Begrunnelse for å velge dette spørsmålet og praktisk fordel for bønder")
    question: str = Field(description="Et spesifikt spørsmål om landbruk som en bonde ville stilt")
    answer: str = Field(description="Et fullstendig og nøyaktig svar")
    
    difficulty: Literal["nybegynner", "mellomnivå", "avansert"] = Field(
        description="Vanskelighetsgrad som kreves for et svar"
    )
    citations: list[str] = Field(description="Kildesitater fra dokumentet")
    
    @field_validator('question')
    def question_cannot_mention_resources_and_personal_data(cls, generated_text: str) -> str:
        forbidden_keywords = [
            'kildene', 'documentene', 'teksten', 'nibio', 'nlr', 'plantevernleksikonet']
        
        # Check if any forbidden keyword is in the question
        for keyword in forbidden_keywords:
            if keyword in generated_text.lower():
                raise ValueError(f"Spørsmålet kan ikke nevnes '{keyword}'. Vennligst omformuler.")
        
        if re.search(PHONE_REGEX, generated_text):
            raise ValueError('Spørsmålet kan ikke inneholder et telefonnummer')
            
        if re.search(EMAIL_REGEX, generated_text):
            raise ValueError('Spørsmålet kan ikke inneholder en e-postadresse')
            
        if re.search(NO_URL_PATTERN, generated_text):
            raise ValueError('Spørsmålet kan ikke inneholde hyperlenker eller URL-er.')
        
        return generated_text
    
    
    @field_validator('answer')
    def answer_cannot_mention_resources_and_personal_data(cls, generated_text: str) -> str:
        forbidden_keywords = [
            'kildene', 'documentene', 'teksten', 'nibio', 'nlr', 'plantevernleksikonet']
        
        # Check if any forbidden keyword is in the answer
        for keyword in forbidden_keywords:
            if keyword in generated_text.lower():
                raise ValueError(f"Svaret kan ikke nevnes '{keyword}'. Vennligst omformuler.")
        
        if re.search(PHONE_REGEX, generated_text):
            raise ValueError('Svaret kan ikke inneholder et telefonnummer')
            
        if re.search(EMAIL_REGEX, generated_text):
            raise ValueError('Svaret kan ikke inneholder en e-postadresse')
            
        if re.search(NO_URL_PATTERN, generated_text):
            raise ValueError('Svaret kan ikke inneholde hyperlenker eller URL-er.')
            
        return generated_text