# https://streamlit.io/playground?example=charts
# Streamlit 패키지 추가
# pip install streamlit
# streamlit 실행 : streamlit run app.py

# import streamlit as st
# import pandas as pd
# import numpy as np
# import altair as alt

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# c = (
#    alt.Chart(chart_data)
#    .mark_circle()
#    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
# )

# st.altair_chart(c, use_container_width=True)

# import streamlit as st
# import pandas as pd
# import numpy as np

# # 표준 정규분포를 따르는 난수 생성, 평균 0, 표준편차 1인 정규분포 난수 추출
# # 20은 행의수, 3은 열의 수
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.line_chart(chart_data)

import streamlit as st
import pandas as pd
import numpy as np

st.write("Streamlit supports a wide range of data visualizations, including [Plotly,"
"Altair, and Bokeh charts](https://docs.streamlit.io/develop/api-reference/charts)."
" 📊 And with over 20 input widgets, you can easily make your data interactive!")

all_users = ["Alice", "Bob", "Charly"]
with st.container(border=True):
    users = st.multiselect("Users", all_users, default=all_users)
    # Rolling Average(이동 평균)는 특정 기간 동안의 평균을 계속 갱신하며 계산하는 평균값
    rolling_average = st.toggle("Rolling average")

np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
if rolling_average:
    data = data.rolling(7).mean().dropna()

tab1, tab2 = st.tabs(["Chart", "Dataframe"])
tab1.line_chart(data, height=250)
tab2.dataframe(data, height=250, use_container_width=True)