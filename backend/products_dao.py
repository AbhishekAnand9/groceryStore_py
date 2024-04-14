import mysql.connector
from sql_connection import get_sql_connection


def get_all_products():
    
    cursor=connection.cursor()

    query=("SELECT products.product_id , products.prooduct_name , products.uom_id , products.price_per_unit , "
            "uom.uon_name from products inner join uom on uom.uom_id=products.uom_id ")

    cursor.execute(query)
    responce = []
    
    for (product_id, prooduct_name, uom_id, price_per_unit,uon_name) in cursor:
        responce.append({
            'product_id' : product_id,
            'prooduct_name': prooduct_name,
            'uom_id':uom_id,
            'price_per_unit' : price_per_unit,
            'uon_name' : uon_name
        })
        
    
    return responce

def insert_new_product(connection,product):
    cursor=connection.cursor()
    
    query=("insert into products (prooduct_name, uom_id , price_per_unit) values(%s ,%s ,%s)")
    
    data=(product['prooduct_name'], product['uom_id'], product['price_per_unit'])
    
    cursor.execute(query,data)
    
    connection.commit()
    
    return cursor.lastrowid
   
def delete_product(connection,product_id):
    cursor=connection.cursor()
    query=("DELETE FROM products WHERE product_id="+str(product_id))
    cursor.execute(query)
    connection.commit()
    
if __name__ == '__main__':
    connection= get_sql_connection()
    
    # print(insert_new_product(connection,{
    #     'prooduct_name':'Broocolli',
    #     'uom_id' : '1',
    #     'price_per_unit' : '20'
    # }))
    print(delete_product(connection, 6))
    
