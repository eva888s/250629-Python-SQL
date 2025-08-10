#請幫我自訂一個function
#連線至postgres DB
#建立連線環境參數的樣版

import psycopg2

def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    return result

def create_connection():
    conn = psycopg2.connect(
        host="dpg-d2bvmo7diees73f5fn8g-a.singapore-postgres.render.com",
        database="chillee_sunday",
        user="chillee_sunday_user",
        password="KRsZo4u7MMXmHLhPo36FN4PeRZBkkQt4",
        port="5432"
    )
    return conn


def main():
    conn = create_connection()
    if conn:
        print("成功連接到資料庫！")
        query = """
        SELECT count(*) AS "筆數"
        FROM "台鐵車站資訊";
        """
        result = execute_query(conn, query)
        print("台鐵車站資訊：", result)
        conn.close()
    else:
        print("無法連接到資料庫，請檢查設定。")
        return

if __name__ == "__main__":
    main()