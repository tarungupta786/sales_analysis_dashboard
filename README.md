# Sales Data Analysis and Visualization Dashboard

A beginner-friendly project using Python, Streamlit, Pandas, and Plotly.

## Features
- Upload a sales CSV file
- Filter by date, category, region, and product
- KPI cards for revenue, units sold, sales records, and average revenue per record
- Monthly revenue trend
- Revenue by category
- Top products by revenue
- Revenue contribution by region
- View and download filtered data
- Quick insights based on selected filters

## Run locally

Python 3.10+ is recommended.

### Linux / macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### Windows
```powershell
py -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
streamlit run app.py
```

Streamlit normally opens at `http://localhost:8501`.

## CSV columns required
`Order Date`, `Product`, `Category`, `Region`, `Units Sold`, `Unit Price`

The dashboard calculates `Revenue = Units Sold × Unit Price`.

`sample_sales.csv` contains fictional sample records, not real company data.
