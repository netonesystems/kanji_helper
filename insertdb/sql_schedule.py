import MySQLdb

# DBに接続しカーソルを取得する
connect = MySQLdb.connect(host='localhost', port=3306, user='reg', passwd='reg' , db='regist', charset='utf8')
cursor = connect.cursor()

id = 3
date = "2018-08-30 19:00:05"
personid = "1"
#参照先キーが無いとエラーになる
eventid = "111"
#参照先にキーが無いとエラーになる
attendance = 1

cursor.execute("INSERT INTO kanji_helper.schedule (id, date, personid, eventid, attendance) VALUES (%s, %s, %s, %s, %s)" % (connect.literal(id), connect.literal(date), connect.literal(personid), connect.literal(eventid), connect.literal(attendance)))

connect.commit()    # コミットする
cursor.close()
connect.close()     # データベースオジェクトを閉じる
