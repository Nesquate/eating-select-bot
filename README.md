# 吃飯吃什麼機器人
一個專門用來對付「吃飯到底要吃什麼」情境的機器人

__正在開發中，相關內容會有大幅度變化__

## 目的
由於有時候決定下一餐要吃什麼的時候會猶豫不決，所以打算寫一個 Discord bot 來解決相關問題。

個人想要在隨機功能上增加更多功能，例如可以直接查地圖等。


## 安裝與使用
首先使用 [Git](https://git-scm.com/) 將整個專案 Clone 下來
```shell
git clone https://github.com/Nesquate/eating-select-bot
```

之後使用 [Poetry](https://python-poetry.org/) 將虛擬環境安裝起來
```shell
poetry install
```

安裝好沒問題之後，進入虛擬環境

```shell
poetry shell
```

建立 `.env` 檔案，並在檔案內填寫 `BOT_TOKEN` 資訊
```text
BOT_TOKEN = ""
```

一切就緒之後即可執行 Bot
```shell
python main.py
```


## 目標 (v 1.0)
- [ ] 打指令跳出隨機地點與詳細資訊
- [ ] 可以用指令搜尋特定餐點的商家
- [ ] 地點詳細資訊有相關按鈕 (可以叫出菜單、小地圖、使用者評價)
- [ ] 地點詳細資訊有喜好選擇 (喜歡/不喜歡)
- [ ] 運用機器學習計算使用者的餐點喜好