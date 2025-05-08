import streamlit as st
import pandas as pd
import random

# ページ設定
st.set_page_config(page_title="今日の格言", layout="centered")

# データ読み込み
df = pd.read_csv("data/sayings.csv")
row = df.sample(1).iloc[0]

# 格言表示
st.title("🌿 今日の格言")
st.subheader(f"『{row['saying']}』")
st.caption(f"出典：{row['source']}")
st.markdown(f"**{row['interpretation']}**")

# コメント
st.markdown("### 🗣 感じたことを共有する")
comment = st.text_area("あなたの感じたことをどうぞ")
if st.button("コメントする"):
    st.success("ありがとうございます！コメントが投稿されました（仮）")

# シェア（リンクコピーなどの仮UI）
st.markdown("### 🔗 シェア")
if st.button("リンクをコピー（仮）"):
    st.info("クリップボード機能は今後実装予定です。")
