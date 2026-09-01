import streamlit as st
from datetime import datetime


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="NEMO // Student System",
    page_icon="🐟",
    layout="centered",
    initial_sidebar_state="collapsed"
)


# ============================================================
# SESSION STATE
# ============================================================

if "menu" not in st.session_state:
    st.session_state.menu = "HOME"

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

if "mood" not in st.session_state:
    st.session_state.mood = 70


# ============================================================
# THEME
# ============================================================

if st.session_state.dark_mode:

    # DARK MODE
    BG = "#BFEFFF"
    PANEL = "#11131A"
    PANEL_2 = "#1A1D27"
    TEXT = "#FFFFFF"
    MUTED = "#D7E9F0"
    PINK = "#FF4FA3"
    CYAN = "#19D9FF"
    BORDER = "#19D9FF"

else:

    # LIGHT MODE
    BG = "#173A63"
    PANEL = "#FFFFFF"
    PANEL_2 = "#EEF9FF"
    TEXT = "#111827"
    MUTED = "#26384A"
    PINK = "#FF4FA3"
    CYAN = "#13BFE8"
    BORDER = "#FF4FA3"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&display=swap'
);


/* ============================================================
   GLOBAL
   ============================================================ */

html,
body,
[class*="css"] {{
    font-family: 'Nunito', sans-serif !important;
}}

.stApp {{
    background:
        radial-gradient(
            circle at 10% 10%,
            rgba(255, 79, 163, 0.15),
            transparent 25%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(25, 217, 255, 0.12),
            transparent 25%
        ),
        {BG} !important;
}}

.main .block-container {{
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}}


/* ============================================================
   REMOVE STREAMLIT DEFAULT
   ============================================================ */

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}


/* ============================================================
   TOP BAR
   ============================================================ */

.top-bar {{
    display: flex;
    justify-content: space-between;
    align-items: center;

    background: {PANEL};

    border: 2px solid {BORDER};

    border-radius: 14px;

    padding: 10px 16px;

    margin-bottom: 18px;

    box-shadow:
        5px 5px 0px rgba(0,0,0,0.20);
}}

.top-left {{
    color: {TEXT} !important;
    font-size: 13px;
    font-weight: 900;
    letter-spacing: 1px;
}}

.live-dot {{
    display: inline-block;

    width: 9px;
    height: 9px;

    background: {PINK};

    border-radius: 50%;

    margin-right: 6px;

    box-shadow:
        0 0 10px {PINK};
}}

.top-right {{
    color: {PINK} !important;
    font-size: 12px;
    font-weight: 900;
}}


/* ============================================================
   LOGO
   ============================================================ */

.logo-box {{
    text-align: center;

    padding: 8px;
}}

.logo {{
    font-size: 64px;

    font-weight: 900;

    color: {PINK} !important;

    text-shadow:
        3px 3px 0px {CYAN},
        6px 6px 0px rgba(0,0,0,0.20);

    letter-spacing: -4px;

    margin-bottom: 0;
}}

.logo-sub {{
    color: {TEXT} !important;

    font-size: 13px;

    font-weight: 900;

    letter-spacing: 3px;

    text-transform: uppercase;
}}


/* ============================================================
   STATUS PANEL
   ============================================================ */

.status-panel {{
    background: {PANEL};

    border: 2px solid {CYAN};

    border-radius: 18px;

    padding: 18px;

    margin-top: 20px;

    box-shadow:
        6px 6px 0px rgba(0,0,0,0.20);
}}

.status-label {{
    color: {PINK} !important;

    font-size: 11px;

    font-weight: 900;

    letter-spacing: 2px;
}}

.status-title {{
    color: {TEXT} !important;

    font-size: 22px;

    font-weight: 900;

    margin-top: 2px;
}}

.status-description {{
    color: {MUTED} !important;

    font-size: 13px;

    font-weight: 600;
}}


/* ============================================================
   FEATURE CARD
   ============================================================ */

.feature-card {{
    background: {PANEL};

    border: 2px solid {BORDER};

    border-radius: 16px;

    padding: 18px;

    min-height: 150px;

    margin-top: 10px;

    box-shadow:
        5px 5px 0px rgba(0,0,0,0.20);

    transition: 0.15s;
}}

.feature-icon {{
    font-size: 30px;
}}

.feature-title {{
    color: {TEXT} !important;

    font-size: 18px;

    font-weight: 900;

    margin-top: 7px;
}}

.feature-description {{
    color: {MUTED} !important;

    font-size: 12px;

    font-weight: 600;

    line-height: 1.5;

    margin-top: 5px;
}}


