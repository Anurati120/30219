import streamlit as st

# 1. 페이지 설정 (넓은 화면, 임팩트 있는 아이콘)
st.set_page_config(page_title="Ultimate Car 20-Questions", page_icon="🏎️", layout="centered")

# 2. 100배 더 멋진 프리미엄 다크 네온 디자인 CSS 적용
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
        background-color: #030712;
        color: #f9fafb !important;
    }
    .stApp {
        background: radial-gradient(circle at top, #111827 0%, #030712 100%);
    }
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #f9fafb !important;
    }
    .hero-box {
        background: linear-gradient(135deg, rgba(31, 41, 55, 0.4), rgba(17, 24, 39, 0.7));
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 35px;
        backdrop-filter: blur(16px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        margin-bottom: 25px;
    }
    .hint-box {
        background: rgba(15, 23, 42, 0.8);
        border-left: 5px solid #3b82f6;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.6);
    }
    /* 고급스러운 가로 배치 보기 버튼 스타일 */
    .stButton>button {
        width: 100%;
        height: 65px;
        border-radius: 16px;
        background: linear-gradient(135deg, #1f2937, #111827);
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
        border-color: #60a5fa;
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(59, 130, 246, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. 풍성하게 확장된 자동차 스무고개 데이터베이스 (총 10문제)
quiz_list = [
    {
        "answer": "포르쉐 911",
        "hints": [
            "1고개: 독일을 대표하는 전설적인 스포츠카 브랜드의 모델입니다.",
            "2고개: 엔진이 차체 맨 뒤쪽에 탑재되는 독특한 '리어 엔진' 구조를 가졌습니다.",
            "3고개: 개구리 눈을 연상시키는 동그란 헤드램프가 수십 년째 이어져 내려옵니다.",
            "4고개: 숫자 세 자리로 이루어진 이름을 가지고 있으며 후륜구동의 교과서입니다.",
            "5고개: 포르쉐의 정체성 그 자체인 베스트셀링 후륜구동 스포츠카입니다!"
        ],
        "options": ["포르쉐 911", "람보르기니 우라칸", "테슬라 모델 S", "페라리 로마"]
    },
    {
        "answer": "현대 아이오닉 5 N",
        "hints": [
            "1고개: 대한민국을 대표하는 글로벌 브랜드의 고성능 전용 모델입니다.",
            "2고개: 배출가스가 전혀 없는 순수 전기 파워트레인을 탑재했습니다.",
            "3고개: SUV 패밀리카의 형태를 지녔지만, 서킷을 폭격하는 괴물 성능을 냅니다.",
            "4고개: 현대차의 고성능 N 브랜드를 상징하는 알파벳이 붙어 있습니다.",
            "5고개: 가짜 변속 충격과 사운드로 가슴을 뛰게 하는 전기 SUV입니다!"
        ],
        "options": ["기아 EV6 GT", "현대 아이오닉 5 N", "제네시스 GV80", "현대 아반떼 N"]
    },
    {
        "answer": "람보르기니 우라칸",
        "hints": [
            "1고개: 이탈리아의 강렬한 감성을 품은 슈퍼카 브랜드 차량입니다.",
            "2고개: 성난 황소 엠블렘을 달고 있으며 폭발적인 V10 자연흡기 엔진을 품었습니다.",
            "3고개: 스페인어로 '허리케인'이라는 뜻의 이름을 가지고 있습니다.",
            "4고개: 이전 모델인 가야르도의 성공을 이어받은 주력 베스트셀링 슈퍼카입니다.",
            "5고개: 람보르기니를 상징하는 10기통 미드십 슈퍼카입니다!"
        ],
        "options": ["페라리 F8", "맥라렌 720S", "람보르기니 우라칸", "포르쉐 타이칸"]
    },
    {
        "answer": "테슬라 모델 S",
        "hints": [
            "1고개: 미국 실리콘밸리의 혁신적인 전기차 전용 브랜드 플래그십입니다.",
            "2고개: 주유소가 필요 없으며 오직 대용량 배터리와 모터로만 움직입니다.",
            "3고개: 하이퍼카를 위협하는 미친 듯한 가속력(Plaid 버전)으로 유명합니다.",
            "4고개: 거대한 중앙 디스플레이와 반자율주행의 선구자격인 모델입니다.",
            "5고개: 알파벳 S가 붙는 테슬라의 대형 럭셔리 전기 세단입니다!"
        ],
        "options": ["테슬라 모델 3", "테슬라 모델 S", "현대 아이오닉 6", "포르쉐 타이칸"]
    },
    {
        "answer": "부가티 치론",
        "hints": [
            "1고개: 프랑스에서 탄생한 초고가 하이퍼카 브랜드의 대표 작품입니다.",
            "2고개: 무려 1,500마력이 넘는 상상을 초월하는 출력을 자랑합니다.",
            "3고개: 시속 400km/h를 가볍게 돌파하는 세계 최고 속도 기록의 아이콘입니다.",
            "4고개: 8리터 16기통(W16) 이라는 거대한 엔진을 탑재했습니다.",
            "5고개: 베이론의 뒤를 이어 지구상에서 가장 비싼 차 중 하나로 꼽힙니다!"
        ],
        "options": ["코닉세그 제스코", "부가티 치론", "파가니 유아이라", "페라리 라페라리"]
    },
    {
        "answer": "BMW M5",
        "hints": [
            "1고개: 독일의 프리미엄 브랜드 BMW의 고성능 디비전 모델입니다.",
            "2고개: 겉보기엔 평범한 럭셔리 비즈니스 세단이지만 속은 괴물입니다.",
            "3고개: 패밀리와 서킷 주행을 동시에 만족시키는 '고성능 세단의 교과서'입니다.",
            "4고개: 강력한 8기통 트윈터보 엔진과 지능형 4륜구동 시스템을 탑재했습니다.",
            "5고개: 알파벳 M과 숫자 5가 조합된 전설적인 스포츠 세단입니다!"
        ],
        "options": ["벤츠 E63 AMG", "아우디 RS6", "BMW M5", "제네시스 G80 스포츠"]
    },
    {
        "answer": "메르세데스-벤츠 G바겐",
        "hints": [
            "1고개: 독일 벤츠의 전통을 이어받은 각진 정통 오프로드 SUV입니다.",
            "2고개: 군용 차량에서 유래된 강인하고 투박한 상남자 디자인이 특징입니다.",
            "3고개: 셀럽들과 연예인들이 가장 사랑하는 드림 카 중 하나입니다.",
            "4고개: 험준한 산악 지형을 탱크처럼 돌파하는 강력한 4륜구동 시스템을 갖췄습니다.",
            "5고개: 알파벳 G로 시작하는 벤츠의 최고급 오프로더입니다!"
        ],
        "options": ["랜드로버 디펜더", "메르세데스-벤츠 G바겐", "지프랭글러", "포르쉐 카이엔"]
    },
    {
        "answer": "현대 아반떼 N",
        "hints": [
            "1고개: 대한민국 도로에서 가장 흔하게 볼 수 있는 준중형 세단이 기반입니다.",
            "2고개: 하지만 일반 모델과는 차원이 다른 극강의 서킷 주행 성능을 자랑합니다.",
            "3고개: 운전자의 아드레날린을 폭발시키는 팝콘 배기음이 시그니처입니다.",
            "4고개: 현대차의 고성능 기술력이 집약된 가성비 끝판왕 스포츠 세단입니다.",
            "5고개: 국산 준중형 세단 베이스에 N 문호가 붙은 이 차의 이름은?"
        ],
        "options": ["현대 아반떼 N", "기아스팅어", "현대 벨로스터", "쉐보레 말리부"]
    },
    {
        "answer": "롤스로이스 팬텀",
        "hints": [
            "1고개: 영국이 자랑하는 전 세계 상위 0.1%를 위한 궁극의 럭셔리 브랜드입니다.",
            "2고개: 보닛 위에는 '환희의 여신상' 은색 마스코트가 우아하게 서 있습니다.",
            "3고개: 세상에서 가장 조용하고 안락한, '움직이는 궁전'으로 불립니다.",
            "4고개: 문이 뒤로 열리는 '코치 도어' 방식을 채택하고 있습니다.",
            "5고개: 롤스로이스의 기함(플래그십)을 상징하는 거대한 세단입니다!"
        ],
        "options": ["벤틀리 플라잉스퍼", "메르세데스-마이바흐 S클래스", "롤스로이스 팬텀", "레인지로버 오토바이오그래피"]
    },
    {
        "answer": "미니 쿠퍼",
        "hints": [
            "1고개: 영국의 헤리티지를 품고 현재는 BMW 그룹에 속한 컴팩트카입니다.",
            "2고개: 동그란 헤드램프와 아기자기하고 개성 넘치는 클래식 디자인이 특징입니다.",
            "3고개: 카트처럼 민첩하고 짜릿한 핸들링 성능으로 '고카트 필링'을 선사합니다.",
            "4고개: 영국 국기(유니언잭) 디자인을 후미등이나 루프에 자주 활용합니다.",
            "5고개: 이름 그대로 '작고 귀여운' 매력을 가진 프리미엄 해치백입니다!"
        ],
        "options": ["피아트 500", "폭스바겐 비틀", "미니 쿠퍼", "푸조 208"]
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

# 5. 화면 레이아웃 구성
st.markdown("<h1 style='text-align: center; font-weight: 800; letter-spacing: -1px;'>🏎️ ULTIMATE CAR 20-QUESTIONS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 16px; margin-bottom: 30px;'>스무고개 룰처럼 힌트를 하나씩 열어가며 최고의 명차를 추리해보세요!</p>", unsafe_allow_html=True)

# [시작 전 화면]
if not st.session_state.started:
    st.markdown("""
    <div class="hero-box" style="text-align: center;">
        <h2 style="color: #60a5fa !important; margin-bottom: 15px;">챌린지 준비 완료!</h2>
        <p style="font-size: 17px; line-height: 1.6; color: #d1d5db;">
            총 <b>10문제</b>의 프리미엄 자동차 스무고개가 기다리고 있습니다.<br>
            모르겠다면 아래의 <b>[💡 다음 힌트 보기]</b>를 눌러 힌트를 추가로 오픈하세요!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 스무고개 챌린지 시작하기"):
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
    max_hints = len(current_quiz["hints"])
    
    # 상단 상태 정보 표시 카드
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"#### 🎯 문제: {st.session_state.current_q_idx + 1} / {len(quiz_list)}")
    with c2:
        st.markdown(f"#### 🔍 공개된 힌트: {st.session_state.hint_step + 1}개 / 총 {max_hints}개")
    
    # 누적된 힌트 출력 박스
    hints_so_far = "<br><br>".join(current_quiz["hints"][:st.session_state.hint_step + 1])
    st.markdown(f"""
    <div class="hint-box">
        <h4 style="color: #60a5fa !important; margin-top: 0; margin-bottom: 12px;">💡 스무고개 힌트 현황</h4>
        <p style="font-size: 17px; line-height: 1.6; margin: 0;">{hints_so_far}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 아직 이 문제를 풀지 않은 경우
    if not st.session_state.solved_current:
        # [스무고개 룰 핵심] 다음 힌트 보기 버튼 (아직 최대 힌트에 도달하지 않았을 때만 노출)
        if st.session_state.hint_step < max_hints - 1:
            if st.button("💡 다음 힌트 보기 (+1 고개 열기)"):
                st.session_state.hint_step += 1
                st.rerun()
            st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)
        
        st.markdown("### 정답을 선택하세요")
        # 가로형 보기 버튼 배치 (4지선다 자동 분할)
        cols = st.columns(len(current_quiz["options"]))
        for i, opt in enumerate(current_quiz["options"]):
            with cols[i]:
                if st.button(opt, key=f"opt_{st.session_state.current_q_idx}_{i}"):
                    if opt == current_quiz["answer"]:
                        st.session_state.solved_current = True
                        st.session_state.score += 1
                        st.success("🎉 정대입니다! 완벽하게 맞히셨습니다!")
                        st.rerun()
                    else:
                        st.error("❌ 아쉽습니다! 정답이 아닙니다. 힌트를 더 보거나 다시 선택해보세요.")
                            
    # 정답을 맞힌 경우 -> 다음 문제로 넘어가는 버튼 활성화
    else:
        st.markdown("---")
        if st.session_state.current_q_idx < len(quiz_list) - 1:
            if st.button("➡️ 다음 문제로 이동하기"):
                st.session_state.current_q_idx += 1
                st.session_state.hint_step = 0
                st.session_state.solved_current = False
                st.rerun()
        else:
            if st.button("🏆 최종 결과 확인하기"):
                st.session_state.game_finished = True
                st.rerun()

# [모든 퀴즈 완료 최종 화면]
else:
    st.markdown("""
    <div class="hero-box" style="text-align: center;">
        <h1 style="color: #4ade80 !important; font-size: 36px; margin-bottom: 10px;">🏆 스무고개 챌린지 완주!</h1>
        <p style="font-size: 18px; color: #d1d5db;">모든 명차 추리 미션을 성공적으로 마쳤습니다.</p>
    </div>
    """, unsafe_allow_html=True)
    
    total_q = len(quiz_list)
    final_score = st.session_state.score
    
    st.metric(label="최종 맞힌 문제 수", value=f"{final_score} / {total_q}")
    
    if final_score == total_q:
        st.balloons()
        st.success("만점 달성! 이 정도면 명실상부한 자동차 마스터 박사님입니다! 🏅✨")
    else:
        st.info("고생하셨습니다! 다시 도전해서 전 문제 만점에 도전해 보세요.")
        
    if st.button("🔄 처음부터 다시 도전하기"):
        st.session_state.started = False
        st.session_state.current_q_idx = 0
        st.session_state.hint_step = 0
        st.session_state.solved_current = False
        st.session_state.score = 0
        st.session_state.game_finished = False
        st.rerun()
