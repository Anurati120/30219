import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(page_title="Ultimate Car 20-Questions", page_icon="🏎️", layout="centered")

# 2. 프리미엄 다크 네온 디자인 & 컴팩트 버튼 CSS 적용
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
        border-radius: 20px;
        padding: 25px;
        backdrop-filter: blur(16px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.5);
        margin-bottom: 20px;
    }
    .success-box {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.3));
        border: 2px solid #10b981;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        backdrop-filter: blur(16px);
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.2);
        margin-bottom: 20px;
    }
    .hint-box {
        background: rgba(15, 23, 42, 0.8);
        border-left: 5px solid #3b82f6;
        border-radius: 12px;
        padding: 15px 20px;
        margin-bottom: 15px;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.6);
    }
    /* 스크롤 없이 한눈에 들어오도록 버튼 높이와 여백 컴팩트 최적화 */
    .stButton>button {
        width: 100%;
        height: 48px;
        border-radius: 10px;
        background: linear-gradient(135deg, #1f2937, #111827);
        color: #ffffff;
        font-size: 14px;
        font-weight: 600;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        margin-bottom: 6px;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #3b82f6, #2563eb);
        border-color: #60a5fa;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# 3. 전체 명차 마스터 풀 (오답 구성용 차량 리스트)
all_car_pool = [
    "포르쉐 911", "람보르기니 우라칸", "테슬라 모델 S", "현대 아이오닉 5 N",
    "부가티 치론", "BMW M5", "메르세데스-벤츠 G바겐", "현대 아반떼 N",
    "롤스로이스 팬텀", "미니 쿠퍼", "페라리 F8", "아우디 R8",
    "맥라렌 720S", "포르쉐 타이칸", "벤틀리 컨티넨탈 GT",
    "지프 랭글러", "토요타 수프라", "포드 머스탱", "쉐보레 콜벳"
]

# 4. 10개의 자동차 스무고개 문제 데이터베이스
quiz_list = [
    {
        "answer": "포르쉐 911",
        "hints": [
            "1고개: 독일을 대표하는 전설적인 스포츠카 브랜드의 모델입니다.",
            "2고개: 엔진이 차체 맨 뒤쪽에 탑재되는 독특한 '리어 엔진' 구조를 가졌습니다.",
            "3고개: 개구리 눈을 연상시키는 동그란 헤드램프가 수십 년째 이어져 내려옵니다.",
            "4고개: 숫자 세 자리로 이루어진 이름을 가지고 있으며 후륜구동의 교과서입니다.",
            "5고개: 포르쉐의 정체성 그 자체인 베스트셀링 후륜구동 스포츠카입니다!"
        ]
    },
    {
        "answer": "현대 아이오닉 5 N",
        "hints": [
            "1고개: 대한민국을 대표하는 글로벌 브랜드의 고성능 전용 모델입니다.",
            "2고개: 배출가스가 전혀 없는 순수 전기 파워트레인을 탑재했습니다.",
            "3고개: SUV 패밀리카의 형태를 지녔지만, 서킷을 폭격하는 괴물 성능을 냅니다.",
            "4고개: 현대차의 고성능 N 브랜드를 상징하는 알파벳이 붙어 있습니다.",
            "5고개: 가짜 변속 충격과 사운드로 가슴을 뛰게 하는 전기 SUV입니다!"
        ]
    },
    {
        "answer": "람보르기니 우라칸",
        "hints": [
            "1고개: 이탈리아의 강렬한 감성을 품은 슈퍼카 브랜드 차량입니다.",
            "2고개: 성난 황소 엠블렘을 달고 있으며 폭발적인 V10 자연흡기 엔진을 품었습니다.",
            "3고개: 스페인어로 '허리케인'이라는 뜻의 이름을 가지고 있습니다.",
            "4고개: 이전 모델인 가야르도의 성공을 이어받은 주력 베스트셀링 슈퍼카입니다.",
            "5고개: 람보르기니를 상징하는 10기통 미드십 슈퍼카입니다!"
        ]
    },
    {
        "answer": "테슬라 모델 S",
        "hints": [
            "1고개: 미국 실리콘밸리의 혁신적인 전기차 전용 브랜드 플래그십입니다.",
            "2고개: 주유소가 필요 없으며 오직 대용량 배터리와 모터로만 움직입니다.",
            "3고개: 하이퍼카를 위협하는 미친 듯한 가속력(Plaid 버전)으로 유명합니다.",
            "4고개: 거대한 중앙 디스플레이와 반자율주행의 선구자격인 모델입니다.",
            "5고개: 알파벳 S가 붙는 테슬라의 대형 럭셔리 전기 세단입니다!"
        ]
    },
    {
        "answer": "부가티 치론",
        "hints": [
            "1고개: 프랑스에서 탄생한 초고가 하이퍼카 브랜드의 대표 작품입니다.",
            "2고개: 무려 1,500마력이 넘는 상상을 초월하는 출력을 자랑합니다.",
            "3고개: 시속 400km/h를 가볍게 돌파하는 세계 최고 속도 기록의 아이콘입니다.",
            "4고개: 8리터 16기통(W16) 이라는 거대한 엔진을 탑재했습니다.",
            "5고개: 베이론의 뒤를 이어 지구상에서 가장 비싼 차 중 하나로 꼽힙니다!"
        ]
    },
    {
        "answer": "BMW M5",
        "hints": [
            "1고개: 독일의 프리미엄 브랜드 BMW의 고성능 디비전 모델입니다.",
            "2고개: 겉보기엔 평범한 럭셔리 비즈니스 세단이지만 속은 괴물입니다.",
            "3고개: 패밀리와 서킷 주행을 동시에 만족시키는 '고성능 세단의 교과서'입니다.",
            "4고개: 강력한 8기통 트윈터보 엔진과 지능형 4륜구동 시스템을 탑재했습니다.",
            "5고개: 알파벳 M과 숫자 5가 조합된 전설적인 스포츠 세단입니다!"
        ]
    },
    {
        "answer": "메르세데스-벤츠 G바겐",
        "hints": [
            "1고개: 독일 벤츠의 전통을 이어받은 각진 정통 오프로드 SUV입니다.",
            "2고개: 군용 차량에서 유래된 강인하고 투박한 상남자 디자인이 특징입니다.",
            "3고개: 셀럽들과 연예인들이 가장 사랑하는 드림 카 중 하나입니다.",
            "4고개: 험준한 산악 지형을 탱크처럼 돌파하는 강력한 4륜구동 시스템을 갖췄습니다.",
            "5고개: 알파벳 G로 시작하는 벤츠의 최고급 오프로더입니다!"
        ]
    },
    {
        "answer": "현대 아반떼 N",
        "hints": [
            "1고개: 대한민국 도로에서 가장 흔하게 볼 수 있는 준중형 세단이 기반입니다.",
            "2고개: 하지만 일반 모델과는 차원이 다른 극강의 서킷 주행 성능을 자랑합니다.",
            "3고개: 운전자의 아드레날린을 폭발시키는 팝콘 배기음이 시그니처입니다.",
            "4고개: 현대차의 고성능 기술력이 집약된 가성비 끝판왕 스포츠 세단입니다.",
            "5고개: 국산 준중형 세단 베이스에 N 문호가 붙은 이 차의 이름은?"
        ]
    },
    {
        "answer": "롤스로이스 팬텀",
        "hints": [
            "1고개: 영국이 자랑하는 전 세계 상위 0.1%를 위한 궁극의 럭셔리 브랜드입니다.",
            "2고개: 보닛 위에는 '환희의 여신상' 은색 마스코트가 우아하게 서 있습니다.",
            "3고개: 세상에서 가장 조용하고 안락한, '움직이는 궁전'으로 불립니다.",
            "4고개: 문이 뒤로 열리는 '코치 도어' 방식을 채택하고 있습니다.",
            "5고개: 롤스로이스의 기함(플래그십)을 상징하는 거대한 세단입니다!"
        ]
    },
    {
        "answer": "미니 쿠퍼",
        "hints": [
            "1고개: 영국의 헤리티지를 품고 현재는 BMW 그룹에 속한 컴팩트카입니다.",
            "2고개: 동그란 헤드램프와 아기자기하고 개성 넘치는 클래식 디자인이 특징입니다.",
            "3고개: 카트처럼 민첩하고 짜릿한 핸들링 성능으로 '고카트 필링'을 선사합니다.",
            "4고개: 영국 국기(유니언잭) 디자인을 후미등이나 루프에 자주 활용합니다.",
            "5고개: 이름 그대로 '작고 귀여운' 매력을 가진 프리미엄 해치백입니다!"
        ]
    }
]

# 5. 세션 상태 초기화
if 'started' not in st.session_state:
    st.session_state.started = False
if 'current_q_idx' not in st.session_state:
    st.session_state.current_q_idx = 0
if 'hint_step' not in st.session_state:
    st.session_state.hint_step = 0
if 'solved_current' not in st.session_state:
    st.session_state.solved_current = False
if 'total_score' not in st.session_state:
    st.session_state.total_score = 0
if 'game_finished' not in st.session_state:
    st.session_state.game_finished = False

# 매 문제마다 정답을 포함한 10개의 고유 보기를 랜덤 생성하는 함수
def get_random_options(correct_answer):
    other_cars = [car for car in all_car_pool if car != correct_answer]
    selected_others = random.sample(other_cars, 9)
    options = selected_others + [correct_answer]
    random.shuffle(options)
    return options

# 6. 화면 레이아웃 구성
st.markdown("<h1 style='text-align: center; font-weight: 800; font-size: 28px; margin-bottom: 5px;'>🏎️ ULTIMATE CAR 20-QUESTIONS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #9ca3af; font-size: 14px; margin-bottom: 20px;'>힌트를 적게 볼수록 더 높은 점수를 획득합니다 (문제당 최대 10점)</p>", unsafe_allow_html=True)

# [시작 전 화면]
if not st.session_state.started:
    st.markdown("""
    <div class="hero-box" style="text-align: center;">
        <h3 style="color: #60a5fa !important; margin-bottom: 10px;">챌린지 준비 완료!</h3>
        <p style="font-size: 15px; line-height: 1.6; color: #d1d5db;">
            총 <b>10문제</b> (총점 100점 만점)<br>
            ⚠️ <b>힌트를 볼 때마다 2점씩 감점됩니다!</b> (기본 10점 시작)<br>
            신중하게 힌트를 열어보고 최고점을 노려보세요!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 스무고개 챌린지 시작하기"):
        st.session_state.started = True
        st.session_state.current_q_idx = 0
        st.session_state.hint_step = 0
        st.session_state.solved_current = False
        st.session_state.total_score = 0
        st.session_state.game_finished = False
        st.rerun()

# [게임 진행 중 화면]
elif not st.session_state.game_finished:
    current_quiz = quiz_list[st.session_state.current_q_idx]
    max_hints = len(current_quiz["hints"])
    
    # 세션에 현재 문제의 10개 보기가 없으면 새로 생성하여 저장
    if 'current_options' not in st.session_state or st.session_state.get('last_q_idx') != st.session_state.current_q_idx:
        st.session_state.current_options = get_random_options(current_quiz["answer"])
        st.session_state.last_q_idx = st.session_state.current_q_idx

    # [상태 A] 아직 정답을 못 맞힌 경우 (문제 풀이 화면)
    if not st.session_state.solved_current:
        # 상단 상태 정보 표시
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"<p style='font-size: 15px; font-weight: 600; margin:0;'>🎯 문제: {st.session_state.current_q_idx + 1} / {len(quiz_list)}</p>", unsafe_allow_html=True)
        with c2:
            # 현재 획득 가능한 예상 점수 계산 (최대 10점 - 힌트 오픈당 2점 감점)
            current_possible_score = max(2, 10 - (st.session_state.hint_step * 2))
            st.markdown(f"<p style='font-size: 15px; font-weight: 600; margin:0; text-align: right; color: #34d399;'>⭐ 현재 배점: {current_possible_score}점</p>", unsafe_allow_html=True)
        
        st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

        # 누적된 힌트 출력 박스
        hints_so_far = "<br>".join(current_quiz["hints"][:st.session_state.hint_step + 1])
        st.markdown(f"""
        <div class="hint-box">
            <p style="font-size: 14px; color: #60a5fa !important; font-weight: 700; margin-bottom: 6px;">💡 스무고개 힌트 현황 (힌트 추가 시 -2점)</p>
            <p style="font-size: 14px; line-height: 1.5; margin: 0;">{hints_so_far}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 다음 힌트 보기 버튼 (최대 힌트가 아닐 때만)
        if st.session_state.hint_step < max_hints - 1:
            if st.button("💡 다음 힌트 보기 (+1 고개 열기 / 점수 -2점)"):
                st.session_state.hint_step += 1
                st.rerun()
        
        st.markdown("<p style='font-size: 14px; font-weight: 700; margin: 8px 0 4px 0;'>🚘 10개의 보기 중 정답을 선택하세요:</p>", unsafe_allow_html=True)
        
        # 2열 구조로 정렬
        options = st.session_state.current_options
        row_size = 2
        for i in range(0, len(options), row_size):
            cols = st.columns(row_size)
            for j in range(row_size):
                if i + j < len(options):
                    opt = options[i + j]
                    with cols[j]:
                        if st.button(opt, key=f"opt_{st.session_state.current_q_idx}_{i+j}"):
                            if opt == current_quiz["answer"]:
                                # 정답 시 이번 문제 획득 점수 계산 후 총점에 반영
                                earned_score = max(2, 10 - (st.session_state.hint_step * 2))
                                st.session_state.earned_score = earned_score
                                st.session_state.total_score += earned_score
                                st.session_state.solved_current = True
                                st.rerun()
                            else:
                                st.error("❌ 틀렸습니다! 다른 차이거나 힌트를 더 확인해보세요.")

    # [상태 B] 정답을 맞힌 경우 독립된 '정답 화면' (폭죽 효과 발동)
    else:
        st.balloons() # 폭죽/축하 파티클 효과
        earned = st.session_state.earned_score
        st.markdown(f"""
        <div class="success-box">
            <h2 style="color: #34d399 !important; font-size: 30px; margin-bottom: 8px;">🎆 정답입니다!</h2>
            <p style="font-size: 16px; color: #f3f4f6; margin-bottom: 4px;">이번 문제 정답: <b style="color: #ffffff; text-decoration: underline;">{current_quiz['answer']}</b></p>
            <h3 style="color: #facc15 !important; font-size: 24px; margin-top: 10px;">획득 점수: +{earned}점</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # 다음 문제로 넘어가기 버튼
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

# [모든 퀴즈 완료 최종 결과 화면]
else:
    st.markdown("""
    <div class="hero-box" style="text-align: center;">
        <h2 style="color: #4ade80 !important; font-size: 26px; margin-bottom: 8px;">🏆 스무고개 챌린지 완주!</h2>
        <p style="font-size: 15px; color: #d1d5db;">모든 10지선다 명차 추리 미션을 완벽하게 마쳤습니다.</p>
    </div>
    """, unsafe_allow_html=True)
    
    final_score = st.session_state.total_score
    max_possible_total = len(quiz_list) * 10
    
    st.metric(label="최종 누적 점수", value=f"{final_score}점 / {max_possible_total}점 만점")
    
    if final_score >= 90:
        st.balloons()
        st.success("🌟 완벽한 명차 마스터! 힌트를 거의 쓰지 않고 완벽한 통찰력을 보여주셨습니다!")
    elif final_score >= 70:
        st.info("🚗 훌륭한 자동차 전문가 수준입니다! 날카로운 추리력이 돋보여요.")
    else:
        st.info("👍 수고하셨습니다! 힌트를 줄이고 다음 번에 더 높은 고득점에 도전해 보세요!")
        
    if st.button("🔄 처음부터 다시 도전하기"):
        st.session_state.started = False
        st.session_state.current_q_idx = 0
        st.session_state.hint_step = 0
        st.session_state.solved_current = False
        st.session_state.total_score = 0
        st.session_state.game_finished = False
        st.rerun()
