import json
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_PATH = Path("data/projects.json")


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    with open(path) as f:
        projects = json.load(f)

    records = []
    for proj in projects:
        for panel in proj["panel_data"]:
            for day, yield_kwh in enumerate(panel["daily_yield_kwh"], start=1):
                records.append({
                    "project_id": proj["project_id"],
                    "customer_region": proj["customer_region"],
                    "installation_date": proj["installation_date"],
                    "system_size_kwp": proj["system_size_kwp"],
                    "panel_id": panel["panel_id"],
                    "day": day,
                    "yield_kwh": yield_kwh,
                })
    return pd.DataFrame(records)


def main():
    st.title("PV & Heat Pump Projects")
    df = load_data(DATA_PATH)

    region = st.selectbox("Region", sorted(df["customer_region"].unique()))
    filtered = df[df["customer_region"] == region]

    project_option = st.selectbox(
        "Project", sorted(filtered["project_id"].unique())
    )

    project_df = filtered[filtered["project_id"] == project_option]

    st.subheader("Daily Yield per Panel")
    chart_df = project_df.pivot_table(
        index="day", columns="panel_id", values="yield_kwh"
    )
    st.line_chart(chart_df)

    st.subheader("Project Metrics")
    info = project_df.iloc[0]
    st.write(
        f"System size: {info.system_size_kwp} kWp | "
        f"Panels: {project_df['panel_id'].nunique()}"
    )


if __name__ == "__main__":
    main()
