import streamlit as st

st.set_page_config(page_title="Recyclability Lab Tool", layout="wide")

st.title("Recyclability Laboratory Test Platform")


# Define tabs
tabs = st.tabs([
    "Overview",
    "Dry Content & Sample Prep",
    "Filtrate Analysis",
    "Lab Data – Screens & Rejects",
    "Macrostickies"
])

# ---- Overview ----
with tabs[0]:
    st.header("Overview")
    st.write("To add: input SO number; sample name; date tested; questionnaire answers - Need to pull from excel.")

# ---- Dry Content ----
with tabs[1]:
    st.header("Dry Content & Sample Prep")
    weight_before = st.number_input("Weight Before Drying (g)")
    weight_after = st.number_input("Weight After Drying (g)")
    if weight_before:
        dry_weight = (weight_after / weight_before) * 50
        moisture_content = (weight_after/ weight_before) * 100
        st.write(f"Moisture Content: {moisture_content:.2f} %")
        st.write(f"Equivalent 50g Dry Weight: {dry_weight:.2f} g")
        st.write("NOTE TO SELF: Add in the different sample components - WEIGHTS, the moisture tests etc..")
        
# ---- Filtrate Analysis ----
with tabs[2]:
    st.header("Filtrate Analysis")
    st.subheader("Filtrate 1")
    filtrate1_tin_weight = st.number_input("Filtrate 1 - Tin Weight (g)", format="%.4f")
    filtrate1_input_weight = st.number_input("Filtrate 1 - Input Weight (g)", format="%.2f")
    filtrate1_output_weight = st.number_input("Filtrate 1 - Output Weight (g)", format="%.4f")
    filtrate1_residue = filtrate1_tin_weight - filtrate1_output_weight
    filtrate1_evap_residue = filtrate1_residue / filtrate1_input_weight if filtrate1_input_weight else 0
    
    st.subheader("Filtrate 2")
    filtrate2_tin_weight = st.number_input("Filtrate 2 - Tin Weight (g)", format="%.4f")
    filtrate2_input_weight = st.number_input("Filtrate 2 - Input Weight (g)", format="%.2f")
    filtrate2_output_weight = st.number_input("Filtrate 2 - Output Weight (g)", format="%.4f")
    filtrate2_residue = filtrate2_tin_weight - filtrate2_output_weight
    filtrate2_evap_residue = filtrate2_residue / filtrate2_input_weight if filtrate2_input_weight else 0

    st.subheader("Water 1")
    water1_tin_weight = st.number_input("Water 1 - Tin Weight (g)", format="%.4f")
    water1_input_weight = st.number_input("Water 1 - Input Weight (g)", format="%.2f")
    water1_output_weight = st.number_input("Water 1 - Output Weight (g)", format="%.4f")
    water1_residue = water1_tin_weight - water1_output_weight
    water1_evap_residue = water1_residue / water1_input_weight if water1_input_weight else 0

    st.subheader("Water 2")
    water2_tine_weight = st.number_input("Water 2 - Tin Weight (g)", format="%.4f")
    water2_input_weight = st.number_input("Water 2 - Input Weight (g)", format="%.2f")
    water2_output_weight = st.number_input("Water 2 - Output Weight (g)", format="%.4f")
    water2_residue = water2_tine_weight - water2_output_weight
    water2_evap_residue = water2_residue / water2_input_weight if water2_input_weight else 0

    # Display table of evaporation residues
    import pandas as pd
    evap_data = {
        "Sample": ["Filtrate 1", "Filtrate 2", "Water 1", "Water 2"],
        "Evaporation Residue": [
            round(filtrate1_evap_residue, 4),
            round(filtrate2_evap_residue, 4),
            round(water1_evap_residue, 4),
            round(water2_evap_residue, 4)
        ]
    }
    evap_df = pd.DataFrame(evap_data)
    st.table(evap_df)

# ---- Lab Data – Screens & Rejects ----
with tabs[3]:
    st.header("Lab Data – Screens & Rejects")
    coarse_reject = st.number_input("Coarse Screen Reject (%)")
    fine_reject = st.number_input("Fine Screen Reject (%)")
    st.write(f"Coarse: {coarse_reject} % | Fine: {fine_reject} %")
    st.write("change to add the tin weight and output weight before calculating the percentage.")
# ---- Macrostickies ----
with tabs[4]:
    st.header("Macrostickies Data")
    macro_input = st.number_input("Macrostickies Count")
    st.write(f"Macrostickies Output: {macro_input}")
