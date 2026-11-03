import streamlit as st
import random

# 1. Session State를 활용한 데이터 초기화
if 'words' not in st.session_state:
    st.session_state.words = {} # 단어 저장용 딕셔너리

st.title("📚 나만의 영단어 오답노트 & 퀴즈")

# 2. 단어 추가 기능 구현
st.subheader("1. 새 단어 추가하기")
new_word = st.text_input("영어 단어 입력").strip()
new_meaning = st.text_input("뜻 입력").strip()

if st.button("단어 추가"):
    if new_word and new_meaning:
        st.session_state.words[new_word] = new_meaning
        st.success(f"'{new_word}' 단어가 성공적으로 추가되었습니다!")
    else:
        st.error("단어와 뜻을 모두 입력해 주세요.")

# 3. 퀴즈 기능 구현
st.subheader("2. 영단어 퀴즈")
if st.button("퀴즈 문제 불러오기"):
    if st.session_state.words:
        st.session_state.current_quiz = random.choice(list(st.session_state.words.keys()))
    else:
        st.warning("등록된 단어가 없습니다. 먼저 단어를 추가해 주세요.")

if 'current_quiz' in st.session_state:
    target_word = st.session_state.current_quiz
    st.write(f"**문제:** `{target_word}`의 뜻은 무엇일까요?")
    user_answer = st.text_input("정답 입력", key="user_ans")
    
    if st.button("채점하기"):
        correct_meaning = st.session_state.words[target_word]
        if user_answer.strip() == correct_meaning:
            st.balloons()
            st.success("정답입니다! 🎉")
        else:
            st.error(f"틀렸습니다. 정답은 '{correct_meaning}' 입니다.")
