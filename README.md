# AtCoder Hint API
競技プログラミングAtCoderで詰まった際に、Gemini APIを使って段階的なヒント（方針/アルゴリズム/コーナーケース/疑似コード）を返すFastAPIベースのWeb API。

## 技術スタック
- Python 3.11 / FastAPI / Pydantic
- Google GenAI SDK (Gemini)
- Docker / Docker Compose
- pytest / httpx

## 起動方法
- .env.exampleをコピーして.envを作成し、GEMINI_API_KEYを設定
- docker compose upで起動
- http://localhost:8000/docs で Swagger UI を確認

## テスト実行方法
- pytestコマンドでモックを使った自動テストが走る