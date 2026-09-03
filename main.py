import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Car 20-Questions", page_icon="🕵️", layout="centered")

# 2. 디자인 스타일 적용 (글씨 흰색, 가로형 큰 버튼 디자인 등)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #0b0f19;
        color: #ffffff !important;
    }
    .stApp {
        background: radial-gradient(circle at center, #111827, #0b0f19);
    }
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #ffffff !important;
    }
    .quiz-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 30px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    /* 버튼 크기를 키우고 가로 배치를 위한 스타일 */
    .stButton>button {
        width: 100%;
        height: 60px;
        border-radius: 14px;
        background: #1f2937;
        color: white;
        font-size: 18px;
        font-weight: 700;
        border: 2px solid rgba(255, 255, 255, 0.2);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: #3b82f6;
        border-color: #3b82f6;
    }
</style>
""", unsafe_allow_html=True)

# 3. 여러 대의 차에 대한 스무고개 문제 데이터베이스 (총 4문제)
quiz_list = [
    {
        "answer": "포르쉐 911",
        "hints": [
            "1고개: 이 차는 독일에서 태어났습니다.",
            "2고개: 엔진이 차체 뒤쪽(리어 엔진)에 탑재되어 있습니다.",
            "3고개: 개구리 눈을 닮은 동그란 헤드램프가 시그니처입니다.",
            "4고개: 숫자 세 자리로 이루어진 이름이며, 스포츠카의 전설로 불립니다.",
            "5고개: 포르쉐의 가장 대표적인 정통 후륜구동 스포츠카입니다!"
        ],
        "options": ["포르쉐 911", "람보르기니 우라칸", "테슬라 모델 S", "현대 아이오닉 5"]
    },
    {
        "answer": "람보르기니 우라칸",
        "hints": [
            "1고개: 이탈리아의 슈퍼카 브랜드 차량입니다.",
            "2고개: 황소 엠블렘을 가지고 있으며, V10 자연흡기 엔진을 품고 있습니다.",
            "3고개: 스페인어로 '허리케인'이라는 뜻을 가지고 있습니다.",
            "4고개: 가야르도의 뒤를 이어 엄청난 인기를 끈 베스트셀링 슈퍼카입니다.",
            "5고개: 람보르기니의 대표적인 V10 미드십 슈퍼카입니다!"
        ],
        "options": ["페라리 로마", "람보르기니 우라칸", "포르쉐 타이칸", "BMW M5"]
    },
    {
        "answer": "테슬라 모델 S",
        "hints": [
            "1고개: 미국의 혁신적인 전기차 전용 브랜드 차량입니다.",
            "2고개: 엔진 없이 배터리와 전기 모터로만 움직이는 럭셔리 세단입니다.",
            "3고개: 엄청난 가속력으로 '플레이드(Plaid)' 버전은 슈퍼카를 압도합니다.",
            "4고개: 대형 터치스크린과 오토파일럿 자율주행 기술의 선구자입니다.",
            "5고개: 알파벳 S가 붙는 테슬라의 플래그십 전기 세단입니다!"
        ],
        "options": ["현대 아이오닉 5", "기아 EV6", "테슬라 모델 S", "포르쉐 타이칸"]
    },
    {
        "answer": "현대 아이오닉 5 N",
        "hints": [
            "1고개: 대한민국 현대자동차에서 출시한 차량입니다.",
            "2고개: 순수 전기로 움직이는 친환경 전기차입니다.",
            "3고개: 패밀리 SUV의 형태를 가졌지만, 서킷 주행이 가능한 괴물입니다.",
            "4고개: 현대차의 고성능 브랜드 알파벳인 '이것'이 붙어 있습니다.",
            "5고개: 가짜 변속 소리와 배기음을 내는 고성능 전기 SUV입니다!"
        ],
        "options": ["현대 아이오닉 5 N", "제네시스 G90", "기아 쏘렌토", "아반떼 N"]
    }
]

# 4. 세션 상태 초기화
if 'started' not in st.session_state:
    st.session_state.started = False
if 'current_q_idx' not in st.session_state:
    st.session_state.current_q_idx = 0
if 'hint_step' not in st.session_state:
    st.session_state.hint_step = 0
if 'solved_current' not in st.session_state:
    st.session_state.solved_current = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_finished' not in st.session_state:
    st.session_state.game_finished = False

# 5. 화면 레이아웃
st.title("🕵️ 자동차 스무고개 챌린지")
st.markdown("<p style='color: #d1d5db;'>힌트를 단계별로 확인하며 어떤 자동차인지 맞춰보세요!</p>", unsafe_allow_html=True)
st.markdown("---")

# [시작 전 화면]
if not st.session_state.started:
    st.markdown("""
    <div class="quiz-card" style="text-align: center;">
        <h2>스무고개 게임을 시작합니다!</h2>
        <p>총 4대의 자동차 문제가 준비되어 있습니다.<br>각 문제마다 5개의 힌트가 숨겨져 있어요!</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 게임 시작하기"):
        st.session_state.started = True
        st.session_state.current_q_idx = 0
        st.session_state.hint_step = 0
        st.session_state.solved_current = False
        st.session_state.score = 0
        st.session_state.game_finished = False
        st.rerun()

