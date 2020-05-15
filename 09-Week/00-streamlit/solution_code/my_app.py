import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from score import score_obs

st.title("Iris App")  # h1
st.header("Our ML project")  # h2
st.subheader("By: My team")  # h3

df_iris = px.data.iris()
df_iris

X = df_iris.drop(columns=["species", "species_id"])
y = df_iris["species"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123)
lr = LogisticRegression()
lr.fit(X_train, y_train)

# get the 4 values we need from the user
# make them integers
s_w = int(st.text_input("Input the Sepal Width", 1))
s_l = int(st.text_input("Input the Sepal Length", 1))
p_w = int(st.text_input("Input the Petal Width", 1))
p_l = int(st.text_input("Input the Petal Length", 1))

user_input = np.array([s_w, s_l, p_w, p_l])

prediction = score_obs(lr, user_input)
prediction

# we moved our function to the score file (first we made it here)

# interactive slider function
x = st.slider("x")
st.write(x, "squared is", x * x)

# st.write()
st.write(f"some phrase {prediction}")
f"some phrase {prediction}"


# markdown to add a link or image
st.markdown("[Data Awesome](https://dataawesome.com)  🎉")

# markdown to change styling
st.markdown(
    "<style>h2{color: red; background-color: coral;} body{ background-color: #f3f3f3;}</style>",
    unsafe_allow_html=True,
)

# hide_streamlit_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# fun
# st.balloons()

# example of interactive element with control flow
# to dynamically change the color of a badge
# streamlit is using bootstrap
score = st.sidebar.selectbox("Which number do you like best?", [1, 20, 24])

"Your Score:", score

sel = score
warn = "okay"

if score < 11:
    kind = "warning"
elif score < 20:
    kind = "warning"
    warn = "bareley"
else:
    kind = "success"

st.markdown(
    f'<span class="badge badge-pill badge-{kind}">{sel} Passing {warn} </span>',
    unsafe_allow_html=True,
)
