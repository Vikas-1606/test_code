import mysql.connector

def insert_product(title: str, price: float, description: str):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mydb",
        port=3306
    )

    cursor = connection.cursor()
    cursor.execute(f"""
    insert into products (title, description, price)
    values ('{title}', '{description}', {price})
    """)
    
    connection.commit()
    cursor.close()
    connection.close()

insert_product('product1',10.50,''this is nice product)