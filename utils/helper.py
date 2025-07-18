import pandas as pd
import streamlit as st
import base64
import streamlit as st


def get_column(df, default_col, label, key_prefix="shared"):
    """
    Returns a column from df.
    - If default_col is found, return it directly.
    - Else, show a selectbox to the user in the sidebar.
    - Uses session_state to avoid duplicate widgets.
    """
    session_key = f"{key_prefix}_{label}".replace(" ", "_")

    if default_col in df.columns:
        # Save it once to session state
        st.session_state[session_key] = default_col
        return default_col
    else:
        if session_key not in st.session_state:
            st.sidebar.warning(f"⚠️ `{default_col}` not found. Please select column for: {label}")
            st.session_state[session_key] = st.sidebar.selectbox(
                f"Select {label}",
                df.columns,
                key=session_key
            )
        return st.session_state[session_key]
def bucket(days):
    if pd.isna(days): return '> 90 Days'
    if days < 30: return '< 30 Days'
    elif days < 61: return '31 - 60 Days'
    elif days < 91: return '61 - 90 Days'
    else: return '> 90 Days'

def percent(val, total):
    val_cr = val / 1e7
    percent = (val / total * 100) if total else 0
    return f"₹ {val_cr:,.2f} Cr ({percent:.1f}%)"

def render_svg(svg_path):
    with open(svg_path, "r") as f:
        svg_data = f.read()
    b64 = base64.b64encode(svg_data.encode()).decode()
    html = f"""
    <div style="text-align:center; padding: 10px;">
        <img src='data:image/svg+xml;base64,{b64}' style='width:400px; height:auto;'>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
    
def highlight_rows(row):
    color = ''
    if "Agreement" in row["Metric"]:
        color = 'background-color: #e6f7ff'  # light blue
    elif "Collected" in row["Metric"]:
        color = 'background-color: #e8fce8'  # light green
    elif "Overdue" in row["Metric"]:
        color = 'background-color: #fff3e6'  # light orange
    elif "Demand" in row["Metric"]:
        color = 'background-color: #fef7e0'  # light yellow
    elif "Units" in row["Metric"]:
        color = 'background-color: #f2f2f2'  # light gray
    return [color] * len(row)