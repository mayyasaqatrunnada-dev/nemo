import streamlit as st

# ==============================
# NEMO
# Know What Matters.
# ==============================

st.set_page_config(
    page_title="NEMO",
    page_icon="🐟",
    layout="centered"
)

# ==============================
# JUDUL
# ==============================

st.title("🐟 NEMO")
st.caption("Know What Matters.")
st.write("Student Life Management Assistant")

st.divider()

# ==============================
# MENU
# ==============================

menu = st.selectbox(
    "Pilih fitur",
    [
        "🏠 Home",
        "📊 Cek Nilai",
        "📋 Prioritas Tugas",
        "⏰ Study Planner",
        "💸 Duid Tracker"
    ]
)

# ==============================
# HOME
# ==============================

if menu == "🏠 Home":

    st.header("Hai! 👋")

    st.write(
        "NEMO membantu kamu mengatur nilai, tugas, "
        "waktu belajar, dan keuangan sederhana."
    )

    st.info(
        "Pilih salah satu fitur di menu sebelah kiri."
    )


# ==============================
# CEK NILAI
# ==============================

elif menu == "📊 Cek Nilai":

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

            st.success("Hasil berhasil dihitung!")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Rata-rata", f"{rata:.2f}")

            with col2:
                st.metric("Predikat", predikat)


# ==============================
# PRIORITAS TUGAS
# ==============================

elif menu == "📋 Prioritas Tugas":

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

            # Menentukan skor urgensi
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

            for i, tugas_data in enumerate(tugas, 1):

                if tugas_data["skor"] >= 8:
                    status = "🔴 Tinggi"
                elif tugas_data["skor"] >= 5:
                    status = "🟡 Sedang"
                else:
                    status = "🟢 Rendah"

                st.write(
                    f"**{i}. {tugas_data['nama']}**"
                )

                st.write(
                    f"Deadline: {tugas_data['deadline']} hari lagi"
                )

                st.write(
                    f"Kesulitan: {tugas_data['kesulitan']}/5"
                )

                st.write(
                    f"Prioritas: {status}"
                )

                st.divider()


# ==============================
# STUDY PLANNER
# ==============================

elif menu == "⏰ Study Planner":

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

        st.success("Rencana berhasil dibuat!")

        st.metric(
            "Waktu per tugas",
            f"{waktu_per_tugas:.2f} jam"
        )

        if waktu_per_tugas >= 2:
            st.write(
                "Waktu cukup longgar. Fokus pada kualitas."
            )

        elif waktu_per_tugas >= 1:
            st.write(
                "Waktu cukup. Kurangi distraksi."
            )

        else:
            st.warning(
                "Waktu cukup sempit. Prioritaskan tugas terpenting."
            )


# ==============================
# DUIT TRACKER
# ==============================

elif menu == "💸 Duid Tracker":

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
            x["nominal"] for x in pengeluaran
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
            st.success(
                "Keuangan masih aman."
            )
