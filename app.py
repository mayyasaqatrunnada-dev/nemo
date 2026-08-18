import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="NEMO",
    page_icon="🐟",
    layout="centered"
)


# ============================================================
# SESSION STATE
# ============================================================

if "menu" not in st.session_state:
    st.session_state.menu = "Home"

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


# ============================================================
# THEME
# ============================================================

if st.session_state.dark_mode:
    # DARK MODE
    # Background tetap biru muda
    bg_color = "#DDF3FF"
    card_color = "#171717"
    text_color = "#FFFFFF"
    secondary_color = "#FFFFFF"
    border_color = "#303030"

else:
    # LIGHT MODE
    # Background biru tua
    bg_color = "#1769AA"
    card_color = "#FFFFFF"
    text_color = "#17202A"
    secondary_color = "#17202A"
    border_color = "#B9DDF5"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&display=swap');


/* ==========================================================
   GLOBAL
   ========================================================== */

html, body, [class*="css"] {{
    font-family: 'Nunito', sans-serif !important;
}}

.stApp {{
    background: {bg_color} !important;
}}


/* ==========================================================
   SEMUA TEKS UTAMA
   ========================================================== */

.stApp .stMarkdown p {{
    color: {text_color} !important;
}}

.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {{
    color: {text_color} !important;
    font-family: 'Nunito', sans-serif !important;
    font-weight: 900 !important;
}}


/* ==========================================================
   NEMO HEADER
   ========================================================== */

.nemo-title {{
    text-align: center;
    color: #FF7A3D !important;
    font-size: 56px;
    font-weight: 900;
    letter-spacing: -2px;
    margin-top: 10px;
    margin-bottom: 0px;
}}

.nemo-subtitle {{
    text-align: center;
    color: {text_color} !important;
    font-size: 19px;
    font-weight: 900;
    letter-spacing: 1px;
}}

.nemo-description {{
    text-align: center;
    color: {secondary_color} !important;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 25px;
}}


/* ==========================================================
   SECTION TITLE
   ========================================================== */

.section-title {{
    text-align: center;
    color: {text_color} !important;
    font-size: 25px;
    font-weight: 900;
    margin-top: 25px;
    margin-bottom: 20px;
}}


/* ==========================================================
   FEATURE CARD
   ========================================================== */

.feature-card {{
    background: {card_color} !important;
    border: 2px solid {border_color};
    border-radius: 22px;
    padding: 20px;
    min-height: 145px;
    margin-bottom: 10px;
    box-shadow: 0 8px 18px rgba(0, 0, 0, 0.18);
}}

.feature-icon {{
    font-size: 32px;
    margin-bottom: 7px;
}}

.feature-title {{
    color: {text_color} !important;
    font-size: 19px;
    font-weight: 900;
    margin-bottom: 5px;
}}

.feature-description {{
    color: {secondary_color} !important;
    font-size: 13px;
    font-weight: 600;
    line-height: 1.5;
}}


/* ==========================================================
   BUTTON
   ========================================================== */

div.stButton > button {{
    width: 100%;
    border-radius: 14px;
    border: 2px solid #FF7A3D !important;
    background: #FF7A3D !important;
    color: #17202A !important;
    font-family: 'Nunito', sans-serif !important;
    font-size: 14px;
    font-weight: 900;
    padding: 10px;
}}

div.stButton > button:hover {{
    background: #4A9FE8 !important;
    border-color: #4A9FE8 !important;
    color: #17202A !important;
}}


/* ==========================================================
   INPUT
   ========================================================== */

.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stSlider label {{
    color: {text_color} !important;
    font-weight: 700 !important;
}}

input {{
    background: #FFFFFF !important;
    color: #17202A !important;
}}


/* ==========================================================
   METRIC
   ========================================================== */

[data-testid="stMetricValue"] {{
    color: {text_color} !important;
}}

[data-testid="stMetricLabel"] {{
    color: {text_color} !important;
}}


/* ==========================================================
   FOOTER
   ========================================================== */

.footer {{
    text-align: center;
    color: {text_color} !important;
    font-size: 12px;
    font-weight: 700;
    margin-top: 40px;
    padding-bottom: 20px;
}}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# FEATURE CARD FUNCTION
# ============================================================

