# django_deploy
網站是依照 [simpleisbetterthancomple的教學](https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/的tutorial)為模板打造出來然後增加功能以及進行修改
## 功能介紹
- 使用者註冊、登入和FB進行第三方登入
- 創建有興趣的Board，在Board中發表主題，根據主題可以回覆評論
- 未登入的用戶只能觀看文章
- 登入之用戶可以進行發表主題，編輯和刪除表發過的主題
- 發布主題和回覆支持markdown語法，利用SimpleMDE美化文字編輯器
- 利用cookies紀錄主題的觀看次數
- 提供DOM進行簡易的文章搜索功能
- 網站的評論系統以Django的ContentTypes進行處理，能夠動態的訪問其他model
## 網站技術
- 前端使用Bootstrap4+jQuery支持響應式網頁
- 資料庫使用Postgresql
- 第三方用戶登入使用django-allauth
- 利用套件Faker撰寫python程式產生Fake data讓網站貼近真實性
