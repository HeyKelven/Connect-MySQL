# A Biblioteca abaixo é fundamental para que a conexão possa ser feita com o Banco de Dados do MySQL
# Próximo passo conectar com o servidor remoto, e não um servidor local. SERA?
import mysql.connector


def get_ingredients():
    # Alterado o password por motivos claros
    cnx = mysql.connector.connect(user='root', password='<password_here>', host='127.0.0.1', database='pizzaria')
    cursor = cnx.cursor()
    cursor.execute("select id_ingre ID, nome_ingre Ingrediente, count(id) Conto from ingredientes left join montagem using(id_ingre) left join pizza using (id) group by Ingrediente order by Conto DESC, Ingrediente;")

    list = []
    for row in cursor:
        list.append(row)

    cursor.close()
    cnx.close()
    return list


for row in get_ingredients():
    print(row)