/* ============================================================
   BUTTON
   ============================================================ */

div.stButton > button {{

    width: 100%;

    min-height: 44px;

    border-radius: 12px;

    border: 2px solid {TEXT} !important;

    background: {PINK} !important;

    color: #111827 !important;

    font-family: 'Nunito', sans-serif !important;

    font-size: 13px;

    font-weight: 900;

    box-shadow:
        4px 4px 0px #111827;

    transition: 0.1s;
}}

div.stButton > button:hover {{

    background: {CYAN} !important;

    color: #111827 !important;

    transform: translate(
        2px,
        2px
    );

    box-shadow:
        2px 2px 0px #111827;
}}


/* ============================================================
   INPUT
   ============================================================ */

.stTextInput label,
.stNumberInput label,
.stSlider label,
.stSelectbox label {{

    color: {TEXT} !important;

    font-weight: 800 !important;
}}

.stTextInput input,
.stNumberInput input {{

    background: {PANEL} !important;

    color: {TEXT} !important;

    border: 2px solid {CYAN} !important;

    border-radius: 10px !important;

    font-weight: 700 !important;
}}


/* ============================================================
   HEADINGS
   ============================================================ */

h1,
h2,
h3,
h4 {{

    color: {TEXT} !important;

    font-family:
        'Nunito',
        sans-serif !important;

    font-weight: 900 !important;
}}


/* ============================================================
   NORMAL TEXT
   ============================================================ */

p {{

    color: {TEXT} !important;
}}


/* ============================================================
   METRIC
   ============================================================ */

[data-testid="stMetric"] {{

    background: {PANEL};

    border: 2px solid {CYAN};

    border-radius: 12px;

    padding: 10px;
}}

[data-testid="stMetricValue"] {{

    color: {PINK} !important;

    font-weight: 900 !important;
}}

[data-testid="stMetricLabel"] {{

    color: {TEXT} !important;

    font-weight: 800 !important;
}}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {{

    border-color: {CYAN} !important;

    opacity: 0.6;
}}


/* ============================================================
   FOOTER
   ============================================================ */

.nemo-footer {{

    text-align: center;

    color: {TEXT} !important;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 1px;

    margin-top: 35px;
}}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# CARD FUNCTION
# ============================================================

