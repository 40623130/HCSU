var tipuesearch = {"pages": [{'title': 'About', 'text': '成員: \n 葉修宏 \n 張育瑋 \n 張華倞 \n 陳鉅忠 \n 此網站專門記錄專題完成進度，以便隨後整理至最後報告使用。 \n Blog用以填寫日誌 \n', 'tags': '', 'url': 'About.html'}, {'title': 'Repair 3D Printer', 'text': '', 'tags': '', 'url': 'Repair 3D Printer.html'}, {'title': 'Air-Hockey', 'text': '', 'tags': '', 'url': 'Air-Hockey.html'}, {'title': 'Onshape', 'text': '圖檔連結 \n', 'tags': '', 'url': 'Onshape.html'}, {'title': 'CoppeliaSim', 'text': '測試程式用設定檔 \n 測試程式用圖檔為精簡化圖檔，除去所以與控制程式運行不相干之物件，僅用於控制程式編寫。 \n 完整版設定檔 \n 完整版設定檔為保留所有實際物體之圖檔 \n', 'tags': '', 'url': 'CoppeliaSim.html'}, {'title': '測試用圖檔設定', 'text': '測試用球桌圖檔(Onshape) \n 首先需要 簡易 球桌與球，如下圖 \n 並將圖檔以stl格式匯出 \n \n 匯入CoppeliaSim(V-rep) \n File \xa0\xa0 → Import\xa0→ Mesh \n 點選Import \n \n 拆解組合圖 \n 左鍵選取需拆解之零件 \n 點選右鍵\xa0 → Edit → Grouping/Merging\xa0→ Divide selected shapes \n 完成後圖檔會從組合拆解為各自零件 \n \n 更改球體顏色(用於影像辨識) \n 左鍵點選欲更改之物件\xa0 →\xa0 點選左側工具欄之放大鏡\xa0→\xa0 Adjust color\xa0\xa0→ Ambient/diffuse component\xa0→ \xa0 \xa0使用RGB或HSL調整顏色 \n \n 自由度設定 \n 新增一個立方體用以固定左右移動軸 \n 新增滑動接頭 \n \n 固定至相應位置，並更改樹狀資料如下圖 \n (球桌短邊命名為X、長 邊命名為Y ) \n \n 另一邊步驟與上面相同 \n \n', 'tags': '', 'url': '測試用圖檔設定.html'}, {'title': '內部程式', 'text': '', 'tags': '', 'url': '內部程式.html'}, {'title': '外部程式', 'text': '', 'tags': '', 'url': '外部程式.html'}, {'title': 'Circuit', 'text': '利用Fritzing完成簡易版的配線圖 \n 使用到 :\xa0 \n 42步進馬達 42BYGH47 1.7A 0.55Nm 12V\xa0 *3 \n A4988 馬達驅動器 *2 \n 極限開關 *2 \n Arduino UNO R3\xa0 *1 \n Arduino cnc shield v3 *1 \n 風扇 *1 \n 24V電供器 *1 \n 傳輸線 *1 \n', 'tags': '', 'url': 'Circuit.html'}, {'title': 'Q&A', 'text': '', 'tags': '', 'url': 'Q&A.html'}, {'title': '如何編輯此網站', 'text': '請先clone本 倉儲 \n 倉儲內有一個資料夾(cmsimde)此時會是空的 \n 再來利用cmd進入 本倉儲 並輸入\xa0 \n git submodule init \n 以及 \n git submodule update \n 跑完後資料夾(cmsimde)裡面會有檔案 \n 如果要編輯跟之前不同之處只差在要執行的wsgi.py在資料夾(cmsimde)裡面 \n 所以只要先輸入 \n cd cmsimde \n 再輸入 \n python wsgi.py \n 之後就可以進行編輯了', 'tags': '', 'url': '如何編輯此網站.html'}]};