import streamlit as st

# Initialize session state variables
if "success_count" not in st.session_state:
    st.session_state.success_count = 0
if "failure_count" not in st.session_state:
    st.session_state.failure_count = 0

st.title("Swipe-Based Trading Strategy Tester")

st.write("👈 Swipe Left for Failure | Swipe Right for Success 👉")

# Buttons to simulate swipe gestures
col1, col2 = st.columns(2)
with col1:
    if st.button("❌ SL"):
        st.session_state.failure_count += 1
with col2:
    if st.button("✅ TP"):
        st.session_state.success_count += 1

# Display statistics
total = st.session_state.success_count + st.session_state.failure_count
success_rate = (st.session_state.success_count / total * 100) if total > 0 else 0

st.subheader("📊 Results So Far")
st.write(f"*Total Swipes:* {total}")
st.write(f"✅ *Successes:* {st.session_state.success_count}")
st.write(f"❌ *Failures:* {st.session_state.failure_count}")
st.write(f"📈 *Success Rate:* {success_rate:.2f}%")

# Reset button
if st.button("🔄 Reset Counts"):
    st.session_state.success_count = 0
    st.session_state.failure_count = 0
