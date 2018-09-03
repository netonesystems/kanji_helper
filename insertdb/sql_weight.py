import MySQLdb

# DBに接続しカーソルを取得する
connect = MySQLdb.connect(host='localhost', port=3306, user='reg', passwd='reg' , db='regist', charset='utf8')
cursor = connect.cursor()

id = 3
personid = 1
eventid = 3
weight = 100

cursor.execute("INSERT INTO kanji_helper.weight (id, personid, eventid, weight) VALUES (%s, %s, %s, %s)" % (connect.literal(id), connect.literal(personid), connect.literal(eventid), connect.literal(weight)))

connect.commit()    # コミットする
cursor.close()
connect.close()     # データベースオジェクトを閉じる
