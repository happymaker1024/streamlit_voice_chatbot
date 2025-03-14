# pip install python-dotenv
# Streamlit 패키지 추가
import streamlit as st

# OpenAI 패키지 추가
import openai
import os
from dotenv import load_dotenv

# .env 파일 경로 지정 
load_dotenv()

# Open AI API 키 설정하기
api_key = os.environ.get('OPENAI_API_KEY')

client = openai.OpenAI(api_key=api_key)

##### 메인 함수 #####
def main():
    # 기본 설정
    st.set_page_config(
        page_title="음성 챗봇 프로그램",
        layout="wide")

    # 제목 
    st.header("음성 챗봇 프로그램")

    # 구분선
    st.markdown("---")

    # 기본 설명
    with st.expander("음성 챗봇 프로그램에 관하여", expanded=True):
        st.write(
        """     
        - 음성 번역 챗봇 프로그램의 UI는 스트림릿을 활용합니다.
        - STT(Speech-To-Text)는 OpenAI의 Whisper를 활용합니다. 
        - 답변은 OpenAI의 GPT 모델을 활용합니다. 
        - TTS(Text-To-Speech)는 OpenAI의 TTS를 활용합니다.
        """
        )

        st.markdown("")

    # 사이드바 생성
    with st.sidebar:

        # GPT 모델을 선택하기 위한 라디오 버튼
        model = st.radio(label="GPT 모델", options=["gpt-3.5-turbo", "gpt-4o", "gpt-4-turbo"])

        st.markdown("---")

        # 리셋 버튼 생성
        if st.button(label="초기화"):
            # 리셋 코드 
            pass

    # 기능 구현 공간
    col1, col2 = st.columns(2)
    with col1:
        # 왼쪽 영역 작성
        st.subheader("질문하기")

    with col2:
        # 오른쪽 영역 작성
        st.subheader("질문/답변")

if __name__=="__main__":
    main()