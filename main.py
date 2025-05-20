import streamlit as st

# MBTI 직업 추천 딕셔너리
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "과학자", "소프트웨어 개발자"],
    "INTP": ["연구원", "데이터 분석가", "이론 물리학자"],
    "ENTJ": ["경영 컨설턴트", "CEO", "프로젝트 매니저"],
    "ENTP": ["스타트업 창업가", "기획자", "마케팅 전략가"],
    "INFJ": ["상담사", "작가", "교사"],
    "INFP": ["예술가", "심리학자", "작가"],
    "ENFJ": ["HR 매니저", "교육자", "정치가"],
    "ENFP": ["광고 기획자", "콘텐츠 크리에이터", "디자이너"],
    "ISTJ": ["회계사", "군인", "공무원"],
    "ISFJ": ["간호사", "사회복지사", "초등학교 교사"],
    "ESTJ": ["은행원", "경영자", "군 간부"],
    "ESFJ": ["상담 교사", "간호 관리자", "행정가"],
    "ISTP": ["엔지니어", "파일럿", "기술자"],
    "ISFP": ["패션 디자이너", "사진작가", "셰프"],
    "ESTP": ["영업 전문가", "기업가", "스포츠 코치"],
    "ESFP": ["배우", "MC", "이벤트 플래너"],
}

# 제목
st.title("🎯 MBTI 직업 추천기")
st.write("MBTI 성격 유형을 입력하면, 어울리는 직업을 추천해드려요!")

# 사용자 입력
user_mbti = st.text_input("당신의 MBTI를 입력해주세요 (예: INFP)").upper()

# 추천 결과 출력
if user_mbti:
    if user_mbti in mbti_jobs:
        st.success(f"✅ {user_mbti} 유형에게 어울리는 직업은 다음과 같아요:")
        for job in mbti_jobs[user_mbti]:
            st.markdown(f"- {job}")
    else:
        st.error("⚠️ 올바른 MBTI 유형을 입력해주세요 (예: ENFP, ISTJ 등).")
