print("家計簿アプリへようこそ！")
import csv

import os

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, "data.csv")

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # 最初の１行をスキップ

    data = {}

    for row in reader:
        amount = int(row[2])  # 金額（3列目）
        type = row[3]  # 種類（4列目）

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
