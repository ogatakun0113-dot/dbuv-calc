import streamlit as st
import math

# --- 見た目の設定（CSS） ---
st.markdown("""
    <style>
    .stNumberInput label {
        font-size: 32px !important;
        color: #FF4B4B !important; /* 電圧入力は赤系で目立たせます */
        font-weight: 800 !important;
        line-height: 1.5;
    }
    div[data-baseweb="input"] {
        height: 60px !important;
        font-size: 28px !important;
        border: 3px solid #FF4B4B !important;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title('📡 dBμV → dBm 変換アプリ')
st.markdown("---")

# 入力欄（dBμVを入力）
dbuv_in = st.number_input("dBμV を入力してください", value=107.0)

# 計算ロジック（50Ω系）
# 1. dBμV から 電圧(V) へ
v_val = 10 ** ((dbuv_in - 120) / 20)

# 2. 電圧(V) から 電力(mW) へ (P = V^2 / R)
mw_val = (v_val ** 2 / 50) * 1000

# 3. 電力(mW) から dBm へ
if mw_val > 0:
    dbm_val = 10 * math.log10(mw_val)
else:
    dbm_val = -float('inf')

# 4. 電力(W) への換算
w_val = mw_val / 1000

# 表示
st.subheader("変換結果 (50Ω)")
c1, c2 = st.columns(2)
with c1:
    st.metric("電力 (dBm)", f"{dbm_val:.2f}")
    st.metric("電圧 (V)", f"{v_val:,.4f}")
with c2:
    st.metric("電力 (mW)", f"{mw_val:,.2f}")
    st.metric("電力 (W)", f"{w_val:,.4f}")
