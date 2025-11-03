import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Product Metrics Dashboard", layout="wide")
st.title("📈 Product Metrics Dashboard (Synthetic)")

days = st.slider("Days of data", 30, 180, 60)
seed = st.number_input("Random seed", value=42, step=1)
np.random.seed(int(seed))

# synthetic generation
dau = np.random.randint(900, 1500, days)
retention = np.clip(np.random.normal(0.78, 0.04, days), 0.55, 0.95)
conversion = np.clip(np.random.normal(0.12, 0.03, days), 0.03, 0.25)

df = pd.DataFrame({
    "Day": range(1, days+1),
    "DAU": dau,
    "Retention": retention,
    "Conversion": conversion
}).set_index("Day")

col1, col2, col3 = st.columns(3)
col1.metric("Avg DAU", int(df["DAU"].mean()))
col2.metric("Avg Retention", f"{df['Retention'].mean():.2%}")
col3.metric("Avg Conversion", f"{df['Conversion'].mean():.2%}")

st.subheader("Trends")
st.line_chart(df[["DAU","Retention","Conversion"]])

st.subheader("Scenario Testing")
lift = st.slider("Simulated feature impact on conversion (pp)", -5, 10, 2)
df["Conversion_scenario"] = np.clip(df["Conversion"] + (lift/100.0), 0, 1)
st.line_chart(df[["Conversion","Conversion_scenario"]])

st.caption("🔎 No external APIs. All numbers are synthetic for product exploration.")
