import streamlit as st
import pandas as pd
import plotly.express as px

# ---------- Sample Input Variables (replace with your dynamic variables) ----------

# Top-Level Summary
total_units = 91
total_agreement_value = "₹ 189.52 Cr"
collected_with_tax = "₹ 135.15 Cr"
collected_without_tax = "₹ 130.00 Cr"

# Agreement Value Breakdown
agr_val_reg = "₹ 99.87 Cr"
agr_val_unreg = "₹ 89.65 Cr"

# Collection Breakdown
collected_reg = "₹ 73.98 Cr"
collected_unreg = "₹ 61.18 Cr"

# Overdue
amount_overdue_total = "₹ 3.26 Cr"
amount_overdue_reg = "₹ 0.37 Cr"
amount_overdue_unreg = "₹ 2.90 Cr"

# ---------- Page Config ----------
st.set_page_config(page_title="Unit Metrics Dashboard", layout="wide")

st.title("📊 Total Unit & Financial Metrics Dashboard")

# ---------- Section 1: Top Summary ----------
st.markdown("### 🔹 Summary Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Units", total_units)
col2.metric("Agreement Value", total_agreement_value)
col3.metric("Collected (With Tax)", collected_with_tax)
col4.metric("Collected (Without Tax)", collected_without_tax)

# ---------- Section 2: Agreement Value Breakdown ----------
with st.expander("📄 Total Agreement Value Breakdown"):
    col1, col2, col3 = st.columns(3)
    col1.metric("Registered", agr_val_reg)
    col2.metric("Unregistered", agr_val_unreg)
    col3.metric("Total", total_agreement_value)

# ---------- Section 3: Amount Collected Breakdown ----------
with st.expander("💰 Amount Collected Breakdown"):
    col1, col2 = st.columns(2)
    col1.metric("With Tax", collected_with_tax)
    col2.metric("Without Tax", collected_without_tax)

    col3, col4 = st.columns(2)
    col3.metric("Registered", collected_reg)
    col4.metric("Unregistered", collected_unreg)

# ---------- Section 4: Amount Overdue ----------
with st.expander("🚨 Amount Overdue Breakdown"):
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Overdue", amount_overdue_total)
    col2.metric("Registered", amount_overdue_reg)
    col3.metric("Unregistered", amount_overdue_unreg)

# ---------- Section 5: Detailed Table ----------
with st.expander("📋 Full Metric Table"):
    df = pd.DataFrame({
        "Metric": [
            "Total Units Booked", "Total Agreement Value", "Amount Collected (With Tax)",
            "Amount Collected (Without Tax)", "Amount Overdue"
        ],
        "All Units": [
            "91", total_agreement_value, collected_with_tax,
            collected_without_tax, amount_overdue_total
        ],
        "Registered Users": [
            "48", agr_val_reg, collected_reg, "-", amount_overdue_reg
        ],
        "Unregistered Users": [
            "43", agr_val_unreg, collected_unreg, "-", amount_overdue_unreg
        ]
    })
    st.dataframe(df, use_container_width=True)

# ---------- Section 6: Pie Chart ----------
with st.expander("📊 Agreement Value Distribution"):
    pie_data = pd.DataFrame({
        'Category': ['Registered', 'Unregistered'],
        'Value': [99.87, 89.65]
    })
    fig = px.pie(pie_data, values='Value', names='Category',
                 title='Registered vs Unregistered - Agreement Value')
    st.plotly_chart(fig, use_container_width=True)
