#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Holiday Question Helper MCP Server
명절 질문 답변 생성기
"""

from datetime import datetime
from typing import Dict, Any
from fastmcp import FastMCP
from responses import (
    QUESTION_CATEGORIES,
    RESPONSE_STYLES,
    MARRIAGE_RESPONSES,
    ALL_RESPONSES,
    detect_category,
    get_response,
    get_all_response
)

# FastMCP 서버 초기화
mcp = FastMCP("Holiday Question Helper")

@mcp.tool
def generate_marriage_response(
    question: str,
    style: str = "humorous"
) -> Dict[str, Any]:
    """결혼 관련 질문에 대한 답변을 생성합니다.
    
    Args:
        question: 친척이 한 질문 (예: "결혼은 언제 하니?", "왜 아직도 안 결혼했어?", "소개팅 안 해?")
        style: 답변 스타일 (humorous, witty, polite, reverse, wise)
    
    Returns:
        dict: {
            "question": "결혼은 언제 하니?",
            "style": "유머러스",
            "response": "제 결혼식 날짜는 제가 제일 궁금해요...",
            "category": "결혼 관련",
            "timestamp": "2025-09-29T10:30:00Z",
            "disclaimer": "이 답변은 유머를 위한 것입니다. 실제 상황에 맞게 조절하세요."
        }
    """
    try:
        # 입력 검증
        if style not in RESPONSE_STYLES:
            return {
                "error": "입력 오류",
                "message": f"지원하지 않는 스타일입니다. 사용 가능: {', '.join(RESPONSE_STYLES.keys())}",
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        
        # 질문 매칭
        question_key = None
        for key in MARRIAGE_RESPONSES.keys():
            if key in question or question in key:
                question_key = key
                break
        
        if not question_key:
            # 일반적인 결혼 관련 질문으로 처리
            question_key = "결혼은 언제 하니?"
        
        # 답변 생성
        response_text = get_response(question_key, style)
        
        # 결과 반환
        result = {
            "question": question,
            "matched_question": question_key,
            "category": "결혼 관련",
            "style": RESPONSE_STYLES[style],
            "response": response_text,
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "disclaimer": "⚠️ 이 답변은 유머를 위한 것입니다. 실제 상황과 가족 관계를 고려해서 적절히 사용하세요."
        }
        
        return result
        
    except Exception as e:
        return {
            "error": "시스템 오류",
            "message": f"예상치 못한 오류가 발생했습니다: {str(e)}",
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        }

@mcp.tool
def generate_response(
    question: str,
    style: str = "humorous",
    category: str = "auto"
) -> Dict[str, Any]:
    """명절 질문에 대한 답변을 생성합니다 (모든 카테고리 지원).
    
    Args:
        question: 친척이 한 질문
        style: 답변 스타일 (humorous, witty, polite, reverse, wise)
        category: 질문 카테고리 (auto, marriage, childbirth, job, study, appearance, age)
                 auto로 설정시 자동 감지
    
    Returns:
        dict: 답변 정보
    """
    try:
        # 입력 검증
        if style not in RESPONSE_STYLES:
            return {
                "error": "입력 오류",
                "message": f"지원하지 않는 스타일입니다. 사용 가능: {', '.join(RESPONSE_STYLES.keys())}",
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        
        # 카테고리 자동 감지 또는 수동 설정
        if category == "auto":
            detected_category = detect_category(question)
        else:
            if category not in QUESTION_CATEGORIES:
                return {
                    "error": "입력 오류",
                    "message": f"지원하지 않는 카테고리입니다. 사용 가능: {', '.join(QUESTION_CATEGORIES.keys())}",
                    "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
                }
            detected_category = category
        
        # 질문 매칭
        question_key = None
        category_responses = ALL_RESPONSES.get(detected_category, {})
        
        for key in category_responses.keys():
            if key in question or question in key:
                question_key = key
                break
        
        if not question_key:
            # 해당 카테고리의 첫 번째 질문으로 처리
            question_key = list(category_responses.keys())[0] if category_responses else None
        
        if not question_key:
            return {
                "error": "답변 생성 실패",
                "message": "적절한 답변을 찾을 수 없습니다.",
                "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        
        # 답변 생성
        response_text = get_all_response(detected_category, question_key, style)
        
        # 결과 반환
        result = {
            "question": question,
            "matched_question": question_key,
            "category": QUESTION_CATEGORIES[detected_category],
            "category_key": detected_category,
            "style": RESPONSE_STYLES[style],
            "style_key": style,
            "response": response_text,
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "disclaimer": "⚠️ 이 답변은 유머를 위한 것입니다. 실제 상황과 가족 관계를 고려해서 적절히 사용하세요."
        }
        
        return result
        
    except Exception as e:
        return {
            "error": "시스템 오류",
            "message": f"예상치 못한 오류가 발생했습니다: {str(e)}",
            "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
        }

@mcp.tool
def list_categories() -> Dict[str, Any]:
    """사용 가능한 모든 질문 카테고리를 조회합니다.
    
    Returns:
        dict: 카테고리 목록 및 설명
    """
    return {
        "categories": QUESTION_CATEGORIES,
        "styles": RESPONSE_STYLES,
        "total_categories": len(QUESTION_CATEGORIES),
        "total_styles": len(RESPONSE_STYLES),
        "timestamp": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    }

# 서버 실행
if __name__ == "__main__":
    mcp.run()