def feature_card(icon, title, description):

    st.markdown(
        f"""
<div class="feature-card">
    <div class="feature-icon">{icon}</div>
    <div class="feature-title">{title}</div>
    <div class="feature-description">{description}</div>
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
# TOP BAR
# ============================================================

now = datetime.now().strftime("%H:%M")

st.markdown(
    f"""
<div class="top-bar">

    <div class="top-left">
        <span class="live-dot"></span>
        NEMO SYSTEM ONLINE
    </div>

    <div class="top-right">
        {now} // STUDENT MODE
    </div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# LOGO
# ============================================================

st.markdown(
    """
<div class="logo-box">

    <div class="logo">
        🐟 NEMO
    </div>

    <div class="logo-sub">
        KNOW WHAT MATTERS.
    </div>

</div>
""",
    unsafe_allow_html=True
)


# ============================================================
# THEME SWITCH
# ============================================================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.session_state.dark_mode:

        if st.button(
            "☀️ SWITCH TO LIGHT MODE",
            key="theme_button"
        ):

            st.session_state.dark_mode = False
            st.rerun()

    else:

        if st.button(
            "🌙 SWITCH TO DARK MODE",
            key="theme_button"
        ):

            st.session_state.dark_mode = True
            st.rerun()


# ============================================================
# HOME
# ============================================================

if st.session_state.menu == "HOME":

    st.markdown(
        """
<div class="status-panel">

    <div class="status-label">
        CURRENT STATUS
    </div>

    <div class="status-title">
        Student Mode: ACTIVE
    </div>

    <div class="status-description">
        Manage your grades, tasks, study time,
        and money in one place.
    </div>

</div>
""",
        unsafe_allow_html=True
    )


    st.markdown(
        """
<div style="
    text-align:center;
    margin-top:28px;
    margin-bottom:10px;
">

<span style="
    color:#FF4FA3;
    font-size:13px;
    font-weight:900;
    letter-spacing:2px;
">
SELECT MODULE
</span>

</div>
""",
        unsafe_allow_html=True
    )


    # ========================================================
    # ROW 1
    # ========================================================

    col1, col2 = st.columns(2)

    with col1:

        feature_card(
            "📊",
            "CEK NILAI",
            "Calculate your average score and "
            "see your academic performance."
        )

        if st.button(
            "OPEN MODULE →",
            key="nilai"
        ):

            st.session_state.menu = "CEK_NILAI"
            st.rerun()


    with col2:

        feature_card(
            "📋",
            "PRIORITAS TUGAS",
            "Sort your assignments based on "
            "deadline and difficulty."
        )

        if st.button(
            "OPEN MODULE →",
            key="prioritas"
        ):

            st.session_state.menu = "PRIORITAS"
            st.rerun()


    # ========================================================
    # ROW 2
    # ========================================================

    col1, col2 = st.columns(2)

    with col1:

        feature_card(
            "⏰",
            "STUDY PLANNER",
            "Divide your available study time "
            "between your tasks."
        )

        if st.button(
            "OPEN MODULE →",
            key="planner"
        ):

            st.session_state.menu = "PLANNER"
            st.rerun()


    with col2:

        feature_card(
            "💸",
            "DUID TRACKER",
            "Track your income, spending, "
            "and remaining money."
        )

        if st.button(
            "OPEN MODULE →",
            key="duid"
        ):

            st.session_state.menu = "DUID"
            st.rerun()


    st.divider()


    if st.button(
        "ℹ️ ABOUT NEMO",
        key="about"
    ):

        st.session_state.menu = "ABOUT"
        st.rerun()


# ============================================================
# CEK NILAI
# ============================================================

elif st.session_state.menu == "CEK_NILAI":

    if st.button(
        "← BACK TO HOME",
        key="back_nilai"
    ):

        st.session_state.menu = "HOME"
        st.rerun()


    st.header("📊 CEK NILAI")

    st.write(
        "Enter your subject names and scores."
    )


    jumlah = st.number_input(
        "NUMBER OF SUBJECTS",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )


    nilai = []


    for i in range(int(jumlah)):

        col1, col2 = st.columns(2)

        with col1:

            nama = st.text_input(
                f"SUBJECT {i + 1}",
                key=f"subject_{i}"
            )

        with col2:

            angka = st.number_input(
                f"SCORE {i + 1}",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                key=f"score_{i}"
            )

        if nama:

            nilai.append(angka)


    if st.button(
        "CALCULATE RESULT",
        key="calculate"
    ):

        if not nilai:

            st.warning(
                "Enter at least one subject."
            )

        else:

            rata = sum(nilai) / len(nilai)


            if rata >= 90:

                predikat = "EXCELLENT"

            elif rata >= 80:

                predikat = "GOOD"

            elif rata >= 70:

                predikat = "OKAY"

            else:

                predikat = "NEEDS WORK"


            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "AVERAGE",
                    f"{rata:.2f}"
                )

            with col2:

                st.metric(
                    "STATUS",
                    predikat
                )


# ============================================================
# PRIORITAS
# ============================================================

elif st.session_state.menu == "PRIORITAS":

    if st.button(
        "← BACK TO HOME",
        key="back_prioritas"
    ):

        st.session_state.menu = "HOME"
        st.rerun()


    st.header("📋 PRIORITAS TUGAS")

    st.write(
        "NEMO calculates priority from deadline "
        "and difficulty."
    )


    jumlah = st.number_input(
        "NUMBER OF TASKS",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )


    tugas = []


    for i in range(int(jumlah)):

        st.subheader(
            f"TASK {i + 1}"
        )

        nama = st.text_input(
            "TASK NAME",
            key=f"task_name_{i}"
        )

        deadline = st.number_input(
            "DAYS LEFT",
            min_value=0,
            max_value=365,
            value=3,
            key=f"task_deadline_{i}"
        )

        kesulitan = st.slider(
            "DIFFICULTY",
            min_value=1,
            max_value=5,
            value=3,
            key=f"task_difficulty_{i}"
        )


        if nama:

            if deadline <= 1:
                urgensi = 5

            elif deadline <= 3:
                urgensi = 4

            elif deadline <= 5:
                urgensi = 3

            elif deadline <= 7:
                urgensi = 2

            else:
                urgensi = 1


            skor = urgensi + kesulitan


            tugas.append(
                {
                    "nama": nama,
                    "deadline": deadline,
                    "kesulitan": kesulitan,
                    "skor": skor
                }
            )


    if st.button(
        "GENERATE PRIORITY",
        key="generate_priority"
    ):

        if not tugas:

            st.warning(
                "Enter at least one task."
            )

        else:

            tugas.sort(
                key=lambda x: x["skor"],
                reverse=True
            )


            st.subheader(
                "PRIORITY QUEUE"
            )


            for i, task in enumerate(
                tugas,
                1
            ):

                if task["skor"] >= 8:

                    status = "🔴 HIGH"

                elif task["skor"] >= 5:

                    status = "🟠 MEDIUM"

                else:

                    status = "🔵 LOW"


                st.write(
                    f"**#{i} — {task['nama']}**"
                )

                st.write(
                    f"Deadline: "
                    f"{task['deadline']} day(s)"
                )

                st.write(
                    f"Difficulty: "
                    f"{task['kesulitan']}/5"
                )

                st.write(
                    f"Priority: {status}"
                )

                st.divider()


