def connect_to_database():
    conn = psycopg2.connect(
        host="127.0.0.1",
        database="yüzTanima",
        user="postgres",
        password="1404"
    )
    return conn




def save_image_to_database(image_path, gender, age, emotion, verified):
    conn = connect_to_database()
    cursor = conn.cursor()

    insert_query = "INSERT INTO images (image_path, gender, age, emotion, verified) VALUES (%s, %s, %s, %s, %s)"
    data = (image_path, json.dumps(gender), age, emotion, verified)

    print("Insert Query:", insert_query)
    print("Data:", data)

    cursor.execute(insert_query, data)

    conn.commit()
    cursor.close()
    conn.close()
