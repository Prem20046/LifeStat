import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# --- App Configuration ---
st.set_page_config(page_title="LifeStat", page_icon="💡", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
        .main {
            background: linear-gradient(to bottom right, #f0f9ff, #cbebff);
            border-radius: 10px;
            padding: 25px;
        }
        h1, h2, h3, h4 {
            color: #003366;
        }
        .stButton>button {
            background-color: #0078d7;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 10em;
            font-weight: 600;
        }
        .stButton>button:hover {
            background-color: #005fa3;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- Landing Section ---
st.title("💡 LifeStat")
st.markdown("### Your Personal Smart Health Tracker")
st.write(
    "Welcome to **LifeStat**, a simple yet powerful way to monitor your daily fitness stats and lifestyle trends. "
    "Track your **steps, sleep, BMI**, and visualize progress effortlessly."
)

# Optional divider
st.markdown("---")

# --- Inputs Section ---
st.header("🧍‍♂️ Daily Health Input")
age = st.number_input("Age", min_value=1, step=1)
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (m)", min_value=0.5, step=0.01)
steps = st.number_input("Steps Walked Today", min_value=0, step=100)
sleep = st.number_input("Hours of Sleep", min_value=0.0, step=0.5)

# --- Calculations ---
if weight > 0 and height > 0:
    bmi = weight / (height ** 2)
    st.subheader("🩺 Health Metrics")
    st.write(f"**Your BMI:** {round(bmi, 2)}")

    if bmi < 18.5:
        st.warning("You are underweight. Consider a balanced diet.")
    elif 18.5 <= bmi < 24.9:
        st.success("You are in a healthy range. Keep it up!")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight. Regular exercise recommended.")
    else:
        st.error("You are in the obese range. Please consult a health professional.")

if sleep < 7:
    st.warning("Try to get at least 7 hours of sleep.")
else:
    st.success("Great! You got enough sleep.")

if steps < 8000:
    st.info("Try to walk at least 8000 steps daily.")
else:
    st.success("Nice! You reached your step goal.")

# --- Visualization ---
st.subheader("📊 Daily Summary Visualization")
labels = ['Steps', 'Sleep Hours']
values = [steps, sleep]

fig, ax = plt.subplots()
ax.bar(labels, values, color=['#4C8BF5', '#34A853'])
ax.set_ylabel("Count")
st.pyplot(fig)

# --- Weekly Analysis ---
st.header("📅 Weekly Analysis")
st.write("Upload a CSV with columns: Date, Steps, SleepHours")

uploaded_file = st.file_uploader("Upload Weekly Data (CSV)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("**Uploaded Data:**")
    st.dataframe(df)

    # Weekly averages
    avg_steps = df["Steps"].mean()
    avg_sleep = df["SleepHours"].mean()
    st.write(f"**Average Steps (Weekly):** {round(avg_steps)}")
    st.write(f"**Average Sleep (Weekly):** {round(avg_sleep, 1)} hours")

    # Weekly Progress Chart
    st.subheader("📈 Weekly Progress")
    fig2, ax2 = plt.subplots()
    ax2.plot(df["Date"], df["Steps"], marker="o", label="Steps", color="#4C8BF5")
    ax2.plot(df["Date"], df["SleepHours"], marker="s", label="Sleep Hours", color="#34A853")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Value")
    ax2.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig2)

# --- Footer ---
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:grey;'>Built with ❤️ using Streamlit & Python | © 2025 LifeStat</p>",
    unsafe_allow_html=True
)
