import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Car Quiz Challenge", page_icon="🏁", layout="centered")

# 2. 디자인 스타일 적용 (고급스러운 다크 테마)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0b0f19;
        color: #f3f4f6;
    }
    .stApp {
        background: radial-gradient(circle at center, #111827, #0b0f19);
    }
    .quiz-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background: #3b82f6;
        color: white;
        font-weight: 600;
        padding: 10px;
        border: none;
    }
    .stButton>button:hover {
        background: #2563eb;
    }
</style>
""", unsafe_allow_html=True)

# 3. 퀴즈 데이터베이스 준비
quiz_data = [
    {
        "question": "이 차는 포르쉐의 대표적인 후륜구동 스포츠카로, 개구리 눈을 닮은 독특한 헤드램프와 뒤쪽에 엔진이 달린 '리어 엔진' 구조가 특징입니다. 이 차의 이름은?",
        "options": ["포르쉐 911", "포르쉐 타이칸", "포르쉐 파나메라", "포르쉐 카이엔"],
        "answer": "포르쉐 911",
        "hint": "숫자 세 자리고 유명한 경주용 차 계열이에요."
    },
    {
        "question": "이탈리아의 슈퍼카 브랜드로, 황소 엠블렘을 가지고 있으며 '람보르기니'의 V12 플래그십 모델 라인업의 전통을 잇는 모델의 이름은? (예: 아벤타도르의 후속 모델)",
        "options": ["우라칸", "레부엘토", "우루스", "갈라도"],
        "answer": "레부엘토",
        "hint": "라틴어로 '격동하는'이라는 뜻을 가진 플러그인 하이브리드 슈퍼카입니다."
    },
    {
        "question": "현대자동차의 고성능 브랜드 'N'에서 나온 첫 번째 순수 전기 고성능 차로, 트랙 주행에 최적화된 이 모델의 이름은?",
        "options": ["아이오닉 5 N", "아반떼 N", "벨로스터 N", "쏘나타 N라인"],
        "answer": "아이오닉 5 N",
        "hint": "국민 전기차 SUV의 이름을 따왔지만 끝에 알파벳 N이 붙습니다."
    },
    {
        "question": "일론 머스크가 이끄는 테슬라의 플래그십 세단으로, 엄청난 가속력과 자율주행 기술로 유명한 이 차의 이름은?",
        "options": ["모델 3", "모델 Y", "모델 S", "사이버트럭"],
        "answer": "모델 S",
        "hint": "알파벳 S로 시작하는 대형 세단입니다."
    }
]

# 4. 세션 상태 초기화 (점수, 현재 문제 번호, 시작 여부 관리)
if 'started' not in st.session_state:
    st.session_state.started = False
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_finished' not in st.session_state:
    st.session_state.quiz_finished = False

# 5. 화면 구성
st.title("🏁 Ultimate Car Quiz Challenge")
st.write("자동차에 대한 지식을 테스트하고 최고점을 노려보세요!")
st.markdown("---")

# [시작 전 화면]
if not st.session_state.started:
    st.markdown("""
    <div class="quiz-card" style="text-align: center;">
        <h2>퀴즈를 시작할 준비가 되셨나요?</h2>
        <p>총 4문제가 출제되며, 힌트를 보고 알맞은 자동차를 맞히는 게임입니다.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 퀴즈 시작하기"):
        st.session_state.started = True
        st.rerun()

# [퀴즈 진행 중 화면]
elif not st.session_state.quiz_finished:
    q_idx = st.session_state.current_q
    current_quiz = quiz_data[q_idx]
    
    st.subheader(f"문제 {q_idx + 1} / {len(quiz_data)}")
    
    with st.container():
        st.markdown(f"""
        <div class="quiz-card">
            <h3>{current_quiz['question']}</h3>
            <p style='color: #60a5fa; font-style: italic;'>💡 힌트: {current_quiz['hint']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 보기 선택 라디오 버튼
    user_choice = st.radio("정답을 선택하세요:", current_quiz['options'], key=f"q_{q_idx}")
    
    if st.button("정답 제출하기"):
        if user_choice == current_quiz['answer']:
            st.session_state.score += 1
            st.success("🎉 정답입니다! 멋지네요!")
        else:
            st.error(f"❌ 아쉽습니다! 정답은 **{current_quiz['answer']}** 였습니다.")
        
        # 다음 문제로 넘어가기 전 잠시 대기 또는 버튼 클릭 유도
        if st.button("다음 문제로 ➡️"):
            if st.session_state.current_q < len(quiz_data) - 1:
                st.session_state.current_q += 1
                st.rerun()
            else:
                st.session_state.quiz_finished = True
                st.rerun()

# [퀴즈 종료 화면]
else:
    st.markdown("""
    <div class="quiz-card" style="text-align: center;">
        <h2>🏆 퀴즈가 종료되었습니다!</h2>
    </div>
    """, unsafe_allow_html=True)
    
    total = len(quiz_data)
    score = st.session_state.score
    
    st.metric(label="최종 점수", value=f"{score} / {total}")
    
    if score == total:
        st.balloons()
        st.success("만세! 모든 문제를 맞혔습니다. 자동차 박사님이시네요! 🏅")
    else:
        st.info("수고하셨습니다! 다시 도전해서 만점에 도전해 보세요.")
        
    if st.button("🔄 처음부터 다시 하기"):
        st.session_state.started = False
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.session_state.quiz_finished = False
        st.rerun()
