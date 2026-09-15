import streamlit as st
import html

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NEMO Student",
    page_icon="🐠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# SESSION STATE
# =========================================================

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

if "menu" not in st.session_state:
    st.session_state.menu = "HOME"


# =========================================================
# THEME
# =========================================================

if st.session_state.dark_mode:
    BG = "#080A0F"
    PANEL = "#11151D"
    PANEL_2 = "#171C25"
    TEXT = "#F7FAFC"
    MUTED = "#AAB6C5"
    ORANGE = "#FF7A00"
    BABY_BLUE = "#9DEBFF"
    BORDER = "#263241"
else:
    BG = "#EAF9FF"
    PANEL = "#FFFFFF"
    PANEL_2 = "#DFF5FC"
    TEXT = "#101820"
    MUTED = "#52616D"
    ORANGE = "#FF6B00"
    BABY_BLUE = "#4FCBEA"
    BORDER = "#B7DCE8"


# =========================================================
# GLOBAL CSS
# =========================================================

st.markdown(
    f"""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    * {{
        font-family: 'Space Grotesk', sans-serif;
    }}

    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    header {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    .block-container {{
        padding-top: 1.5rem;
        padding-bottom: 4rem;
        max-width: 1200px;
    }}

    /* ================= TOP BAR ================= */

    .top-bar {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-left: 4px solid {ORANGE};
        border-radius: 14px;
        padding: 10px 18px;
        margin-bottom: 25px;

        display: flex;
        justify-content: space-between;
        align-items: center;

        box-shadow: 0 0 20px rgba(255,122,0,0.08);
    }}

    .system {{
        font-family: 'Orbitron', sans-serif;
        color: {BABY_BLUE};
        font-size: 12px;
        letter-spacing: 2px;
    }}

    .status {{
        color: {ORANGE};
        font-size: 12px;
        font-weight: 700;
    }}

    /* ================= LOGO ================= */

    .logo {{
        font-family: 'Orbitron', sans-serif;
        font-size: 52px;
        font-weight: 800;
        color: {TEXT};
        letter-spacing: 5px;
        margin-bottom: -10px;
    }}

    .logo span {{
        color: {ORANGE};
    }}

    .tagline {{
        color: {BABY_BLUE};
        font-family: 'Orbitron', sans-serif;
        letter-spacing: 3px;
        font-size: 13px;
        margin-bottom: 30px;
    }}

    /* ================= SECTION ================= */

    .section-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 20px;
        color: {TEXT};
        letter-spacing: 1px;
        margin-top: 20px;
        margin-bottom: 15px;
    }}

    .section-title span {{
        color: {ORANGE};
    }}

    /* ================= FEATURE CARD ================= */

    .feature-card {{
        background: {PANEL};
        border: 1px solid {BORDER};
        border-radius: 18px;
        padding: 22px;
        min-height: 175px;

        transition: 0.2s ease;

        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    }}

    .feature-card:hover {{
        border-color: {ORANGE};
        transform: translateY(-3px);
    }}

    .feature-icon {{
        font-size: 30px;
        margin-bottom: 10px;
    }}

    .feature-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 16px;
        color: {ORANGE};
        margin-bottom: 8px;
    }}

    .feature-description {{
        color: {MUTED};
        font-size: 13px;
        line-height: 1.6;
    }}

    /* ================= INFO BOX ================= */

    .info-box {{
        background: {PANEL_2};
        border: 1px solid {BORDER};
        border-left: 4px solid {BABY_BLUE};
        border-radius: 12px;
        padding: 15px 18px;
        margin: 15px 0;
        color: {TEXT};
    }}

    /* ================= RESULT ================= */

    .result-box {{
        background: {PANEL};
        border: 1px solid {ORANGE};
        border-radius: 15px;
        padding: 20px;
        margin-top: 20px;
        text-align: center;
    }}

    .result-number {{
        font-family: 'Orbitron', sans-serif;
        font-size: 42px;
        color: {ORANGE};
        font-weight: 800;
    }}

    .result-label {{
        color: {MUTED};
        font-size: 13px;
    }}

    /* ================= SHIMEJI ================= */

    .fish-shimeji {{
        position: fixed;
        right: 22px;
        bottom: 25px;

        width: 85px;
        height: 85px;

        background: {PANEL};
        border: 2px solid {ORANGE};
        border-radius: 50%;

        display: flex;
        align-items: center;
        justify-content: center;

        font-size: 47px;

        z-index: 9999;

        animation: floatFish 3s ease-in-out infinite;

        box-shadow:
            0 0 15px rgba(255,122,0,0.25),
            0 0 30px rgba(157,235,255,0.12);
    }}

    @keyframes floatFish {{
        0% {{
            transform: translateY(0px) rotate(-2deg);
        }}

        50% {{
            transform: translateY(-10px) rotate(2deg);
        }}

        100% {{
            transform: translateY(0px) rotate(-2deg);
        }}
    }}

    .fish-label {{
        position: fixed;
        right: 25px;
        bottom: 115px;

        background: {PANEL};
        border: 1px solid {BABY_BLUE};
        border-radius: 12px;

        padding: 9px 12px;
        max-width: 190px;

        color: {TEXT};
        font-size: 11px;
        line-height: 1.4;

        z-index: 9998;

        box-shadow: 0 5px 20px rgba(0,0,0,0.15);
    }}

    .fish-label b {{
        color: {ORANGE};
    }}

    /* ================= FOOTER ================= */

    .footer {{
        text-align: center;
        color: {MUTED};
        font-size: 11px;
        margin-top: 50px;
        letter-spacing: 1px;
    }}

    /* ================= STREAMLIT BUTTON ================= */

    div.stButton > button {{
        border: 1px solid {ORANGE};
        border-radius: 10px;
        background: {PANEL};
        color: {TEXT};
        font-weight: 600;
        transition: 0.2s;
    }}

    div.stButton > button:hover {{
        background: {ORANGE};
        color: #000000;
        border-color: {ORANGE};
    }}

    /* ================= INPUT ================= */

    input, textarea {{
        border-radius: 10px !important;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# SHIMEJI
# =========================================================

tips = {
    "HOME": "Hai! Aku NEMO 🐠<br><b>Tip:</b> Pilih fitur yang mau kamu gunakan.",
    "CEK NILAI": "Mau cek nilai?<br><b>Tip:</b> Masukkan nilai tiap mata pelajaran.",
    "PRIORITAS TUGAS": "Deadline mengejar? 😭<br><b>Tip:</b> Masukkan deadline dan tingkat kesulitan tugas.",
    "STUDY PLANNER": "Waktunya belajar.<br><b>Tip:</b> Masukkan waktu belajar yang tersedia.",
    "DUID TRACKER": "Uangmu sedang diamati. 👁️<br><b>Tip:</b> Catat pemasukan dan pengeluaranmu.",
    "ABOUT": "Aku NEMO!<br><b>Know What Matters.</b>"
}

current_tip = tips.get(
    st.session_state.menu,
    "Halo! Aku NEMO 🐠"
)

st.markdown(
    f"""
    <div class="fish-label">
        {current_tip}
    </div>

    <div class="fish-shimeji">
        🐠
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# TOP BAR
# =========================================================

st.markdown(
    f"""
    <div class="top-bar">
        <div class="system">NEMO SYSTEM // ONLINE</div>
        <div class="status">● READY</div>
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="logo">NEM<span>O</span></div>
    <div class="tagline">KNOW WHAT MATTERS</div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# THEME BUTTON
# =========================================================

theme_col1, theme_col2 = st.columns([5, 1])

with theme_col2:

    if st.session_state.dark_mode:
        button_text = "☀️ LIGHT"
    else:
        button_text = "🌙 DARK"

    if st.button(button_text, use_container_width=True):
        st.session_state.dark_mode = not st.session_state.dark_mode
        st.rerun()


# =========================================================
# NAVIGATION
# =========================================================

st.markdown(
    '<div class="section-title">SELECT <span>MODULE</span></div>',
    unsafe_allow_html=True
)

nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    if st.button("⌂ HOME", use_container_width=True):
        st.session_state.menu = "HOME"

with nav2:
    if st.button("▣ NILAI", use_container_width=True):
        st.session_state.menu = "CEK NILAI"

with nav3:
    if st.button("⚡ TUGAS", use_container_width=True):
        st.session_state.menu = "PRIORITAS TUGAS"

with nav4:
    if st.button("◷ STUDY", use_container_width=True):
        st.session_state.menu = "STUDY PLANNER"

with nav5:
    if st.button("Rp DUIT", use_container_width=True):
        st.session_state.menu = "DUID TRACKER"


# =========================================================
# HOME
# =========================================================

if st.session_state.menu == "HOME":

    st.markdown(
        '<div class="section-title">NEMO <span>FEATURES</span></div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c1:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">CEK NILAI</div>
                <div class="feature-description">
                    Hitung rata-rata nilai dan lihat status
                    performa akademikmu secara sederhana.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">PRIORITAS TUGAS</div>
                <div class="feature-description">
                    Tentukan tugas mana yang harus dikerjakan
                    terlebih dahulu berdasarkan deadline dan kesulitan.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    c3, c4 = st.columns(2)

    with c3:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <div class="feature-title">STUDY PLANNER</div>
                <div class="feature-description">
                    Atur pembagian waktu belajar supaya
                    kegiatan akademikmu lebih terstruktur.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c4:
        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">💸</div>
                <div class="feature-title">DUid TRACKER</div>
                <div class="feature-description">
                    Catat pemasukan dan pengeluaran untuk mengetahui
                    kondisi keuanganmu.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="info-box">
            <b>🐠 NEMO STATUS</b><br>
            Your student life management system is ready.
            Choose a module above to begin.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# CEK NILAI
# =========================================================

elif st.session_state.menu == "CEK NILAI":

    st.markdown(
        '<div class="section-title">MODULE // <span>CEK NILAI</span></div>',
        unsafe_allow_html=True
    )

    st.write(
        "Masukkan nilai mata pelajaran untuk menghitung rata-rata."
    )

    jumlah_mapel = st.number_input(
        "Jumlah mata pelajaran",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )

    nilai = []

    for i in range(jumlah_mapel):

        col1, col2 = st.columns([3, 1])

        with col1:
            nama = st.text_input(
                f"Nama mata pelajaran {i + 1}",
                key=f"mapel_{i}"
            )

        with col2:
            angka = st.number_input(
                "Nilai",
                min_value=0.0,
                max_value=100.0,
                value=75.0,
                key=f"nilai_{i}"
            )

        nilai.append(angka)

    if st.button(
        "CALCULATE RESULT",
        use_container_width=True
    ):

        rata = sum(nilai) / len(nilai)

        if rata >= 90:
            status = "EXCELLENT"
        elif rata >= 80:
            status = "GOOD"
        elif rata >= 70:
            status = "NEED IMPROVEMENT"
        else:
            status = "KEEP GOING"

        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-label">AVERAGE SCORE</div>
                <div class="result-number">{rata:.2f}</div>
                <div class="result-label">{status}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# PRIORITAS TUGAS
# =========================================================

elif st.session_state.menu == "PRIORITAS TUGAS":

    st.markdown(
        '<div class="section-title">MODULE // <span>PRIORITAS TUGAS</span></div>',
        unsafe_allow_html=True
    )

    st.write(
        "Semakin dekat deadline dan semakin sulit tugasnya, "
        "semakin tinggi prioritasnya."
    )

    jumlah_tugas = st.number_input(
        "Jumlah tugas",
        min_value=1,
        max_value=20,
        value=4,
        step=1
    )

    tugas = []

    for i in range(jumlah_tugas):

        st.markdown(f"### Task {i + 1}")

        nama = st.text_input(
            "Nama tugas",
            key=f"task_name_{i}"
        )

        col1, col2 = st.columns(2)

        with col1:
            deadline = st.number_input(
                "Hari menuju deadline",
                min_value=0,
                max_value=365,
                value=7,
                key=f"deadline_{i}"
            )

        with col2:
            kesulitan = st.slider(
                "Tingkat kesulitan",
                min_value=1,
                max_value=5,
                value=3,
                key=f"difficulty_{i}"
            )

        # Semakin sedikit hari, semakin tinggi skor
        urgency = max(1, 30 - deadline)

        score = urgency + (kesulitan * 5)

        tugas.append(
            {
                "nama": nama if nama else f"Tugas {i + 1}",
                "deadline": deadline,
                "kesulitan": kesulitan,
                "score": score
            }
        )

    if st.button(
        "GENERATE PRIORITY",
        use_container_width=True
    ):

        tugas.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        st.markdown(
            '<div class="section-title">PRIORITY <span>QUEUE</span></div>',
            unsafe_allow_html=True
        )

        for index, task in enumerate(tugas):

            if index == 0:
                level = "🔥 VERY HIGH"
            elif index == 1:
                level = "🟠 HIGH"
            else:
                level = "🔵 NORMAL"

            st.markdown(
                f"""
                <div class="info-box">
                    <b>#{index + 1} {html.escape(task["nama"])}</b><br>
                    Deadline: {task["deadline"]} hari lagi<br>
                    Kesulitan: {task["kesulitan"]}/5<br>
                    Priority: {level}
                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# STUDY PLANNER
# =========================================================

elif st.session_state.menu == "STUDY PLANNER":

    st.markdown(
        '<div class="section-title">MODULE // <span>STUDY PLANNER</span></div>',
        unsafe_allow_html=True
    )

    waktu = st.number_input(
        "Waktu belajar tersedia (menit)",
        min_value=15,
        max_value=1440,
        value=120,
        step=15
    )

    jumlah = st.number_input(
        "Jumlah tugas/materi",
        min_value=1,
        max_value=20,
        value=4,
        step=1
    )

    materi = []

    for i in range(jumlah):

        nama = st.text_input(
            f"Materi/Tugas {i + 1}",
            key=f"study_{i}"
        )

        materi.append(
            nama if nama else f"Materi {i + 1}"
        )

    if st.button(
        "CREATE STUDY PLAN",
        use_container_width=True
    ):

        pembagian = waktu / jumlah

        st.markdown(
            '<div class="section-title">YOUR <span>STUDY PLAN</span></div>',
            unsafe_allow_html=True
        )

        for i, item in enumerate(materi):

            st.markdown(
                f"""
                <div class="info-box">
                    <b>SESSION {i + 1}</b><br>
                    {html.escape(item)}<br>
                    ⏱️ {pembagian:.0f} menit
                </div>
                """,
                unsafe_allow_html=True
            )

        st.success(
            f"Total waktu belajar: {waktu} menit."
        )


# =========================================================
# DUid TRACKER
# =========================================================

elif st.session_state.menu == "DUID TRACKER":

    st.markdown(
        '<div class="section-title">MODULE // <span>DUid TRACKER</span></div>',
        unsafe_allow_html=True
    )

    pemasukan = st.number_input(
        "Total pemasukan",
        min_value=0.0,
        value=0.0,
        step=1000.0
    )

    jumlah_pengeluaran = st.number_input(
        "Jumlah pengeluaran",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )

    total_pengeluaran = 0.0

    for i in range(jumlah_pengeluaran):

        col1, col2 = st.columns([2, 1])

        with col1:

            kategori = st.text_input(
                f"Kategori pengeluaran {i + 1}",
                key=f"expense_name_{i}"
            )

        with col2:

            nominal = st.number_input(
                "Nominal",
                min_value=0.0,
                value=0.0,
                step=1000.0,
                key=f"expense_value_{i}"
            )

        total_pengeluaran += nominal

    if st.button(
        "CALCULATE MONEY",
        use_container_width=True
    ):

        sisa = pemasukan - total_pengeluaran

        if sisa > 0:
            status = "MONEY REMAINING"
        elif sisa == 0:
            status = "BALANCED"
        else:
            status = "OVER BUDGET"

                st.markdown(
            f"""
            <div class="result-box">
                <div class="result-label">REMAINING MONEY</div>
                <div class="result-number">
                    Rp {sisa:,.0f}
                </div>
                <div class="result-label">
                    {status}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# ABOUT
# =========================================================

elif st.session_state.menu == "ABOUT":

    st.markdown(
        '<div class="section-title">SYSTEM // <span>ABOUT NEMO</span></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="feature-card">

            <div class="feature-title">
                NEMO STUDENT
            </div>

            <div class="feature-description">

                NEMO Student adalah Student Life Management Assistant
                yang dirancang untuk membantu pelajar mengelola kebutuhan
                sehari-hari dalam satu platform.

                <br><br>

                NEMO memiliki empat fitur utama:

                <br><br>

                📊 <b>Cek Nilai</b><br>
                Menghitung rata-rata nilai.

                <br><br>

                ⚡ <b>Prioritas Tugas</b><br>
                Menentukan tugas berdasarkan deadline dan kesulitan.

                <br><br>

                📚 <b>Study Planner</b><br>
                Membantu membagi waktu belajar.

                <br><br>

                💸 <b>Duid Tracker</b><br>
                Mencatat pemasukan dan pengeluaran.

                <br><br>

                Dibangun menggunakan Python dan Streamlit.

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        NEMO STUDENT // KNOW WHAT MATTERS<br>
        SYSTEM DESIGNED FOR STUDENT LIFE
    </div>
    """,
    unsafe_allow_html=True
)
