from google import genai
from fastapi import HTTPException, status
from app.schemas.hint import HintRequest, HintResponse

class HintService:
    def __init__(self, api_key: str):
        self.client = genai.Client(api_key=api_key)
    def generate_hint(self, request: HintRequest) -> HintResponse:
        prompt = f"""
        あなたは競技プログラミングのコーチです。以下の情報をもとに、ヒントを出してください。
        問題ID: {request.problem_id}
        現在のコード: {request.current_code}
        ヒントレベル: {request.level} (1: 解法の方針 / 2: アルゴリズム / 3: コーナーケース / 4: 擬似コード)
        ※注意: レベルに応じたヒントだけを出し、答えそのものの完全なコードは書かないでください。
        """
        try:
            response = self.client.models.generate_content(
                model = "gemini-3.6-flash",
                contents = prompt
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=f"Gemini API の呼び出しに失敗しました: {str(e)}"
            )
            
        return HintResponse(
            problem_id=request.problem_id,
            level=request.level,
            hint=response.text,
            next_level=None if request.level == 4 else request.level + 1
        )