# [게임 진행 중 화면]
elif not st.session_state.game_finished:
    current_quiz = quiz_list[st.session_state.current_q_idx]
    max_steps = len(current_quiz["hints"])
    
    # 상단 상태 표시 (몇 번째 문제인지, 몇 번째 힌트인지)
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.markdown(f"### 🚗 문제 {st.session_state.current_q_idx + 1} / {len(quiz_list)}")
    with col_info2:
        st.markdown(f"### 💡 현재 힌트: {st.session_state.hint_step + 1}고개 / {max_steps}고개")
    
    # 공개된 힌트 누적 출력 카드
    hints_so_far = "<br>".join(current_quiz["hints"][:st.session_state.hint_step + 1])
    st.markdown(f"""
    <div class="quiz-card">
        <h4>🔍 스무고개 힌트</h4>
        <p style="font-size: 18px; line-height: 1.6;">{hints_so_far}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 아직 정답을 맞히지 않은 경우: 보기 버튼 가로 배치
    if not st.session_state.solved_current:
        st.markdown("### 정답을 선택하세요")
        cols = st.columns(len(current_quiz["options"]))
        
        for i, opt in enumerate(current_quiz["options"]):
            with cols[i]:
                if st.button(opt, key=f"opt_{st.session_state.current_q_idx}_{i}"):
                    if opt == current_quiz["answer"]:
                        st.session_state.solved_current = True
                        st.session_state.score += 1
                        st.success("🎉 정답입니다! 멋지게 맞히셨어요!")
                        st.rerun()
                    else:
                        # 틀렸을 때: 힌트가 남아있다면 다음 힌트 개방
                        if st.session_state.hint_step < max_steps - 1:
                            st.session_state.hint_step += 1
                            st.warning("❌ 틀렸습니다! 다음 힌트가 열립니다.")
                            st.rerun()
                        else:
                            st.error(f"😢 아쉽게도 기회를 모두 소진했습니다! 정답은 **{current_quiz['answer']}** 였습니다.")
                            st.session_state.solved_current = True  # 다음 문제로 넘어가기 위해 처리
                            st.rerun()
                            
    # 정답을 맞혔거나 기회를 소진한 경우 -> "다음 문제 풀기" 버튼 활성화
    else:
        st.markdown("---")
        if st.session_state.current_q_idx < len(quiz_list) - 1:
            if st.button("➡️ 다음 문제 풀기"):
                st.session_state.current_q_idx += 1
                st.session_state.hint_step = 0
                st.session_state.solved_current = False
                st.rerun()
        else:
            if st.button("🏆 최종 결과 보기"):
                st.session_state.game_finished = True
                st.rerun()

# [모든 퀴즈 완료 화면]
else:
    st.markdown("""
    <div class="quiz-card" style="text-align: center;">
        <h1 style="color: #4ade80 !important;">🏆 모든 스무고개를 마쳤습니다!</h1>
        <p style="font-size: 22px; margin-top: 15px;">나의 최종 점수</p>
    </div>
    """, unsafe_allow_html=True)
    
    total_q = len(quiz_list)
    final_score = st.session_state.score
    
    st.metric(label="맞힌 문제 수", value=f"{final_score} / {total_q}")
    
    if final_score == total_q:
        st.balloons()
        st.success("완벽합니다! 자동차 박사님 인증서 수여! 🏅✨")
    else:
        st.info("수고하셨습니다! 다시 도전해서 만점에 도전해 보세요.")
        
    if st.button("🔄 처음부터 다시 하기"):
        st.session_state.started = False
        st.session_state.current_q_idx = 0
        st.session_state.hint_step = 0
        st.session_state.solved_current = False
        st.session_state.score = 0
        st.session_state.game_finished = False
        st.rerun()
