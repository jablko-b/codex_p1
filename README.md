# PV & Heat Pump Demo

This repository contains a small synthetic dataset of photovoltaic (PV) and heat pump projects as well as a simple Streamlit dashboard to explore the data.

## Setup

Install the required packages and generate the dataset:

```bash
pip install -r requirements.txt
python generate_dataset.py
```

Run the Streamlit app:

```bash
streamlit run dashboard.py
```

The app allows you to select a region and project to view daily yields for each panel.
