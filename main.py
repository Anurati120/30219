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

# 3. 스무고개 대상 자동차 데이터베이스 및 단계별 힌트 (최대 5단계 = 5고개)
car_game_data = {
    "answer": "포르쉐 911",
    "hints": [
        "1고개: 이 차는 독일에서 태어났습니다.",
        "2고개: 엔진이 차체 뒤쪽(리어 엔진)에 탑재되어 있습니다.",
        "3고개: 개구리 눈을 닮은 동그란 헤드램프가 시그니처입니다.",
        "4고개: 숫자 세 자리로 이루어진 이름이며, 스포츠카의 전설로 불립니다.",
        "5고개: 포르쉐의 가장 대표적인 정통 후륜구동 스포츠카입니다!"
    ],
    "options": ["포르쉐 911", "람보르기니 우라칸", "테슬라 모델 S", "현대 아이오닉 5"]
}

# 4. 세션 상태 초기화
if 'started' not in st.session_state:
    st.session_state.started = False
if 'hint_step' not in st.session_state:
    st.session_state.hint_step = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'is_success' not in st.session_state:
    st.session_state.is_success = False

# 5. 화면 레이아웃
st.title("🕵️ 자동차 스무고개 챌린지")
st.markdown("<p style='color: #d1d5db;'>힌트를 보고 어떤 자동차인지 맞춰보세요! (총 5개의 힌트 제공)</p>", unsafe_allow_html=True)
st.markdown("---")

# [시작 전 화면]
if not st.session_state.started:
    st.markdown("""
    <div class="quiz-card" style="text-align: center;">
        <h2>스무고개 게임을 시작합니다!</h2>
        <p>힌트가 하나씩 늘어날수록 정답을 맞힐 확률이 높아집니다.<br>과연 몇 번 만에 맞힐 수 있을까요?</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 게임 시작하기"):
        st.session_state.started = True
        st.rerun()

# [게임 진행 중 화면]
elif not st.session_state.game_over:
    current_step = st.session_state.hint_step
    max_steps = len(car_game_data["hints"])
    
    # 상단 상태 표시
    st.markdown(f"### 🎯 현재 진행: {current_step + 1}고개 / 총 {max_steps}고개")
    
    # 힌트 카드 박스
    hints_so_far = "<br>".join(car_game_data["hints"][:current_step + 1])
    st.markdown(f"""
    <div class="quiz-card">
        <h4>💡 공개된 힌트 목록</h4>
        <p style="font-size: 18px; line-height: 1.6;">{hints_so_far}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 정답을 선택하세요 (가로 배치)")
    
    # 가로(세 개 혹은 네 개의 열)로 버튼 배치
    cols = st.columns(len(car_game_data["options"]))
    
    for i, opt in enumerate(car_game_data["options"]):
        with cols[i]:
            if st.button(opt, key=f"opt_{i}"):
                if opt == car_game_data["answer"]:
                    st.session_state.game_over = True
                    st.session_state.is_success = True
                    st.rerun()
                else:
                    # 틀렸을 때 힌트를 하나 더 늘림 (마지막 힌트까지 다 썼는데 틀리면 게임 오버)
                    if st.session_state.hint_step < max_steps - 1:
                        st.session_state.hint_step += 1
                        st.warning("❌ 틀렸습니다! 다음 힌트가 열립니다.")
                        st.rerun()
                    else:
                        st.session_state.game_over = True
                        st.session_state.is_success = False
                        st.rerun()

# [게임 종료 화면 (성공 또는 실패)]
else:
    if st.session_state.is_success:
        st.balloons()
        st.markdown("""
        <div class="quiz-card" style="text-align: center;">
            <h1 style="color: #4ade80 !important;">🎉 정답입니다!</h1>
            <p style="font-size: 20px;">훌륭합니다! 완벽하게 차를 맞히셨네요!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="quiz-card" style="text-align: center;">
            <h1 style="color: #f87171 !important;">😢 아쉽게도 기회를 모두 소진했습니다.</h1>
            <p style="font-size: 20px;">정답은 바로 <b>포르쉐 911</b> 이었습니다!</p>
        </div>
        """, unsafe_allow_html=True)
        
    if st.button("🔄 다시 도전하기"):
        st.session_state.started = False
        st.session_state.hint_step = 0
        st.session_state.game_over = False
        st.session_state.is_success = False
        st.rerun()
