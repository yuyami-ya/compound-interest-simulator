import streamlit as st
import pandas as pd
from services import calculate

def display():
    st.header("複利計算シミュレータ 入力")
    button = st.button("PUSH")
    if button:
        # data = file_service.read_csv(uploaded_file)
        year_month_list, pay_list, amount_appraised_list, increase_amount_list = calculate.calculate()
        
        # TODO: キーを英語に, 表示名は別で付ける
        data = {
            '年月': year_month_list,
            '元金(万)': pay_list,
            '評価額(万)': amount_appraised_list,
            '前月からの増加額(万)': increase_amount_list
        }
        line_and_color_settings = (
            ["元金(万)", "評価額(万)"],
            ["#A1CBC7", "#9A80A7"]
        )
        
        print(f"{data}")
        # 反転表示
        df = pd.DataFrame(data)
        df_transpose = pd.DataFrame(data).transpose(copy=True)
        st.dataframe(df_transpose)
        # TODO: グラフの表示がうまくいかない
        st.line_chart(data=df, x="年月", y=line_and_color_settings[0], color=line_and_color_settings[1])