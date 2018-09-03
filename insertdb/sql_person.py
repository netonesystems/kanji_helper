import MySQLdb

# DBに接続しカーソルを取得する
connect = MySQLdb.connect(host='localhost', port=3306, user='reg', passwd='reg' , db='regist', charset='utf8')
cursor = connect.cursor()

id = 3
username = "kensuke"
email = "localhost@tet.test"

cursor.execute("INSERT INTO kanji_helper.person (id, username, email) VALUES (%s, %s, %s)" % (connect.literal(id), connect.literal(username), connect.literal(email)))

connect.commit()    # コミットする
cursor.close()
connect.close()     # データベースオジェクトを閉じる
