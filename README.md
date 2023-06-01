# teams_reminder
このプログラムはMicrosoft Teamsのリマインダーです。
チーム内のゼミやミーティングのリマインド機能としての使用を目的としています。


Teamsアプリ上にあるincoming_webhookからアドレスをコピーして、それをreminder.pyの"webhook_url"のところに貼り付けてください。

jsonファイル内bodyにある"zoom URL"や"documents URL"にzoomのミーティングのURLや共有書類のURLを貼り付けることでボックスが生成されます。
bodyにある<at></at>とentitiesにある<at></at>にアカウント名、entitiesにあるIDのにメールアドレス、nameにアカウント名をいれるとteamsでメンションができるようになります。


# リマインドさせる方法

LinuxやmacOSにあるcronを用います。
ターミナル上で
```
crontab -e
```
をして、cronの中に
```
30 15 * * 1 ~/anaconda3/bin/python ~/teams_reminder/reminder.py
```
などとpythonのPATHとreminder.pyのPATHを書き込むことで指定した曜日時間にリマインドすることができます。

```
30 15 * * 1
```
はそれぞれ、分、時、日、月、曜日を表しています。
```
分　0~59
時　0~23
日　1~31
月　1~12
曜日 1(月), 2(火), 3(水), 4(木), 5(金), 6(土), 7(日)
```
を表しています。そのため、
```
30 15 * * 1
```
は毎週月曜日の15:30にリマインドされ、
```
10 11 13 * * *
```
とすると、毎月13日の11時10分にリマインドされという仕組みになっています。
