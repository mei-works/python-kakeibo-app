print("家計簿アプリへようこそ！")
import csv

import os

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Hiragino Sans"

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "data2.csv")

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # 最初の１行をスキップ

    data = {}
    expense_category = {}

    for row in reader:
        amount = int(row[2])  # 金額（3列目）
        type = row[3]  # 種類（4列目）
        category = row[1] #項目

        month = row[0][:7]  
        month = month.replace("-", "年", 1) + "月"

        if len(row[0]) != 10:
            print("日付ミス:", row[0])

        if month not in data:
            data[month] = {"income": 0, "expense": 0}

        # 振り分け
        if type == "収入":
            data[month]["income"] += amount
        else:
            data[month]["expense"] += amount
            expense_category[category] = expense_category.get(category, 0) + amount
    
    for month in data:
        income = data[month]["income"]
        expense = data[month]["expense"]
        balance = income - expense

        print(month)
        print("収入:", income)
        print("支出:", expense)
        print("収支:", balance)

        if balance > 0:
            print("黒字！いい感じです👍")
        elif balance == 0:
            print("ちょうどですね")
        else:
            print("支出を見直してみましょう")
        print("------")

# グラフ用データ作成
months = list(data.keys())
expenses = [data[m]["expense"] for m in months]
incomes = [data[m]["income"] for m in months]

# 棒グラフ
import numpy as np

x = np.arange(len(months))  # 位置
width = 0.4  # 棒の幅

# 色指定
expense_color = "#8A2BE2"   
income_color  = "#DDA0DD"   


plt.bar(x - width/2, expenses, width=width, label="支出", color=expense_color)
plt.bar(x + width/2, incomes, width=width, label="収入", color=income_color)

offset = max(max(incomes), max(expenses)) * 0.05

for i in range(len(months)):
    income = incomes[i]
    expense = expenses[i]
    balance = incomes[i] - expenses[i]

    plt.text(x[i] + width/2, income, str(income), ha='center', va='bottom')
    plt.text(x[i] - width/2, expense, str(expense), ha='center', va='bottom')

    plt.text(x[i], max(income, expense) + offset, 
             f"収支:{balance}", 
             ha='center', va='bottom', fontsize=9, color="black")

plt.xticks(x, months)
plt.legend()

plt.title("月別の収入と支出")
plt.ylabel("金額（円）")


plt.show()

#円グラフ
expense_category.get(category, 0) + amount

labels = list(expense_category.keys())
values = list(expense_category.values())

color_map = {
    "食費": "#8A2BE2",
    "カード引落": "#6A5ACD",
    "交通費": "#9370DB",
    "娯楽": "#BA55D3",
    "日用品": "#DDA0DD",
    "雑費": "#483D8B"
}

colors = [color_map.get(label, "#CCCCCC")for label in labels]

plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90, colors = colors)
plt.title("支出の内訳")
plt.show()