def feature_card(icon, title, description):

    st.markdown(
        f'<div class="feature-card">'
        f'<div class="feature-icon">{icon}</div>'
        f'<div class="feature-title">{title}</div>'
        f'<div class="feature-description">{description}</div>'
        f'</div>',
        unsafe_allow_html=True
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="nemo-title">🐟 NEMO</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nemo-subtitle">Know What Matters.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nemo-description">'
    'Student Life Management Assistant'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# THEME BUTTON
# ============================================================

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    if st.session_state.dark_mode:

        if st.button(
            "☀️ Light Mode",
            key="theme_button"
        ):
            st.session_state.dark_mode = False
            st.rerun()

    else:

        if st.button(
            "🌙 Dark Mode",
            key="theme_button"
        ):
            st.session_state.dark_mode = True
            st.rerun()


# ============================================================
# HOME
# ============================================================

if st.session_state.menu == "Home":

    st.markdown(
        '<div class="section-title">Mau ngapain hari ini?</div>',
        unsafe_allow_html=True
    )


    # --------------------------------------------------------
    # ROW 1
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        feature_card(
            "📊",
            "Cek Nilai",
            "Hitung rata-rata dan lihat performa akademikmu."
        )

        if st.button(
            "Buka Cek Nilai",
            key="home_nilai"
        ):
            st.session_state.menu = "Cek Nilai"
            st.rerun()


    with col2:

        feature_card(
            "📋",
            "Prioritas Tugas",
            "Tentukan tugas mana yang harus dikerjakan lebih dulu."
        )

        if st.button(
            "Buka Prioritas",
            key="home_prioritas"
        ):
            st.session_state.menu = "Prioritas Tugas"
            st.rerun()


    # --------------------------------------------------------
    # ROW 2
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        feature_card(
            "⏰",
            "Study Planner",
            "Bagi waktu belajar berdasarkan jumlah tugas."
        )

        if st.button(
            "Buka Planner",
            key="home_planner"
        ):
            st.session_state.menu = "Study Planner"
            st.rerun()


    with col2:

        feature_card(
            "💸",
            "Duid Tracker",
            "Pantau pemasukan, pengeluaran, dan sisa uang."
        )

        if st.button(
            "Buka Duid Tracker",
            key="home_duid"
        ):
            st.session_state.menu = "Duid Tracker"
            st.rerun()


    st.divider()


    if st.button(
        "ℹ️ Tentang NEMO",
        key="home_about"
    ):
        st.session_state.menu = "About NEMO"
        st.rerun()


# ============================================================
# CEK NILAI
# ============================================================

elif st.session_state.menu == "Cek Nilai":

    if st.button(
        "← Kembali ke Home",
        key="back_nilai"
    ):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("📊 Cek Nilai")

    st.write(
        "Masukkan nilai mata pelajaran untuk mengetahui "
        "rata-rata dan predikat akademikmu."
    )

    jumlah = st.number_input(
        "Jumlah mata pelajaran",
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
                f"Mata pelajaran {i + 1}",
                key=f"nama_nilai_{i}"
            )

        with col2:

            angka = st.number_input(
                f"Nilai {i + 1}",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                key=f"angka_nilai_{i}"
            )

        if nama:
            nilai.append(angka)


    if st.button(
        "Hitung Nilai",
        key="hitung_nilai"
    ):

        if len(nilai) == 0:

            st.warning(
                "Masukkan minimal satu nilai."
            )

        else:

            rata = sum(nilai) / len(nilai)

            if rata >= 90:
                predikat = "Sangat Baik"

            elif rata >= 80:
                predikat = "Baik"

            elif rata >= 70:
                predikat = "Cukup"

            else:
                predikat = "Perlu Ditingkatkan"


            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Rata-rata",
                    f"{rata:.2f}"
                )

            with col2:

                st.metric(
                    "Predikat",
                    predikat
                )


# ============================================================
# PRIORITAS TUGAS
# ============================================================

elif st.session_state.menu == "Prioritas Tugas":

    if st.button(
        "← Kembali ke Home",
        key="back_prioritas"
    ):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("📋 Prioritas Tugas")

    st.write(
        "NEMO menentukan prioritas berdasarkan deadline "
        "dan tingkat kesulitan."
    )

    jumlah = st.number_input(
        "Jumlah tugas",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )

    tugas = []

    for i in range(int(jumlah)):

        st.subheader(
            f"Tugas {i + 1}"
        )

        nama = st.text_input(
            "Nama tugas",
            key=f"nama_tugas_{i}"
        )

        deadline = st.number_input(
            "Deadline (hari lagi)",
            min_value=0,
            max_value=365,
            value=3,
            key=f"deadline_{i}"
        )

        kesulitan = st.slider(
            "Tingkat kesulitan",
            min_value=1,
            max_value=5,
            value=3,
            key=f"kesulitan_{i}"
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
        "Tentukan Prioritas",
        key="hitung_prioritas"
    ):

        if not tugas:

            st.warning(
                "Masukkan minimal satu tugas."
            )

        else:

            tugas.sort(
                key=lambda x: x["skor"],
                reverse=True
            )

            st.subheader(
                "Urutan Prioritas"
            )

            for i, data in enumerate(
                tugas,
                1
            ):

                if data["skor"] >= 8:
                    status = "🔴 Tinggi"

                elif data["skor"] >= 5:
                    status = "🟠 Sedang"

                else:
                    status = "🔵 Rendah"

                st.write(
                    f"**{i}. {data['nama']}**"
                )

                st.write(
                    f"Deadline: {data['deadline']} hari lagi"
                )

                st.write(
                    f"Kesulitan: {data['kesulitan']}/5"
                )

                st.write(
                    f"Prioritas: {status}"
                )

                st.divider()


