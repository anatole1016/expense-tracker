import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
from storage import load_expenses

def data_frame():
    expenses = load_expenses()
    df = pd.DataFrame(expenses)
    df["date"] = pd.to_datetime(df["date"])
    return df

def category_expenses():
    df = data_frame()
    if df.empty:
        print("No data to plot.")
        return
    category_totals = df.groupby("category")["amount"].sum()
    plt.figure()
    plt.pie(
    category_totals,
        labels=category_totals.index,
        autopct="%1.1f%%"
    )
    plt.title("Expenses by Category")
    plt.tight_layout()
    plt.show()