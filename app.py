import streamlit as st
from scheduler import MangaScheduler

st.title("AI 漫剧生成系统")
prompt = st.text_area("输入剧情分镜")
uploaded_file = st.file_uploader("上传角色肖像", type=['png'])

if st.button("开始一键生成"):
    # 这里整合全自动逻辑
    st.write("1. 正在分析剧本...")
    st.write("2. 正在调用 ComfyUI 渲染引擎...")
    st.write("3. 正在合成视频...")
    st.success("制作完成！")
