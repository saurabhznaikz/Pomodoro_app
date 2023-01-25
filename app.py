import streamlit as st
import time
from winotify import Notification, audio

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("styles.css")

#---------------------------------#
st.write("""
# The Pomodoro App
Let's do some focus work with this app.
Developed by: [Saurabh Naik]
""")

user_input = st.number_input('Insert number of sessions',value=2)
user_input1 = st.number_input('Insert work time in minutes',value=25)
user_input1 = int(user_input1*60)
temp1=user_input1
user_input2 = st.number_input('Insert break time in minutes',value=5)
user_input2 = int(user_input2*60)
temp2 = user_input2
button_clicked = st.button("Start")
toast = Notification(app_id='Pomodoro', title='Start Working ASAP', duration='long')
toast.set_audio(audio.LoopingCall8,loop=True)
if button_clicked:
    for i in range(0,user_input):
        user_input1=temp1
        user_input2=temp2
        toast.set_audio(audio.Default, loop=True)
        toast.show()
        with st.empty():
            while user_input1:
                mins= user_input1
                timer = '{:02d}'.format(mins)
                st.header(f"⏳ {timer} secs remaining")
                time.sleep(1)
                user_input1 -= 1
                st.success("🔔 Time for a break!")
            toast = Notification(app_id='Pomodoro', title='Take a break', duration='long')
            toast.set_audio(audio.Default, loop=True)
            toast.show()

        with st.empty():
            while user_input2:
                # Start the break
                mins2= user_input2
                timer2 = '{:02d}'.format(mins2)
                st.header(f"⏳ {timer2} secs remaining")
                time.sleep(1)
                user_input2 -= 1
                st.error("⏰ break is over!")
            toast = Notification(app_id='Pomodoro', title='Break Finish', duration='long')
            toast.set_audio(audio.Default, loop=True)
            toast.show()
