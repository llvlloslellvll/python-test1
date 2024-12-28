import psycopg2 as psy
import pandas as pd
def excelDb (route = '') :
    if route != '' :
        df = pd.read_excel(route)

        conn = psy.connect(
            database="first",
            user='postgres',
            password='moslem',
            host='localhost',
            port='5432'
        )

        cursor = conn.cursor()

        a = []
        for index, row in df.iterrows():
            a.append("('" + row['name'] + "', '" + row['time'] + "')")

        cursor.execute("INSERT INTO test (firstname, lastname) VALUES " + ",".join(a))
        conn.commit()
        cursor.execute("SELECT * FROM test")

        return cursor.fetchall()


db_values = excelDb("c:\\Users\\MosleM\\PycharmProjects\\PythonProject\\files\\exo.xlsx")
for i in db_values:
    print(i)