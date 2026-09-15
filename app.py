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
# COLOR THEME
# =========================================================

if st.session_state.dark_mode:
    BG = "#080A0F"
    PANEL = "#11151D"
    PANEL_2 = "#171C25"
    TEXT = "#F7FAFC"
    MUTED = "#AAB6C5"
    ORANGE = "#FF7A00"
    BLUE = "#9DEBFF"
    BORDER = "#263241"
else:
    BG = "#EAF9FF"
    PANEL = "#FFFFFF"
    PANEL_2 = "#DFF5FC"
    TEXT = "#101820"
    MUTED = "#52616D"
    ORANGE = "#FF6B00"
    BLUE = "#4FCBEA"
    BORDER = "#B7DCE8"

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    f"""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    * {{
        box-sizing: border-box;
    }}

    html, body, [class*="css"] {{
        font-family: 'Space Grotesk', sans-serif;
    }}

    .stApp {{
        background: {BG};
        color: {TEXT};
    }}

    .block-container {{
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 5rem;
    }}

    /* TOP BAR */

    .topbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 18px 24px;
        margin-bottom: 28px;

        background: {PANEL};
        border: 1px solid {BORDER};
        border-radius: 18px;

        box-shadow: 0 10px 30px rgba(0,0,0,0.12);
    }}

    .logo {{
        font-family: 'Orbitron', sans-serif;
        font-size: 26px;
        font-weight: 800;
        color: {ORANGE};
        letter-spacing: 3px;
    }}

    .logo span {{
        color: {BLUE};
    }}

    .subtitle {{
        font-size: 12px;
        color: {MUTED};
        margin-top: 3px;
        letter-spacing: 1px;
    }}

    /* TITLES */

    .page-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 38px;
        font-weight: 800;
        color: {TEXT};
        margin-bottom: 4px;
    }}

    .page-title span {{
        color: {ORANGE};
    }}

    .page-subtitle {{
        color: {MUTED};
        font-size: 15px;
        margin-bottom: 28px;
    }}

    .section-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 20px;
        color: {BLUE};
        margin-top: 20px;
        margin-bottom: 15px;
    }}

    /* FEATURE CARDS */

    .feature-card {{
    background: {PANEL};
    border: 1px solid {BORDER};
    border-radius: 18px;
    padding: 24px;
    min-height: 180px;
    margin-bottom: 18px;

    box-shadow: 0 8px 24px rgba(0,0,0,0.10);
}}

    /* INFO BOX */

    .info-box {{
        background: {PANEL_2};
        border-left: 4px solid {BLUE};
        border-radius: 12px;
        padding: 16px 18px;
        margin: 15px 0;
        color: {TEXT};
    }}

    /* RESULT */

    .result-box {{
        background: {PANEL};
        border: 1px solid {ORANGE};
        border-radius: 18px;
        padding: 25px;
        margin-top: 20px;
        text-align: center;
    }}

    .result-label {{
        color: {MUTED};
        font-size: 13px;
        letter-spacing: 1px;
        margin: 6px;
    }}

    .result-number {{
        font-family: 'Orbitron', sans-serif;
        font-size: 38px;
        font-weight: 800;
        color: {ORANGE};
        margin: 8px;
    }}

    .result-status {{
        font-family: 'Orbitron', sans-serif;
        font-size: 17px;
        color: {BLUE};
        font-weight: 700;
    }}

    /* INPUTS */

    .stTextInput label,
    .stNumberInput label,
    .stSelectbox label,
    .stSlider label {{
        color: {TEXT} !important;
        font-weight: 600 !important;
    }}

    input {{
        border-radius: 10px !

    /* BUTTONS */

    .stButton > button {{
        border-radius: 10px;
        border: 1px solid {BORDER};
        font-weight: 700;
        transition: 0.2s;
    }}

    .stButton > button:hover {{
        border-color: {ORANGE};
        color: {ORANGE};
    }}

    /* FOOTER */

    .footer {{
        margin-top: 60px;
        padding-top: 20px;

        border-top: 1px solid {BORDER};

        text-align: center;

        color: {MUTED};
        font-family: 'Orbitron', sans-serif;
        font-size: 10px;
        letter-spacing: 2px;
        line-height: 1.8;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# HEADER
# =========================================================

header_html = (
    '<div class="topbar">'
    '<div>'
    '<div class="logo">NE<span>MO</span></div>'
    '<div class="subtitle">STUDENT LIFE MANAGEMENT ASSISTANT</div>'
    '</div>'
    '</div>'
)

st.markdown(header_html, unsafe_allow_html=True)

# =========================================================
# NAVIGATION
# =========================================================

nav1, nav2, nav3, nav4, nav5, nav6 = st.columns(6)

with nav1:
    if st.button("HOME", use_container_width=True):
        st.session_state.menu = "HOME"

with nav2:
    if st.button("NILAI", use_container_width=True):
        st.session_state.menu = "CEK NILAI"

with nav3:
    if st.button("TUGAS", use_container_width=True):
        st.session_state.menu = "PRIORITAS TUGAS"

with nav4:
    if st.button("STUDY", use_container_width=True):
        st.session_state.menu = "STUDY PLANNER"

with nav5:
    if st.button("DUIT", use_container_width=True):
        st.session_state.menu = "DUID TRACKER"

with nav6:
    if st.button("ABOUT", use_container_width=True):
        st.session_state.menu = "ABOUT"

st.write("")

# =========================================================
# HOME
# =========================================================

if st.session_state.menu == "HOME":

    st.markdown(
        """
        <div class="page-title">
            KNOW WHAT <span>MATTERS.</span>
        </div>

        <div class="page-subtitle">
            NEMO membantu kamu mengatur kehidupan sekolah tanpa harus
            mengandalkan ingatan yang kadang suka menghilang entah ke mana.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📊</div>
                <div class="feature-title">CEK NILAI</div>
                <div class="feature-description">
                    Hitung rata-rata nilai dan lihat status akademikmu
                    dengan cepat.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">📚</div>
                <div class="feature-title">STUDY PLANNER</div>
                <div class="feature-description">
                    Atur waktu belajar dan bagi waktu secara sederhana
                    berdasarkan materi yang harus dipelajari.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <div class="feature-title">PRIORITAS TUGAS</div>
                <div class="feature-description">
                    Tentukan tugas mana yang harus dikerjakan lebih dulu
                    berdasarkan deadline dan tingkat kesulitan.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="feature-card">
                <div class="feature-icon">💰</div>
                <div class="feature-title">DUID TRACKER</div>
                <div class="feature-description">
                    Catat pemasukan dan pengeluaran supaya uangmu
                    tidak lenyap secara misterius.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="info-box">
            <b>NEMO STATUS:</b><br>
            SYSTEM READY // STUDENT MODE ACTIVE
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# CEK NILAI
# =========================================================

