import streamlit as st

from func import r_todos,w_todos

st.title('todo app')
st.subheader('be productive')
li=r_todos()
def addtodo():
    li.append(st.session_state['newtodo'] + '\n')
    w_todos(li)

for i in li:
    cb=st.checkbox(i,key=i)
    print(cb,i)
    if cb:
        li.remove(i)
        w_todos(li)
        del st.session_state[i]
        st.rerun()
st.text_input(label='',placeholder='type your todo to add',on_change=addtodo,key='newtodo')

#st.session_state