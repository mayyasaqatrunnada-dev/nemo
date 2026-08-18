import streamlit as st

# ============================================================
# NEMO
# Know What Matters.
# ============================================================

st.set_page_config(
    page_title="NEMO",
    page_icon="🐟",
    layout="centered"
)

# ============================================================
# STYLE
# ============================================================

st.markdown("""
<style>

    /* BACKGROUND */
    .stApp {
        background-color: #0B0F14;
        color: #F5F5F5;
    }

    /* MAIN TITLE */
    .nemo-title {
        text-align: center;
        font-size: 52px;
        font-weight: 800;
        color: #FF7A00;
        margin-top: 20px;
        margin-bottom: 0px;
    }

    .nemo-subtitle {
        text-align: center;
        font-size: 18px;
        color: #2196F3;
        margin-top: 0px;
        margin-bottom: 10px;
    }

    .nemo-description {
        text-align: center;
        color: #B8C0CC;
        font-size: 15px;
        margin-bottom: 30px;
    }

    /* SECTION TITLE */
    .section-title {
        color: #FFFFFF;
        font-size: 25px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    /* CARD */
    .feature-card {
        background-color: #151B23;
        border: 1px solid #263241;
        border-radius: 16px;
        padding: 20px;
        min-height: 150px;
        margin-bottom: 15px;
    }

    .feature-icon {
        font-size: 30px;
    }

    .feature-title {
        font-size: 19px;
        font-weight: 700;
        color: #FFFFFF;
        margin-top: 5px;
    }

    .feature-description {
        font-size: 13px;
        color: #AAB4C0;
    }

    /* ORANGE BUTTON */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #FF7A00;
        background-color: #FF7A00;
        color: #FFFFFF;
        font-weight: 700;
        padding: 10px;
    }

    div.stButton > button:hover {
        background-color: #2196F3;
        border-color: #2196F3;
        color: #FFFFFF;
    }

    /* FOOTER */
    .footer {
        text-align: center;
        color: #697586;
        font-size: 12px;
        margin-top: 40px;
        padding-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="nemo-title">🐟 NEMO</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nemo-subtitle"><i>Know What Matters.</i></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="nemo-description">'
    'Student Life Management Assistant'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MENU
# ============================================================

if "menu" not in st.session_state:
    st.session_state.menu = "Home"


# ============================================================
# HOME
# ============================================================

if st.session_state.menu == "Home":

    st.markdown(
        '<div class="section-title">Mau ngapain hari ini?</div>',
        unsafe_allow_html=True
    )

    # ---------- ROW 1 ----------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Cek Nilai</div>
            <div class="feature-description">
                Hitung rata-rata dan lihat performa akademikmu.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Cek Nilai", key="nilai"):
            st.session_state.menu = "Cek Nilai"
            st.rerun()

    with col2:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📋</div>
            <div class="feature-title">Prioritas Tugas</div>
            <div class="feature-description">
                Tentukan tugas mana yang harus dikerjakan dulu.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Prioritas", key="prioritas"):
            st.session_state.menu = "Prioritas Tugas"
            st.rerun()


    # ---------- ROW 2 ----------

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">⏰</div>
            <div class="feature-title">Study Planner</div>
            <div class="feature-description">
                Bagi waktu belajar berdasarkan jumlah tugas.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Planner", key="planner"):
            st.session_state.menu = "Study Planner"
            st.rerun()

    with col2:

        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">💸</div>
            <div class="feature-title">Duid Tracker</div>
            <div class="feature-description">
                Pantau pemasukan, pengeluaran, dan sisa uang.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Buka Duid Tracker", key="duid"):
            st.session_state.menu = "Duid Tracker"
            st.rerun()
    
# ============================================================
# CEK NILAI
# ============================================================

elif st.session_state.menu == "Cek Nilai":

    if st.button("← Kembali ke Home"):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("📊 Cek Nilai")

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
                f"Mata pelajaran {i+1}",
                key=f"nama_{i}"
            )

        with col2:
            angka = st.number_input(
                f"Nilai {i+1}",
                min_value=0.0,
                max_value=100.0,
                value=0.0,
                key=f"nilai_{i}"
            )

        if nama:
            nilai.append(angka)

    if st.button("Hitung Nilai"):

        if len(nilai) == 0:

            st.warning("Masukkan minimal satu nilai.")

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

            st.success("Nilai berhasil dihitung.")

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
if rata >= 90:

    st.success(
        "💡 Insight: Performa akademikmu sangat baik. "
        "Pertahankan konsistensinya."
    )

elif rata >= 80:

    st.info(
        "💡 Insight: Performa akademikmu sudah baik. "
        "Masih ada ruang untuk meningkatkan beberapa nilai."
    )

elif rata >= 70:

    st.warning(
        "💡 Insight: Nilaimu cukup, tetapi masih perlu ditingkatkan. "
        "Fokus pada mata pelajaran dengan nilai terendah."
    )

else:

    st.error(
        "💡 Insight: Nilai masih perlu banyak ditingkatkan. "
        "Coba buat jadwal belajar yang lebih teratur."
    )

# ============================================================
# PRIORITAS TUGAS
# ============================================================

elif st.session_state.menu == "Prioritas Tugas":

    if st.button("← Kembali ke Home"):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("📋 Prioritas Tugas")

    jumlah = st.number_input(
        "Jumlah tugas",
        min_value=1,
        max_value=20,
        value=3,
        step=1
    )

    tugas = []

    for i in range(int(jumlah)):

        st.subheader(f"Tugas {i+1}")

        nama = st.text_input(
            "Nama tugas",
            key=f"tugas_{i}"
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
            key=f"sulit_{i}"
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

            tugas.append({
                "nama": nama,
                "deadline": deadline,
                "kesulitan": kesulitan,
                "skor": skor
            })

    if st.button("Tentukan Prioritas"):

        if not tugas:

            st.warning("Masukkan minimal satu tugas.")

        else:

            tugas.sort(
                key=lambda x: x["skor"],
                reverse=True
            )

            st.subheader("Urutan Prioritas")

            for i, data in enumerate(tugas, 1):

                if data["skor"] >= 8:
                    status = "🔴 Tinggi"
                elif data["skor"] >= 5:
                    status = "🟡 Sedang"
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

    if st.button("← Kembali ke Home"):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("⏰ Study Planner")

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

    if st.button("Buat Rencana"):

        waktu_per_tugas = waktu / jumlah

        st.success("Rencana berhasil dibuat.")

        st.metric(
            "Waktu per tugas",
            f"{waktu_per_tugas:.2f} jam"
        )

        if waktu_per_tugas >= 2:

    st.success(
        "💡 Insight: Waktu cukup longgar. "
        "Kamu bisa fokus pada kualitas pengerjaan."
    )

elif waktu_per_tugas >= 1:

    st.info(
        "💡 Insight: Waktu cukup. "
        "Usahakan mengurangi distraksi selama belajar."
    )

else:

    st.warning(
        "💡 Insight: Waktu cukup sempit. "
        "Kerjakan tugas dengan prioritas tertinggi terlebih dahulu."
    )


# ============================================================
# DUIT TRACKER
# ============================================================

elif st.session_state.menu == "Duid Tracker":

    if st.button("← Kembali ke Home"):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("💸 Duid Tracker")

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

    pengeluaran = []

    for i in range(int(jumlah)):

        col1, col2 = st.columns(2)

        with col1:

            kategori = st.text_input(
                f"Kategori {i+1}",
                key=f"kategori_{i}"
            )

        with col2:

            nominal = st.number_input(
                f"Nominal {i+1}",
                min_value=0.0,
                value=0.0,
                step=1000.0,
                key=f"nominal_{i}"
            )

        if kategori:

            pengeluaran.append({
                "kategori": kategori,
                "nominal": nominal
            })

    if st.button("Hitung Keuangan"):

        total = sum(
            x["nominal"]
            for x in pengeluaran
        )

        sisa = pemasukan - total

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Pemasukan",
                f"Rp{pemasukan:,.0f}"
            )

        with col2:

            st.metric(
                "Pengeluaran",
                f"Rp{total:,.0f}"
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

    persentase_sisa = (sisa / pemasukan) * 100

    st.success(
        "Keuangan masih aman."
    )

    st.info(
        f"💡 Insight: Kamu masih memiliki "
        f"{persentase_sisa:.1f}% dari pemasukanmu."
    )

# ============================================================
# ABOUT PAGE
# ============================================================

if st.session_state.menu == "About NEMO":

    if st.button("← Kembali ke Home", key="back_about"):
        st.session_state.menu = "Home"
        st.rerun()

    st.header("ℹ️ Tentang NEMO")

    st.write(
        """
        **NEMO (Know What Matters.)** adalah Student Life
        Management Assistant yang dirancang untuk membantu
        siswa mengelola beberapa kebutuhan sehari-hari
        dalam satu platform sederhana.
        """
    )

    st.subheader("Apa yang bisa dilakukan NEMO?")

    st.write("📊 **Cek Nilai**")
    st.write(
        "Menghitung rata-rata nilai dan memberikan predikat akademik."
    )

    st.write("📋 **Prioritas Tugas**")
    st.write(
        "Menentukan prioritas tugas berdasarkan deadline dan tingkat kesulitan."
    )

    st.write("⏰ **Study Planner**")
    st.write(
        "Membantu membagi waktu belajar berdasarkan jumlah tugas."
    )

    st.write("💸 **Duid Tracker**")
    st.write(
        "Menghitung pemasukan, pengeluaran, dan sisa uang."
    )

    st.subheader("Teknologi")

    st.write(
        "🐍 Python  •  Streamlit  •  GitHub  •  Google Colab"
    )

    st.info(
        "NEMO dibuat untuk membantu pengguna mengetahui "
        "apa yang penting dan menentukan prioritas dengan lebih mudah."
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
