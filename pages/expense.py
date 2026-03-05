import streamlit as st
import matplotlib.pyplot as plt
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

fr = {
    "expected_yeild": 0.0,
    "actual_yeild": 0.0,
    "market_rate": 0.0,
    "maintenance_costs": 0.0,
    "labour_costs": 0.0,
    "capital_expenses": 0.0,
    "total_expenses": 0.0,
    "revenue": 0.0,
    "profit": 0.0,
    "yeild_change": 0.0,
}

st.header("Expense Report")

with st.form(key="farm_expenses"):
    fr["expected_yeild"] = st.number_input("Expected yield (kg)", min_value=0.0)
    fr["actual_yeild"] = st.number_input("Actual yield (kg)", min_value=0.0)
    fr["market_rate"] = st.number_input("Market rate per kg (₹)", min_value=0.0)
    fr["maintenance_costs"] = st.number_input("Maintenance costs (₹)", min_value=0.0)
    fr["labour_costs"] = st.number_input("Labour costs (₹)", min_value=0.0)
    fr["capital_expenses"] = st.number_input("Capital expenses (₹)", min_value=0.0)
    
    submit_ans = st.form_submit_button(label="Submit")

if submit_ans:
    fr["total_expenses"] = fr["maintenance_costs"] + fr["labour_costs"] + fr["capital_expenses"]
    fr["revenue"] = fr["actual_yeild"] * fr["market_rate"]
    fr["profit"] = fr["revenue"] - fr["total_expenses"]
    fr["yeild_change"] = ((fr["actual_yeild"] - fr["expected_yeild"]) / fr["expected_yeild"] * 100) if fr["expected_yeild"] > 0 else 0

    st.subheader("Summary Report")
    st.write(f"Total Revenue: ₹{fr['revenue']:.2f}")
    st.write(f"Total Expenses: ₹{fr['total_expenses']:.2f}")
    st.write(f"Net Profit/Loss: ₹{fr['profit']:.2f}")
    st.write(f"Yield Change: {fr['yeild_change']:.2f}%")

    if fr["profit"] > 0:
        st.success("You made a profit this cycle.")
    else:
        st.error("Loss detected. Try optimizing costs or reviewing farming practices.")

    # Pie chart (natural theme)
    st.subheader("Cost Breakdown")
    labels = ["Maintenance", "Labour", "Capital"]
    values = [fr["maintenance_costs"], fr["labour_costs"], fr["capital_expenses"]]
    colors = ["#88B04B", "#A3C1AD", "#C2B280"]  # natural greens and earth tones

    fig, ax = plt.subplots(figsize=(4, 4))
    ax.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
    ax.set_title("Cost Distribution")
    ax.axis("equal")
    st.pyplot(fig)

    # Bar graph (natural theme)
    st.subheader("Yield & Revenue Comparison")
    categories = ["Expected Yield", "Actual Yield", "Total Cost", "Revenue"]
    values = [fr["expected_yeild"], fr["actual_yeild"], fr["total_expenses"], fr["revenue"]]
    bar_colors = ["#BFD8B8", "#7DA97C", "#C19A6B", "#6B8E23"]

    fig2, ax2 = plt.subplots(figsize=(5, 3))
    bars = ax2.bar(categories, values, width=0.5, color=bar_colors)
    ax2.set_ylabel("Value")
    ax2.set_title("Yield vs Revenue & Cost Overview")
    ax2.tick_params(axis="x", rotation=20)

    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2, height, f"{height:.1f}", ha="center", va="bottom", fontsize=8)

    st.pyplot(fig2)

    # PDF generation
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, height - 50, "Farm Expense Report")

    c.setFont("Helvetica", 12)
    y = height - 100
    for key, value in fr.items():
        c.drawString(50, y, f"{key.replace('_', ' ').title()}: {value}")
        y -= 20

    c.save()
    pdf_buffer.seek(0)

    st.download_button(
        label="Download PDF Report",
        data=pdf_buffer,
        file_name="farm_report.pdf",
        mime="application/pdf"
    )
