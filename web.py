import streamlit as st
import functions

todos = functions.get()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.save(todos)


st.title("My To-do App")
st.subheader("Add and complete to-dos")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Enter a to-do:', label_visibility="hidden", placeholder="Add a to-do:",
              on_change=add_todo, key="new_todo")