# ============================================================
# STUDY PLANNER
# ============================================================

elif st.session_state.menu == "Study Planner":

    if st.button(
        "← Kembali ke Home",
        key="back_planner"
    ):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("⏰ Study Planner")

    st.write(
        "Atur waktu belajar berdasarkan waktu yang tersedia "
        "dan jumlah tugas."
    )

    waktu = st.number_input(
        "Waktu belajar tersedia (jam)",
        min_value=0.5,
        max_value=24.0,
        value=2.0,
        step=0.5
    )

    jumlah = st.number_input(
        "Jumlah tugas",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )


    if st.button(
        "Buat Rencana",
        key="buat_rencana"
    ):

        waktu_per_tugas = waktu / jumlah

        st.success(
            "Rencana berhasil dibuat."
        )

        st.metric(
            "Waktu per tugas",
            f"{waktu_per_tugas:.2f} jam"
        )


# ============================================================
# DUID TRACKER
# ============================================================

elif st.session_state.menu == "Duid Tracker":

    if st.button(
        "← Kembali ke Home",
        key="back_duid"
    ):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("💸 Duid Tracker")

    st.write(
        "Catat pemasukan dan pengeluaran "
        "untuk mengetahui sisa uang."
    )

    pemasukan = st.number_input(
        "Uang masuk",
        min_value=0.0,
        value=100000.0,
        step=10000.0
    )

    jumlah = st.number_input(
        "Jumlah pengeluaran",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )

    total_pengeluaran = 0


    for i in range(int(jumlah)):

        col1, col2 = st.columns(2)

        with col1:

            st.text_input(
                f"Kategori {i + 1}",
                key=f"kategori_{i}"
            )

        with col2:

            nominal = st.number_input(
                f"Nominal {i + 1}",
                min_value=0.0,
                value=0.0,
                step=1000.0,
                key=f"nominal_{i}"
            )

            total_pengeluaran += nominal


    if st.button(
        "Hitung Keuangan",
        key="hitung_keuangan"
    ):

        sisa = pemasukan - total_pengeluaran

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Pemasukan",
                f"Rp{pemasukan:,.0f}"
            )

        with col2:

            st.metric(
                "Pengeluaran",
                f"Rp{total_pengeluaran:,.0f}"
            )

        with col3:

            st.metric(
                "Sisa",
                f"Rp{sisa:,.0f}"
            )

        if sisa < 0:

            st.error(
                "Pengeluaran lebih besar daripada pemasukan."
            )

        elif sisa == 0:

            st.warning(
                "Uang kamu habis."
            )

        else:

            st.success(
                "Keuangan masih aman."
            )


# ============================================================
# ABOUT NEMO
# ============================================================

elif st.session_state.menu == "About NEMO":

    if st.button(
        "← Kembali ke Home",
        key="back_about"
    ):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("ℹ️ Tentang NEMO")

    st.write(
        "**NEMO (Know What Matters.)** adalah Student Life "
        "Management Assistant yang membantu siswa mengelola "
        "kebutuhan sehari-hari dalam satu aplikasi sederhana."
    )

    st.subheader("Fitur NEMO")

    st.write(
        "📊 **Cek Nilai**"
    )

    st.write(
        "Menghitung rata-rata nilai dan predikat."
    )

    st.write(
        "📋 **Prioritas Tugas**"
    )

    st.write(
        "Menentukan prioritas berdasarkan deadline "
        "dan tingkat kesulitan."
    )

    st.write(
        "⏰ **Study Planner**"
    )

    st.write(
        "Membagi waktu belajar berdasarkan jumlah tugas."
    )

    st.write(
        "💸 **Duid Tracker**"
    )

    st.write(
        "Menghitung pemasukan, pengeluaran, dan sisa uang."
    )

    st.subheader("Teknologi")

    st.write(
        "🐍 Python • Streamlit • GitHub"
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    '<div class="footer">'
    'NEMO • Know What Matters.'
    '</div>',
    unsafe_allow_html=True
)
