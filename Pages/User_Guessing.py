import streamlit as st
import random

st.set_page_config(page_title="User Guessing",page_icon="D:\Streamlit\Pages\zoro_logo.png")
st.title("User guessing a number")
st.header("Rules:")
st.write("1.Computer will think a number a from 1 to 100.")
st.write("2.For each input the range for input will varry.")
st.write("3.Guess it in minimum number of moves(HINT: Use binary Search)")

if "think_num" not in st.session_state:
    st.session_state.think_num=random.randint(1,100)
    st.session_state.min=1
    st.session_state.max=100
    st.session_state.count=0
    st.session_state.tries=10

low=st.session_state.min
high=st.session_state.max

st.subheader("Let's Begin")
st.write(f"Number of remaining attempts:{st.session_state.tries}")
guess_num=st.text_input(f"Enter your guess between {low} and {high}")
if guess_num.isdigit():
    guess_num=int(guess_num)
    if st.session_state.tries>1:
        if guess_num==st.session_state.think_num:
            st.write(f"Yes, The number is {guess_num}")
            st.write(f"You found the number in {st.session_state.count} tries.")
            st.success("You have won")
            st.balloons()
        elif guess_num>st.session_state.think_num:
            st.write("Your Guess is greater than coumputer's number")
            st.session_state.max=guess_num
            st.button("Next try")
            st.session_state.tries-=1
        elif guess_num<st.session_state.think_num:
            st.write("Your Guess is less than coumputer's number")
            st.session_state.min=guess_num
            st.session_state.tries-=1
            st.button("Next try")
    else:
        st.write("You ran out of attempts, Better luck next time")
        restrat=st.button("Restart")
        if restrat:
            st.rerun()
else:
    if guess_num:
        st.write("Please enter a valid number.")