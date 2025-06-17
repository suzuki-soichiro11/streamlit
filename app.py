import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("レイアウトとデータ可視化")

# --- サイドバー  ---
st.sidebar.header("設定")
graph_type = st.sidebar.radio("グラフの種類を選択", ("Matplorlib", "Plotly"))

# --- メイン画面 ---
st.write("サイドバーでグラフを切り替えられます")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("設定項目")
    st.write("ここに設定などを配置できます")
    with st.expander("詳細設定"):
        st.image("https://static.streamlit.io/examples/dice.jpg")

with col2:
    st.header("グラフ表示エリア")
    if graph_type == "Matplorlib":
        st.subheader("Matplorlibグラフ")
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        fig, ax = plt.subplots()
        ax.plot(x, y)
        st.pyplot(fig)
    else:
        st.subheader("Plotly")
        df = px.data.iris()
        fig = px.scatter(
            df,
            x="sepal_width",
            y="sepal_length",
        )
        st.plotly_chart(fig, use_container_width=True)