elif st.session_state.menu == "CEK NILAI":

    st.markdown(
        """
        <div class="page-title">
            CEK <span>NILAI</span>
        </div>

        <div class="page-subtitle">
            Masukkan nilai setiap mata pelajaran untuk menghitung rata-rata.
        </div>
        """,
        unsafe_allow_html=True
    )

    jumlah_mapel = st.number_input(
        "Jumlah mata pelajaran",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )

    nilai_list = []

    for i in range(jumlah_mapel):

        col1, col2 = st.columns([2, 1])

        with col1:
            nama = st.text_input(
                f"Nama mata pelajaran {i + 1}",
                key=f"mapel_{i}"
            )

        with col2:
            nilai = st.number_input(
                f"Nilai {i + 1}",
                min_value=0.0,
                max_value=100.0,
                value=75.0,
                step=1.0,
                key=f"nilai_{i}"
            )

        nilai_list.append(nilai)

    if st.button(
        "CALCULATE SCORE",
        use_container_width=True
    ):

        rata_rata = sum(nilai_list) / len(nilai_list)

        if rata_rata >= 90:
            status = "EXCELLENT"
        elif rata_rata >= 80:
            status = "GOOD"
        elif rata_rata >= 70:
            status = "NEED IMPROVEMENT"
        else:
            status = "KEEP GOING"

        st.markdown(
            f"""
            <div class="result-box">

                <div class="result-label">
                    AVERAGE SCORE
                </div>

                <div class="result-number">
                    {rata_rata:.2f}
                </div>

                <div class="result-status">
                    {status}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# PRIORITAS TUGAS
# =========================================================

elif st.session_state.menu == "PRIORITAS TUGAS":

    st.markdown(
        """
        <div class="page-title">
            PRIORITAS <span>TUGAS</span>
        </div>

        <div class="page-subtitle">
            Tentukan tugas mana yang perlu diselesaikan terlebih dahulu.
        </div>
        """,
        unsafe_allow_html=True
    )

    jumlah_tugas = st.number_input(
        "Jumlah tugas",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )

    daftar_tugas = []

    for i in range(jumlah_tugas):

        st.markdown(
            f'<div class="section-title">TASK {i + 1}</div>',
            unsafe_allow_html=True
        )

        nama = st.text_input(
            "Nama tugas",
            key=f"task_name_{i}"
        )

        col1, col2 = st.columns(2)

        with col1:
            deadline = st.number_input(
                "Deadline dalam berapa hari?",
                min_value=0,
                max_value=365,
                value=3,
                step=1,
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

        daftar_tugas.append(
            {
                "nama": nama,
                "deadline": deadline,
                "kesulitan": kesulitan
            }
        )

    if st.button(
        "ANALYZE PRIORITY",
        use_container_width=True
    ):

        for task in daftar_tugas:

            urgency = max(
                1,
                30 - task["deadline"]
            )

            task["score"] = (
                urgency +
                (task["kesulitan"] * 5)
            )

        daftar_tugas.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        st.markdown(
            '<div class="section-title">TASK PRIORITY</div>',
            unsafe_allow_html=True
        )

        for index, task in enumerate(daftar_tugas):

            if index == 0:
                level = "VERY HIGH"
            elif index == 1:
                level = "HIGH"
            else:
                level = "NORMAL"

            nama_aman = html.escape(
                task["nama"] if task["nama"] else "Unnamed Task"
            )

            st.markdown(
                f"""
                <div class="result-box">

                    <div class="result-label">
                        PRIORITY #{index + 1}
                    </div>

                    <div class="result-number">
                        {nama_aman}
                    </div>

                    <div class="result-status">
                        {level}
                    </div>

                    <div class="result-label">
                        Deadline: {task["deadline"]} hari
                        &nbsp; | &nbsp;
                        Difficulty: {task["kesulitan"]}/5
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# STUDY PLANNER
# =========================================================

elif st.session_state.menu == "STUDY PLANNER":

    st.markdown(
        """
        <div class="page-title">
            STUDY <span>PLANNER</span>
        </div>

        <div class="page-subtitle">
            Bagi waktu belajar secara sederhana agar semua materi
            mendapat jatah waktu.
        </div>
        """,
        unsafe_allow_html=True
    )

    waktu = st.number_input(
        "Waktu belajar tersedia (menit)",
        min_value=10,
        max_value=1440,
        value=120,
        step=10
    )

    jumlah_materi = st.number_input(
        "Jumlah materi / tugas",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )

    materi_list = []

    for i in range(jumlah_materi):

        materi = st.text_input(
            f"Materi {i + 1}",
            key=f"materi_{i}"
        )

        materi_list.append(materi)

    if st.button(
        "CREATE STUDY PLAN",
        use_container_width=True
    ):

        pembagian = waktu / jumlah_materi

        st.markdown(
            '<div class="section-title">YOUR STUDY PLAN</div>',
            unsafe_allow_html=True
        )

        for i, materi in enumerate(materi_list):

            nama_materi = html.escape(
                materi if materi else f"Materi {i + 1}"
            )

            st.markdown(
                f"""
                <div class="result-box">

                    <div class="result-label">
                        SESSION {i + 1}
                    </div>

                    <div class="result-number">
                        {nama_materi}
                    </div>

                    <div class="result-status">
                        {pembagian:.0f} MINUTES
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# DUID TRACKER
# =========================================================

elif st.session_state.menu == "DUID TRACKER":

    st.markdown(
        """
        <div class="page-title">
            DUID <span>TRACKER</span>
        </div>

        <div class="page-subtitle">
            Catat pemasukan dan pengeluaranmu.
        </div>
        """,
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
        min_value=0,
        max_value=30,
        value=3,
        step=1
    )

    total_pengeluaran = 0.0

    for i in range(jumlah_pengeluaran):

        col1, col2 = st.columns([2, 1])

        with col1:
            kategori = st.text_input(
                f"Pengeluaran {i + 1}",
                key=f"expense_name_{i}"
            )

        with col2:
            nominal = st.number_input(
                f"Nominal {i + 1}",
                min_value=0.0,
                value=0.0,
                step=1000.0,
                key=f"expense_amount_{i}"
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

                <div class="result-label">
                    REMAINING MONEY
                </div>

                <div class="result-number">
                    Rp {sisa:,.0f}
                </div>

                <div class="result-status">
                    {status}
                </div>

                <div class="result-label">
                    Total pengeluaran:
                    Rp {total_pengeluaran:,.0f}
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
        """
        <div class="section-title">ABOUT NEMO</div>
        <div class="page-subtitle">
            STUDENT LIFE MANAGEMENT ASSISTANT
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
            <b>NEMO STUDENT</b><br><br>
            NEMO adalah asisten sederhana untuk membantu siswa
            mengatur kehidupan sekolah sehari-hari.
            <br><br>

            <b>FEATURES</b><br>
            📊 Cek Nilai — menghitung rata-rata nilai.<br>
            ⚡ Prioritas Tugas — menentukan tugas yang harus dikerjakan lebih dulu.<br>
            📚 Study Planner — membagi waktu belajar.<br>
            💰 Duid Tracker — mencatat pemasukan dan pengeluaran.
            <br><br>

            <b>KNOW WHAT MATTERS.</b>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# NEMO FISH HELPER
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

fish_html = (
    '<div class="fish-label">'
    + current_tip
    + '</div>'
    '<div class="fish-shimeji">🐠</div>'
)

st.markdown(
    fish_html,
    unsafe_allow_html=True
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        NEMO STUDENT // KNOW WHAT MATTERS.<br>
        SYSTEM DESIGNED FOR STUDENT LIFE
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# NEMO FISH HELPER
# =========================================================

tips = {
    "HOME": "Hai! Aku NEMO 🐠<br><b>Tip:</b> Pilih fitur yang mau kamu gunakan.",
    "CEK NILAI": "Mau cek nilai?<br><b>Tip:</b> Masukkan nilai tiap mata pelajaran.",
    "PRIORITAS TUGAS": "Deadline mengejar 😭<br><b>Tip:</b> Masukkan deadline dan tingkat kesulitan tugas.",
    "STUDY PLANNER": "Waktunya belajar.<br><b>Tip:</b> Masukkan waktu belajar yang tersedia.",
    "DUID TRACKER": "Uangmu sedang diamati 👁️<br><b>Tip:</b> Catat pemasukan dan pengeluaranmu.",
    "ABOUT": "Aku NEMO! 🐠<br><b>Know What Matters.</b>"
}

current_tip = tips.get(
    st.session_state.menu,
    "Halo! Aku NEMO 🐠"
)

st.markdown(
    f"""
    <style>
    @keyframes fishFloat {{
        0% {{
            transform: translateY(0px);
        }}

        50% {{
            transform: translateY(-12px);
        }}

        100% {{
            transform: translateY(0px);
        }}
    }}
    </style>

    <div style="
        position: fixed;
        right: 25px;
        bottom: 25px;
        z-index: 999999;
        font-size: 60px;
        animation: fishFloat 3s ease-in-out infinite;
        filter: drop-shadow(0 5px 8px rgba(0,0,0,0.3));
    ">
        🐠
    </div>

    <div style="
        position: fixed;
        right: 90px;
        bottom: 85px;
        z-index: 999998;
        max-width: 230px;
        padding: 12px 15px;
        background: {PANEL};
        border: 1px solid {BLUE};
        border-radius: 14px;
        color: {TEXT};
        font-size: 12px;
        line-height: 1.5;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    ">
        {current_tip}
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

        NEMO STUDENT // KNOW WHAT MATTERS.<br>
        SYSTEM DESIGNED FOR STUDENT LIFE

    </div>
    """,
    unsafe_allow_html=True
)
