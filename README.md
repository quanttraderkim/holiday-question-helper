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

## 구현된 기능

### 기본 기능
- ✅ 6개 질문 카테고리 (결혼, 육아, 취업, 학업, 외모, 나이)
- ✅ 5가지 답변 스타일 (유머러스, 사이다, 정중한 회피, 역공, 현명한)
- ✅ 카테고리 자동 감지

### 고급 기능 (3단계)
- ✅ 사용자 상황 맞춤형 답변 (나이, 직업, 결혼여부 반영)
- ✅ 복수 스타일 답변 동시 생성
- ✅ 유사 질문 추천
- ✅ 예시 질문 조회

## 사용 예시

### 기본 답변 생성
```python
generate_response(
    question="결혼은 언제 하니?",
    style="humorous"
)
```

### 맞춤형 답변 생성
```python
generate_custom_response(
    question="취업은 했니?",
    style="polite",
    age=25,
    job="취준생"
)
```

### 여러 스타일 한 번에
```python
generate_multiple_responses(
    question="살 찐 것 같은데?",
    styles="humorous,witty,polite"
)
```

### 예시 질문 조회
```python
get_question_examples()
```

## 주의사항

⚠️ 이 도구는 유머를 위한 것입니다. 실제 가족 모임에서는 상황과 관계를 고려해서 적절히 사용하세요.
