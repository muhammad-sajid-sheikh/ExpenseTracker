import streamlit as st
from datetime import date

# ----- Expense Class -----
class Expense:
    def __init__(self, amount, category, date, note):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.note = note

    def __str__(self):
        return f"{self.date} | {self.category} | Rs: {self.amount:.2f} | {self.note}"

# ----- ExpenseTracker Class -----
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_total(self):
        return sum(exp.amount for exp in self.expenses)

    def clear(self):
        self.expenses = []

# ----- App UI -----
st.set_page_config(page_title="Expense Tracker", layout="centered")

st.title("💸 Expense Tracker")

# Initialize session state
if "tracker" not in st.session_state:
    st.session_state.tracker = ExpenseTracker()

# Form to Add Expense
with st.form("expense_form"):
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    category = st.text_input("Category")
    expense_date = st.date_input("Date", value=date.today())
    note = st.text_input("Note (optional)")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        if category:
            exp = Expense(amount, category, expense_date, note)
            st.session_state.tracker.add_expense(exp)
            st.success("Expense added successfully.")
        else:
            st.error("Please enter a category.")

# Show All Expenses
st.subheader("📋 Expenses List")
if st.session_state.tracker.expenses:
    for e in st.session_state.tracker.expenses:
        st.write(str(e))
    st.markdown(f"**Total Spent:** Rs: {st.session_state.tracker.get_total():.2f}")
else:
    st.info("No expenses added yet.")

# Clear All Expenses
if st.button("🗑️ Clear All"):
    st.session_state.tracker.clear()
    st.success("All expenses cleared.")
