import MySQLdb

# DBに接続しカーソルを取得する
connect = MySQLdb.connect(host='localhost', port=3306, user='reg', passwd='reg' , db='regist', charset='utf8')
cursor = connect.cursor()

id = 3
eventname = "kensuke"
description = "TokyoSta"
area = "Yaesu"
start_time = "2018-08-30 19:00:05"
end_time = "2018-08-30 20:00:00"

cursor.execute("INSERT INTO kanji_helper.event (id, eventname, description, area, start_time, end_time) VALUES (%s, %s, %s, %s, %s, %s)" % (connect.literal(id), connect.literal(eventname), connect.literal(description), connect.literal(area), connect.literal(start_time), connect.literal(end_time)))

connect.commit()    # コミットする
cursor.close()
connect.close()     # データベースオジェクトを閉じる
