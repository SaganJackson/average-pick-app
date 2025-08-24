import streamlit as st
import pandas as pd
from io import BytesIO

st.title("Average Pick Calculator")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file is not None:
    # Read Excel File
    df = pd.read_excel(uploaded_file)

    # Calculate average picks
    avg_picks = df.groupby("Player", as_index=False)["Pick"].mean()
    avg_picks.rename(columns={"Pick": "Average Pick"}, inplace=True)

    # Sort results from lowest to highest average pick
    avg_picks = avg_picks.sort_values(by="Average Pick", ascending=True)

    # Reset index so numbers are in order
    avg_picks = avg_picks.reset_index(drop=True)

    # Make the index start at 1
    avg_picks.index = avg_picks.index + 1

    #Show results in table
    st.subheader("Results")
    st.dataframe(avg_picks)

    #Convert dataframe to Excel for download
    output = BytesIO()
    avg_picks.to_excel(output, index=False, engine="openpyxl")
    st.download_button(
        label="Download Results as Excel",
        data=output.getvalue(),
        file_name="player_average_picks.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
