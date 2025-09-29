#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
전체 기능 통합 테스트 스크립트
"""

import sys
from responses import (
    detect_category,
    get_all_response,
    customize_response,
    get_similar_questions,
    get_all_question_examples,
    ALL_RESPONSES,
    QUESTION_CATEGORIES,
    RESPONSE_STYLES
)

def test_all_functions():
    """모든 함수 테스트"""
    print("=" * 60)
    print("명절 질문 답변 생성기 - 전체 기능 테스트")
    print("=" * 60)
    
    tests_passed = 0
    tests_failed = 0
    
    # 테스트 1: 카테고리 감지
    print("\n[테스트 1] 카테고리 자동 감지")
    try:
        category = detect_category("결혼은 언제 하니?")
        assert category == "marriage"
        print("✅ 통과")
        tests_passed += 1
    except Exception as e:
        print(f"❌ 실패: {e}")
        tests_failed += 1
    
    # 테스트 2: 답변 생성
    print("\n[테스트 2] 답변 생성")
    try:
        response = get_all_response("marriage", "결혼은 언제 하니?", "humorous")
        assert response and len(response) > 0
        print("✅ 통과")
        tests_passed += 1
    except Exception as e:
        print(f"❌ 실패: {e}")
        tests_failed += 1
    
    # 테스트 3: 답변 커스터마이징
    print("\n[테스트 3] 답변 커스터마이징")
    try:
        base_response = "결혼은 준비 중입니다."
        user_situation = {"age": 25, "job": "학생"}
        customized = customize_response(base_response, user_situation)
        assert customized is not None
        print("✅ 통과")
        tests_passed += 1
    except Exception as e:
        print(f"❌ 실패: {e}")
        tests_failed += 1
    
    # 테스트 4: 유사 질문 추천
    print("\n[테스트 4] 유사 질문 추천")
    try:
        similar = get_similar_questions("marriage", "결혼은 언제 하니?")
        assert isinstance(similar, list)
        print("✅ 통과")
        tests_passed += 1
    except Exception as e:
        print(f"❌ 실패: {e}")
        tests_failed += 1
    
    # 테스트 5: 예시 질문 조회
    print("\n[테스트 5] 예시 질문 조회")
    try:
        examples = get_all_question_examples()
        assert isinstance(examples, dict)
        assert len(examples) > 0
        print("✅ 통과")
        tests_passed += 1
    except Exception as e:
        print(f"❌ 실패: {e}")
        tests_failed += 1
    
    # 테스트 6: 데이터 무결성
    print("\n[테스트 6] 데이터 무결성 검증")
    try:
        assert len(QUESTION_CATEGORIES) == 6
        assert len(RESPONSE_STYLES) == 5
        assert len(ALL_RESPONSES) == 6
        print("✅ 통과")
        tests_passed += 1
    except Exception as e:
        print(f"❌ 실패: {e}")
        tests_failed += 1
    
    # 결과 요약
    print("\n" + "=" * 60)
    print(f"테스트 결과: {tests_passed}개 통과, {tests_failed}개 실패")
    print("=" * 60)
    
    return tests_failed == 0

if __name__ == "__main__":
    success = test_all_functions()
    sys.exit(0 if success else 1)
