from pydantic import BaseModel, Field

class HintRequest(BaseModel):
    problem_id: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="AtCoderの問題ID（例： abc300_c）"
    )
    current_code: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="現在書いているコード"
    )
    level: int = Field(
        ...,
        ge=1,
        le=4,
        description="ヒントのレベル（1:方針、 2:アルゴリズム, 3:コーナーケース, 4:疑似コード"
    )

class HintResponse(BaseModel):
    problem_id: str
    level: int
    hint: str
    next_level: int | None = None