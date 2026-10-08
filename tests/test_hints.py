from fastapi.testclient import TestClient
from main import app
from app.schemas.hint import HintRequest, HintResponse
from app.api.v1.hints import get_hint_service

client = TestClient(app)

def test_generate_hint_validation_error():
    response = client.post(
        "/api/v1/hints",
        json={
            "problem_id": "abc300_c",
            "current_code": "print('hello')",
            "level": 5  
        }
    )

    assert response.status_code == 422

class MockHintService:
    def generate_hint(self, request: HintRequest) -> HintResponse:
        return HintResponse(
            problem_id=request.problem_id,
            level=request.level,
            hint="これはテスト用ヒントです",
            next_level=None if request.level == 4 else request.level + 1
        )  

def test_generate_hint_service():
    app.dependency_overrides[get_hint_service] = lambda: MockHintService()
    try:
        response = client.post(
            "/api/v1/hints",
            json={
                "problem_id": "abc300_c",
                "current_code": "print('test')",
                "level": 1
            }
        )

        assert response.status_code == 200
        data = response.json()
        assert data["hint"] == "これはテスト用ヒントです"
        assert data["next_level"] == 2

    finally:
        app.dependency_overrides.clear()