# ============================================================
# STUDY PLANNER
# ============================================================

elif st.session_state.menu == "PLANNER":

    if st.button(
        "← BACK TO HOME",
        key="back_planner"
    ):

        st.session_state.menu = "HOME"
        st.rerun()


    st.header("⏰ STUDY PLANNER")

    st.write(
        "Tell NEMO how much time you have."
    )


    waktu = st.number_input(
        "AVAILABLE TIME (HOURS)",
        min_value=0.5,
        max_value=24.0,
        value=2.0,
        step=0.5
    )


    jumlah = st.number_input(
        "NUMBER OF TASKS",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )


    if st.button(
        "GENERATE PLAN",
        key="generate_plan"
    ):

        per_tugas = waktu / jumlah


        st.success(
            "PLAN GENERATED."
        )


        st.metric(
            "TIME PER TASK",
            f"{per_tugas:.2f} HOURS"
        )


        if per_tugas >= 2:

            st.info(
                "You have enough time. "
                "Focus on quality."
            )

        elif per_tugas >= 1:

            st.info(
                "Time is limited. "
                "Stay focused."
            )

        else:

            st.warning(
                "Very limited time. "
                "Start with your highest priority task."
            )


# ============================================================
# DUID TRACKER
# ============================================================

elif st.session_state.menu == "DUID":

    if st.button(
        "← BACK TO HOME",
        key="back_duid"
    ):

        st.session_state.menu = "HOME"
        st.rerun()


    st.header("💸 DUID TRACKER")

    st.write(
        "Track your simple daily finances."
    )


    pemasukan = st.number_input(
        "INCOME",
        min_value=0.0,
        value=100000.0,
        step=10000.0
    )


    jumlah = st.number_input(
        "NUMBER OF EXPENSES",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )


    total = 0


    for i in range(int(jumlah)):

        col1, col2 = st.columns(2)

        with col1:

            st.text_input(
                f"CATEGORY {i + 1}",
                key=f"category_{i}"
            )

        with col2:

            nominal = st.number_input(
                f"AMOUNT {i + 1}",
                min_value=0.0,
                value=0.0,
                step=1000.0,
                key=f"amount_{i}"
            )

            total += nominal


    if st.button(
        "CALCULATE MONEY",
        key="calculate_money"
    ):

        sisa = pemasukan - total


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "INCOME",
                f"Rp{pemasukan:,.0f}"
            )


        with col2:

            st.metric(
                "SPENT",
                f"Rp{total:,.0f}"
            )


        with col3:

            st.metric(
                "LEFT",
                f"Rp{sisa:,.0f}"
            )


        if sisa < 0:

            st.error(
                "WARNING: Spending exceeded income."
            )

        elif sisa == 0:

            st.warning(
                "Your balance is zero."
            )

        else:

            st.success(
                "Balance looks okay."
            )


# ============================================================
# ABOUT
# ============================================================

elif st.session_state.menu == "ABOUT":

    if st.button(
        "← BACK TO HOME",
        key="back_about"
    ):

        st.session_state.menu = "HOME"
        st.rerun()


    st.header("🐟 ABOUT NEMO")


    st.markdown(
        """
### KNOW WHAT MATTERS.

NEMO is a simple **Student Life Management Assistant**
designed to put several everyday student tools into one
small digital platform.

Instead of jumping between different calculators,
notes, and random websites, NEMO keeps the basic stuff
in one place.

---

### MODULES

📊 **CEK NILAI**

Calculate academic averages.

📋 **PRIORITAS TUGAS**

Sort assignments based on urgency and difficulty.

⏰ **STUDY PLANNER**

Divide available study time between tasks.

💸 **DUID TRACKER**

Calculate income, expenses, and remaining money.

---

### BUILT WITH

🐍 Python  
⚡ Streamlit  
🌐 GitHub  

---

**NEMO // KNOW WHAT MATTERS.**
"""
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
<div class="nemo-footer">

NEMO // STUDENT SYSTEM // v1.0

</div>
""",
    unsafe_allow_html=True
)
