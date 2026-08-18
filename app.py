import streamlit as st

st.set_page_config(
    page_title="NEMO",
    page_icon="🐟"
)

st.title("NEMO")
st.subheader("Know What Matters.")

st.write("Student Life Management Assistant")

st.divider()

st.write("Pilih fitur yang ingin kamu gunakan:")

if st.button("📊 Cek Nilai"):
    st.write("Fitur Cek Nilai")

if st.button("📋 Prioritas Tugas"):
    st.write("Fitur Prioritas Tugas")

if st.button("⏰ Study Planner"):
    st.write("Fitur Study Planner")

if st.button("💸 Duid Tracker"):
    st.write("Fitur Duid Tracker")
