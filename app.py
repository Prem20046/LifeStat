import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Title
st.title("❤️ ArogyaMitra")




# --- Inputs ---
age = st.number_input("Enter your age", min_value=1, step=1)
weight = st.number_input("Enter your weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Enter your height (m)", min_value=0.5, step=0.01)
steps = st.number_input("Steps walked today", min_value=0, step=100)
sleep = st.number_input("Hours of sleep", min_value=0.0, step=0.5)

# --- Calculations ---
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.subheader("Health Metrics")
    st.write(f"Your BMI is **{round(bmi, 2)}**")

    if bmi < 18.5:
        st.warning("You are underweight. Consider a balanced diet.")
    elif 18.5 <= bmi < 24.9:
        st.success("You are in the healthy range. Keep it up!")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight. Regular exercise recommended.")
    else:
        st.error("You are in the obese range. Please consult a health professional.")

if sleep < 7:
    st.warning("You should aim for at least 7 hours of sleep.")
else:
    st.success("Great! You had enough sleep.")

if steps < 8000:
    st.info("Try to walk at least 8000 steps daily.")
else:
    st.success("Awesome! You hit your steps goal.")

# --- Visualization ---
st.subheader("Daily Summary Visualization")
labels = ['Steps', 'Sleep Hours']
values = [steps, sleep]

fig, ax = plt.subplots()
ax.bar(labels, values, color=['blue', 'green'])
ax.set_ylabel("Count")
st.pyplot(fig)

# --- CSV Upload for Weekly Data ---
st.subheader("Upload Weekly Data (CSV)")
st.write("CSV should have columns: Date, Steps, SleepHours")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:", df)

    # Weekly averages
    avg_steps = df["Steps"].mean()
    avg_sleep = df["SleepHours"].mean()
    st.write(f"**Average Steps per week:** {round(avg_steps)}")
    st.write(f"**Average Sleep per week:** {round(avg_sleep,1)} hours")

    # Plot
    fig2, ax2 = plt.subplots()
    ax2.plot(df["Date"], df["Steps"], marker="o", label="Steps")
    ax2.plot(df["Date"], df["SleepHours"], marker="s", label="Sleep Hours")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Value")
    ax2.legend()
    st.pyplot(fig2)

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.subheader("Upload Weekly Data (CSV)")
st.write("CSV should have columns: Date, Steps, SleepHours")

# CSV uploader
uploaded_file = st.file_uploaderuploaded_file = st.file_uploader(
    "Upload Weekly Data (CSV)",  # change the label if you want
    type=["csv"],
    key="weekly_csv"  # <-- add a unique key
)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:", df)

    # Weekly averages
    avg_steps = df["Steps"].mean()
    avg_sleep = df["SleepHours"].mean()
    st.write(f"**Average Steps per week:** {round(avg_steps)}")
    st.write(f"**Average Sleep per week:** {round(avg_sleep,1)} hours")

    # Line chart for progress
    st.subheader("Weekly Progress Chart")
    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Steps"], marker="o", label="Steps")
    ax.plot(df["Date"], df["SleepHours"], marker="s", label="Sleep Hours")
    ax.set_xlabel("Date")
    ax.set_ylabel("Count")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)





