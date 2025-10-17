import streamlit as st

st.set_page_config(page_title="Recyclability Lab Tool", layout="wide")

st.title("Recyclability Laboratory Test")

# Define tabs
tabs = st.tabs([
    "Overview",
    "Dry Content & Sample Prep",
    "Filtrate Analysis",
    "Coarse Screen",
    "Fine Screen",
    "Macrostickies",
    "Scorecard", 
    "Dial"
])

# ---- Overview ----
with tabs[0]:
    st.header("Overview")
    sample_name = st.text_input("Sample Name")
    order_number = st.text_input("Order Number")
    date_tested = st.date_input("Date of Testing", format="DD-MM-YYYY")
    st.write(f"Sample Name: {sample_name}")
    st.write(f"Order Number: {order_number}")
    st.write(f"Date of Testing: {date_tested.strftime('%d-%m-%Y')}")


# ---- Dry Content ----
with tabs[1]:
    st.header("Dry Content & Sample Prep")
    st.subheader("Moisture Test 1")
    weight_before1 = st.number_input("Air Dry Mass (Test 1, g)", key="weight_before1")
    weight_after1 = st.number_input("Oven Dry Mass (Test 1, g)", key="weight_after1")
    moisture1 = None
    if weight_before1:
        moisture1 = (weight_after1 / weight_before1) * 100
        st.write(f"Moisture Content (Test 1): {moisture1:.2f} %")

    st.subheader("Moisture Test 2")
    weight_before2 = st.number_input("Air Dry Mass (Test 2, g)", key="weight_before2")
    weight_after2 = st.number_input("Oven Dry Mass (Test 2, g)", key="weight_after2")
    moisture2 = None
    if weight_before2:
        moisture2 = (weight_after2 / weight_before2) * 100
        st.write(f"Moisture Content (Test 2): {moisture2:.2f} %")

    if moisture1 is not None and moisture2 is not None:
        avg_moisture = (moisture1 + moisture2) / 2
        st.write(f"Average Moisture Content: {avg_moisture:.2f} %")
        avg_bone_dry_equiv = (((weight_after1 / weight_before1) + (weight_after2 / weight_before2)) / 2) * 50
        st.write(f"Average 50g Bone Dry Equivalent: {avg_bone_dry_equiv:.2f} g")
        st.write("Add in the calc for amount of water needed for disintegration, sample for fine screen testing, stock consistency, macrostickies plus option for multiple moisture tests")
        
# ---- Filtrate Analysis ----
with tabs[2]:
    st.header("Filtrate Analysis")
    st.subheader("Filtrate 1")
    filtrate1_tin_weight = st.number_input("Filtrate 1 - Tin Weight (g)", step=0.0001, format="%.4f")
    filtrate1_input_weight = st.number_input("Filtrate 1 - Input Weight (g)", format="%.2f")
    filtrate1_output_weight = st.number_input("Filtrate 1 - Output Weight (g)", format="%.4f")
    filtrate1_residue = filtrate1_tin_weight - filtrate1_output_weight
    filtrate1_evap_residue = filtrate1_residue / filtrate1_input_weight if filtrate1_input_weight else 0
    
    st.subheader("Filtrate 2")
    filtrate2_tin_weight = st.number_input("Filtrate 2 - Tin Weight (g)", step=0.0001, format="%.4f")
    filtrate2_input_weight = st.number_input("Filtrate 2 - Input Weight (g)", format="%.2f")
    filtrate2_output_weight = st.number_input("Filtrate 2 - Output Weight (g)", format="%.4f")
    filtrate2_residue = filtrate2_tin_weight - filtrate2_output_weight
    filtrate2_evap_residue = filtrate2_residue / filtrate2_input_weight if filtrate2_input_weight else 0

    st.subheader("Water 1")
    water1_tin_weight = st.number_input("Water 1 - Tin Weight (g)", step=0.0001, format="%.4f")
    water1_input_weight = st.number_input("Water 1 - Input Weight (g)", format="%.2f")
    water1_output_weight = st.number_input("Water 1 - Output Weight (g)", format="%.4f")
    water1_residue = water1_tin_weight - water1_output_weight
    water1_evap_residue = water1_residue / water1_input_weight if water1_input_weight else 0

    st.subheader("Water 2")
    water2_tine_weight = st.number_input("Water 2 - Tin Weight (g)", step=0.0001, format="%.4f")
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
    st.header("Coarse Screen")
    st.subheader("Stock Consistency")
    filter_paper = st.number_input("Filter Paper", step=0.0001, format="%.4f")
    water_input = st.number_input("Input Weight", step=0.0001, format="%.4f")
    output_weight = st.number_input("Output Weight", step=0.0001, format="%.4f")
    residue_oven_dry = output_weight - filter_paper
    
    if water_input and water_input != 0:
        stock_consistency = (residue_oven_dry / water_input) * 100 
        st.write(f"Stock Consistency: {stock_consistency:.2f} %")
    else:
        st.warning("Input Weight is zero or missing — cannot calculate stock consistency.")

    st.subheader("Coarse Rejects")
    coarse_tin_weight = st.number_input("Coarse Rejects - Tin Weight (g)", step=0.0001, format="%.4f")
    coarse_output_weight = st.number_input("Coarse Rejects - Output Weight (g)", format="%.4f")
    coarse_reject = (coarse_output_weight - coarse_tin_weight) if coarse_tin_weight else 0
    percentage_to_sample = coarse_reject/50 * 100 if coarse_reject else 0
    st.write(f"Coarse: {percentage_to_sample:.2f} %")

    # ---- Fine Screen ----
