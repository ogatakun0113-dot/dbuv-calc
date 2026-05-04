import streamlit as st
import math

# --- ページ設定 ---
st.set_page_config(page_title="dBμV→dBm変換アプリ", layout="centered")

# --- 見た目の設定（CSS） ---
st.markdown("""
    <style>
    /* クレジット表示用のCSS */
    .credit {
        text-align: right;
        font-size: 14px;
        color: #666;
        margin-bottom: -20px;
    }
    /* 入力欄のラベルを大きく、太く、赤くする */
    .stNumberInput label {
        font-size: 32px !important;
        color: #FF4B4B !important;
        font-weight: 800 !important;
        line-height: 1.5;
    }
    /* 入力枠内の数字そのものを大きくする */
    div[data-baseweb="input"] {
        height: 60px !important;
        font-size: 28px !important;
        border: 3px solid #FF4B4B !important;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 右上にクレジットを表示
st.markdown('<p class="credit">開発/制作：緒方</p>', unsafe_allow_html=True)

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
