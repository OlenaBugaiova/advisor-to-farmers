from typing import Literal

from pydantic import Field, BaseModel, field_validator


class DataFormat(BaseModel):

    question: str = Field(description="Et spesifikt spørsmål om landbruk som en bonde ville stilt")
    answer: str = Field(description="Et fullstendig og nøyaktig svar")
    
    difficulty: Literal["nybegynner", "mellomnivå", "avansert"] = Field(
        description="Vanskelighetsgrad som kreves for et svar"
    )
    citations: list[str] = Field(description="Kildesitater fra dokumentet")
    
    @field_validator('question')
    def question_cannot_mention_resources(cls, generated_text: str) -> str:
        forbidden_keywords = [
            'kildene', 'documentene', 'teksten', 'nibio', 'nlr', 'plantevernleksikonet']
        
        # Check if any forbidden keyword is in the question
        for keyword in forbidden_keywords:
            if keyword in generated_text.lower():
                raise ValueError(f"Spørsmålet kan ikke nevnes '{keyword}'. Vennligst omformuler.")
        
        return generated_text
    
    
    @field_validator('answer')
    def answer_cannot_mention_resources(cls, generated_text: str) -> str:
        forbidden_keywords = [
            'kildene', 'documentene', 'teksten', 'nibio', 'nlr', 'plantevernleksikonet']
        
        # Check if any forbidden keyword is in the answer
        for keyword in forbidden_keywords:
            if keyword in generated_text.lower():
                raise ValueError(f"Svaret kan ikke nevnes '{keyword}'. Vennligst omformuler.")
        
        return generated_text