with tabs[4]:
    st.subheader("Fine Rejects")
    fine_tin_weight = st.number_input("Fine Rejects - Tin Weight (g)", step=0.0001, format="%.4f")
    fine_output_weight = st.number_input("Fine Rejects - Output Weight (g)", format="%.4f")
    fine_reject = (fine_output_weight - fine_tin_weight) if fine_tin_weight else 0
    percentage_to_sample_fine = fine_reject/20 * 100 if fine_reject else 0
    st.write(f"Fine: {percentage_to_sample_fine:.2f} %")

    # ---- Macrostickies ----
with tabs[5]:
    st.header("Macrostickies AREA Data")
    import pandas as pd
    import numpy as np
    st.write("Paste AREA data below (Screening 1 and Screening 2):")
    set_numbers = ["150 - 200 µm", "200 - 300 µm", "300 - 400 µm", "400 - 500 µm", "500 - 600 µm", "600 - 1000 µm", "1000 - 1500µm", "1500 - 2000µm", "2000 - 3000µm", "3000 - 5000µm", "5000 - 10000µm", "10000 - 20000µm", "20000 - 50000µm", "50000 - 200000µm", "150 - 200000µm"]
    num_sets = len(set_numbers)
    initial_data = {
        "Set Number": set_numbers,
        "Screening 1": [0.00] * num_sets,
        "Screening 2": [0.00] * num_sets
    }
    df = pd.DataFrame(initial_data)
    edited_df = st.data_editor(df, num_rows="dynamic", key="area_data")
    # Calculate mean and stdev for each row
    edited_df["Mean"] = edited_df[["Screening 1", "Screening 2"]].mean(axis=1).round(2)
    edited_df["Std Dev"] = edited_df[["Screening 1", "Screening 2"]].std(axis=1).round(2)

    # Replace last row with totals
    total_row = {
        "Set Number": "150 - 200000µm",
        "Screening 1": round(edited_df["Screening 1"].sum(), 2),
        "Screening 2": round(edited_df["Screening 2"].sum(), 2),
        "Mean": round(edited_df["Mean"].sum(), 2),
        "Std Dev": round(edited_df["Std Dev"].sum(), 2)
    }
    results_df = edited_df.copy()
    results_df.iloc[-1] = total_row
    st.write("Results:")
    display_df = results_df.copy()
    display_df["Screening 1"] = display_df["Screening 1"].map(lambda x: f"{x:.2f}")
    display_df["Screening 2"] = display_df["Screening 2"].map(lambda x: f"{x:.2f}")
    display_df["Mean"] = display_df["Mean"].map(lambda x: f"{x:.2f}")
    display_df["Std Dev"] = display_df["Std Dev"].map(lambda x: f"{x:.2f}")
    st.table(display_df)

    st.header("Macrostickies Number Data")
    import pandas as pd
    import numpy as np
    st.write("Paste NUMBER data below (Screening 1 and Screening 2):")
    set_numbers = ["150 - 200 µm", "200 - 300 µm", "300 - 400 µm", "400 - 500 µm", "500 - 600 µm", "600 - 1000 µm", "1000 - 1500µm", "1500 - 2000µm", "2000 - 3000µm", "3000 - 5000µm", "5000 - 10000µm", "10000 - 20000µm", "20000 - 50000µm", "50000 - 200000µm", "150 - 200000µm"]
    num_sets = len(set_numbers)
    initial_data_1 = {
        "Set Number": set_numbers,
        "Screening 1": [0.00] * num_sets,
        "Screening 2": [0.00] * num_sets
    }
    df = pd.DataFrame(initial_data_1)
    edited_1_df = st.data_editor(df, num_rows="dynamic", key="number_data")
    edited_1_df["Mean"] = edited_1_df[["Screening 1", "Screening 2"]].mean(axis=1).round(2)
    edited_1_df["Std Dev"] = edited_1_df[["Screening 1", "Screening 2"]].std(axis=1).round(2)

    total_row = {
        "Set Number": "150 - 200000µm",
        "Screening 1": round(edited_1_df["Screening 1"].sum(), 2),
        "Screening 2": round(edited_1_df["Screening 2"].sum(), 2),
        "Mean": round(edited_1_df["Mean"].sum(), 2),
        "Std Dev": round(edited_1_df["Std Dev"].sum(), 2)
    }
    results1_df = edited_1_df.copy()
    results1_df.iloc[-1] = total_row
    st.write("Results:")
    display1_df = results1_df.copy()
    display1_df["Screening 1"] = display1_df["Screening 1"].map(lambda x: f"{x:.2f}")
    display1_df["Screening 2"] = display1_df["Screening 2"].map(lambda x: f"{x:.2f}")
    display1_df["Mean"] = display1_df["Mean"].map(lambda x: f"{x:.2f}")
    display1_df["Std Dev"] = display1_df["Std Dev"].map(lambda x: f"{x:.2f}")
    st.table(display1_df)

    # ---- Scorecard ----
with tabs[6]:
    st.header("Scorecard")
    st.write("To be added")
    total_yield = (100 - percentage_to_sample-percentage_to_sample_fine)
    st.write(f"Total Yield: {total_yield:.2f} %")

    #---- Dial -----
with tabs[7]:
    st.header("Dial")
    st.write("To be added")
    
