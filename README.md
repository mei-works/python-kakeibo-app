# 家計簿アプリ

PythonでCSVデータを読み込み、月ごとの収入・支出・収支を集計・表示するシンプルな家計簿アプリです。

## 機能

* CSVファイルの読み込み
* 収入・支出の分類
* 月ごとの収入・支出・収支の集計
* 収支に応じたコメント表示（黒字・赤字など）
* 月ごとの収入・支出を棒グラフで可視化
* 支出をカテゴリ別に円グラフで可視化

## 工夫した点

* 日付の形式に誤りがある場合に検知できるようにした
* 日付データから月ごとに分類し、月別の収支を表示できるようにした
* 辞書（data構造）を使って、月ごとのデータを管理するようにした
* 収入と支出の違いが直感的に分かるよう、色の濃淡で区別した
* 棒グラフ上の数値や収支のテキストが重ならないよう、表示位置を調整した
  
## 使用技術

* Python
* CSV（標準ライブラリ）


A simple household account app built with Python that reads CSV data and calculates monthly income, expenses, and balance.

## Features

* Reads CSV files
* Classifies income and expenses
* Aggregates monthly income, expenses, and balance
* Displays comments based on balance (profit or deficit)
* Visualizes monthly income and expenses by using a bar chart
* Shows expenses for each category by using a pie chart
  
## Improvements
* Added validation to detect incorrect date formats
* Grouped data by month and calculated monthly balance
* Used a dictionary structure to manage monthly data efficiently
* Used different shades of color to make it easy to distinguish between income and expenses
* Adjusted text positions to prevent numbers from overlapping on the graph

## Technologies Used
* Python
* CSV (standard library)
