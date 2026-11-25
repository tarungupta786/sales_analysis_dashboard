import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Sales Insights Dashboard", page_icon="📊", layout="wide")
st.title("📊 Sales Data Analysis Dashboard")
st.caption("Explore revenue, products, categories, regions, and sales trends.")

REQUIRED_COLUMNS = {"Order Date", "Product", "Category", "Region", "Units Sold", "Unit Price"}

@st.cache_data
def load_sample_data():
    df = pd.read_csv(Path(__file__).parent / "sample_sales.csv", parse_dates=["Order Date"])
    df["Revenue"] = df["Units Sold"] * df["Unit Price"]
    return df

uploaded_file = st.sidebar.file_uploader("Upload your sales CSV", type=["csv"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        missing = REQUIRED_COLUMNS - set(df.columns)
        if missing:
            st.error("Missing required columns: " + ", ".join(sorted(missing)))
            st.info("Use sample_sales.csv as a template.")
            st.stop()
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
        df["Units Sold"] = pd.to_numeric(df["Units Sold"], errors="coerce")
        df["Unit Price"] = pd.to_numeric(df["Unit Price"], errors="coerce")
        df = df.dropna(subset=["Order Date", "Product", "Category", "Region", "Units Sold", "Unit Price"])
        df["Revenue"] = df["Units Sold"] * df["Unit Price"]
    except Exception as exc:
        st.error(f"Could not read the uploaded file: {exc}")
        st.stop()
else:
    df = load_sample_data()
    st.sidebar.info("Showing fictional sample data. Upload your own CSV to analyze it.")

if df.empty:
    st.warning("No valid sales rows were found.")
    st.stop()

st.sidebar.header("Filters")
min_date, max_date = df["Order Date"].min().date(), df["Order Date"].max().date()
date_range = st.sidebar.date_input("Order date range", value=(min_date, max_date), min_value=min_date, max_value=max_date)
if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date, end_date = min_date, max_date

categories = sorted(df["Category"].dropna().unique())
regions = sorted(df["Region"].dropna().unique())
products = sorted(df["Product"].dropna().unique())
selected_categories = st.sidebar.multiselect("Category", categories, default=categories)
selected_regions = st.sidebar.multiselect("Region", regions, default=regions)
selected_products = st.sidebar.multiselect("Product", products, default=products)

filtered = df[
    (df["Order Date"].dt.date >= start_date) &
    (df["Order Date"].dt.date <= end_date) &
    (df["Category"].isin(selected_categories)) &
    (df["Region"].isin(selected_regions)) &
    (df["Product"].isin(selected_products))
].copy()

if filtered.empty:
    st.warning("No sales match the selected filters. Change your filters to see results.")
    st.stop()

total_revenue = filtered["Revenue"].sum()
total_units = filtered["Units Sold"].sum()
record_count = len(filtered)
avg_revenue = total_revenue / record_count if record_count else 0
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
c2.metric("Units Sold", f"{total_units:,.0f}")
c3.metric("Sales Records", f"{record_count:,}")
c4.metric("Average Revenue / Record", f"₹{avg_revenue:,.0f}")

st.divider()
left, right = st.columns(2)
with left:
    st.subheader("Revenue over time")
    monthly = filtered.assign(Month=filtered["Order Date"].dt.to_period("M").astype(str)).groupby("Month", as_index=False)["Revenue"].sum()
    fig = px.line(monthly, x="Month", y="Revenue", markers=True, title="Monthly revenue")
    fig.update_layout(xaxis_title="", yaxis_title="Revenue (₹)")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Revenue by category")
    category_sales = filtered.groupby("Category", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)
    fig = px.bar(category_sales, x="Category", y="Revenue", title="Category performance", text_auto=".2s")
    fig.update_layout(xaxis_title="", yaxis_title="Revenue (₹)")
    st.plotly_chart(fig, use_container_width=True)

left, right = st.columns(2)
with left:
    st.subheader("Top products")
    product_sales = filtered.groupby("Product", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False).head(10)
    fig = px.bar(product_sales.sort_values("Revenue"), x="Revenue", y="Product", orientation="h", title="Top products by revenue", text_auto=".2s")
    fig.update_layout(xaxis_title="Revenue (₹)", yaxis_title="")
    st.plotly_chart(fig, use_container_width=True)
with right:
    st.subheader("Revenue by region")
    region_sales = filtered.groupby("Region", as_index=False)["Revenue"].sum().sort_values("Revenue", ascending=False)
    fig = px.pie(region_sales, names="Region", values="Revenue", hole=0.35, title="Regional contribution")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Filtered sales data")
display_df = filtered.sort_values("Order Date", ascending=False).copy()
display_df["Order Date"] = display_df["Order Date"].dt.strftime("%Y-%m-%d")
st.dataframe(display_df, use_container_width=True, hide_index=True)
st.download_button("⬇️ Download filtered data as CSV", data=filtered.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_sales_data.csv", mime="text/csv")

st.subheader("Quick insights")
best_product = product_sales.iloc[-1]["Product"] if not product_sales.empty else "N/A"
best_category = category_sales.iloc[0]["Category"] if not category_sales.empty else "N/A"
best_region = region_sales.iloc[0]["Region"] if not region_sales.empty else "N/A"
st.markdown(f"- **Top product by revenue:** {best_product}\n"
            f"- **Top category by revenue:** {best_category}\n"
            f"- **Top region by revenue:** {best_region}\n"
            f"- **Date range analyzed:** {start_date} to {end_date}")
st.caption("The included dataset is fictional and intended for learning and demonstration.")
