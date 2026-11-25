📊 Sales Insights Dashboard

An interactive Streamlit dashboard for exploring sales data. Upload your own CSV (or use the built-in sample data) and instantly see revenue, products, categories, regions and monthly trends, with filters and CSV export.

The included sample_sales.csv is fictional and meant for learning and demonstration.

📌 Table of Contents
Features
Tech Stack
Project Structure
Getting Started
Using Your Own Data
Dashboard Walkthrough
Future Improvements
License
Author
✨ Features
Upload your own CSV or explore the bundled sample dataset
Smart validation: clear error messages for missing columns, and invalid rows are cleaned automatically
Sidebar filters: order date range, category, region and product
KPI cards: Total Revenue, Units Sold, Sales Records, Average Revenue per Record
Interactive Plotly charts:
Monthly revenue trend (line)
Revenue by category (bar)
Top 10 products by revenue (horizontal bar)
Regional contribution (donut)
Filtered data table with one-click CSV download
Quick insights: top product, category and region at a glance
Handles empty data and empty filter results gracefully
🛠 Tech Stack
Area	Tools
Framework	Streamlit
Data processing	Pandas
Visualization	Plotly Express
Language	Python 3.9+
📁 Project Structure
sales_analysis_dashboard/
├── app.py              # Streamlit dashboard
├── sample_sales.csv    # Fictional sample dataset (also usable as a template)
├── requirements.txt    # Python dependencies
├── LICENSE
└── README.md

If your main file has a different name, replace app.py in this README.

🚀 Getting Started
Clone the repository
bash
git clone https://github.com/tarungupta786/sales_analysis_dashboard.git
cd sales_analysis_dashboard
(Optional) Create a virtual environment
bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
Install dependencies
bash
pip install -r requirements.txt

Or install manually: pip install streamlit pandas plotly 4. Run the app

bash
streamlit run app.py
Open the local URL shown in your terminal (usually http://localhost:8501).
📂 Using Your Own Data

Upload a CSV from the sidebar. It must contain these columns:

Column	Description
Order Date	Date of the sale (e.g. 2025-03-15)
Product	Product name
Category	Product category
Region	Sales region
Units Sold	Number of units (numeric)
Unit Price	Price per unit (numeric)

Revenue is calculated automatically as Units Sold × Unit Price. Rows with missing or invalid values in these columns are dropped. Use sample_sales.csv as a template.

🧭 Dashboard Walkthrough
Filter the data using the sidebar (dates, categories, regions, products).
Read the KPIs at the top for a quick performance summary.
Explore the charts to spot trends, best sellers and strong regions.
Download the filtered table as CSV for further analysis.
🔮 Future Improvements
Sales forecasting
Profit and discount analysis
Customer segmentation
Deployment on Streamlit Community Cloud
Support for Excel uploads
📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

👤 Author

Tarun Gupta GitHub: @tarungupta786

⭐ If you found this project useful, consider giving it a star!