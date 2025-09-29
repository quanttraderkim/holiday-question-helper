# 명절 질문 답변 생성기 MCP Server

명절 때 친척들의 부담스러운 질문에 위트있게 답변하는 도구입니다.

## 설치 방법

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

## 실행 방법

```bash
# 개발 서버 실행
fastmcp dev main.py

# 프로덕션 서버 실행
python main.py
```

## 2단계 구현 기능

- ✅ **6개 카테고리** 지원:
  - 결혼 관련 (3개 질문)
  - 육아 관련 (2개 질문)
  - 취업/진로 (2개 질문)
  - 학업 관련 (1개 질문)
  - 외모 관련 (2개 질문)
  - 나이 관련 (2개 질문)

- ✅ **5가지 답변 스타일** (유머러스, 사이다, 정중한 회피, 역공, 현명한)
- ✅ **카테고리 자동 감지** 기능
- ✅ **통합 답변 생성** 함수

## 사용 예시

```python
# 함수: generate_response (모든 카테고리 지원)
# 질문: "애는 언제 낳니?"
# 스타일: "humorous"
# 카테고리: "auto" (자동 감지)
# 결과: 육아 관련 유머러스한 답변 반환

# 함수: list_categories
# 결과: 사용 가능한 모든 카테고리와 스타일 목록 반환
```

## 주의사항

⚠️ 이 도구는 유머를 위한 것입니다. 실제 가족 모임에서는 상황과 관계를 고려해서 적절히 사용하세요.
