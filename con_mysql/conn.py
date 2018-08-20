# A Biblioteca abaixo é fundamental para que a conexão possa ser feita com o Banco de Dados do MySQL
# Próximo passo conectar com o servidor remoto, e não um servidor local. SERA?
import mysql.connector


def get_ingredients():
    # Alterado o password por motivos claros
    cnx = mysql.connector.connect(user='root', password='mangaverde', host='127.0.0.1', database='pizzaria')
    cursor = cnx.cursor()
    cursor.execute("select id_ingre ID, nome_ingre Ingrediente, count(id) Conto from ingredientes left join montagem using(id_ingre) left join pizza using (id) group by Ingrediente order by Ingrediente;")

    list = []
    for row in cursor:
        list.append(row)

    cursor.close()
    cnx.close()
    return list


def get_specific_pizzaria(nome_pizzaria):
    cnx = mysql.connector.connect(user='root', password='mangaverde', host='127.0.0.1', database='pizzaria')
    result = cnx.cursor()
    result.execute("select * from estabelecimento where estabelecimento.nome_pizzaria like \"%" + str(nome_pizzaria) + "%\";")
    list = []
    for row in result:
        list.append(row)

    result.close()
    cnx.close()
    print(list[0][0])
    return list[0][0]


def get_specific_pizza(nome_pizza, id_pizzaria):
    cnx = mysql.connector.connect(user='root', password='mangaverde', host='127.0.0.1', database='pizzaria')
    result = cnx.cursor()
    result.execute(
        "select * from pizza where pizza.nome_pizza like \"%" + str(nome_pizza) + "%\" and pizza.id_pizzaria = " + str(id_pizzaria) + ";")
    list = []
    for row in result:
        list.append(row)

    result.close()
    cnx.close()
    print(list[0][0])
    return list[0][0]


def create_new_pizzaria(nome_pizzaria, change_string):
    cnx = mysql.connector.connect(user='root', password='mangaverde', host='127.0.0.1', database='pizzaria')
    result = cnx.cursor()
    result.execute("INSERT INTO estabelecimento (nome_pizzaria) VALUES (\"" + nome_pizzaria + "\");")
    cnx.commit()
    result.close()
    cnx.close()
    change_string.set(str(get_specific_pizzaria(nome_pizzaria)))


def create_new_pizza(nome_pizza, tipo_pizza, tamanho_pizza, preco_pizza, tempo_pizza, id_pizzaria, cha):
    cnx = mysql.connector.connect(user='root', password='mangaverde', host='127.0.0.1', database='pizzaria')
    result = cnx.cursor()
    result.execute("INSERT INTO pizza (nome_pizza, tipo, tamanho, preco, tempo, id_pizzaria) values" 
                   "(\"" + nome_pizza + "\", \"" + tipo_pizza + "\", \"" + tamanho_pizza + "\", " +
                   str(preco_pizza) + ", " + str(tempo_pizza) + ", " + str(id_pizzaria) + ");")
    cnx.commit()
    result.close()
    cnx.close()
    cha.set(str(get_specific_pizza(nome_pizza, id_pizzaria)))


def insert_montagem(string_pizza):
    cnx = mysql.connector.connect(user='root', password='mangaverde', host='127.0.0.1', database='pizzaria')
    result = cnx.cursor()
    result.execute(string_pizza.get()[:-2] + ";")
    cnx.commit()
    result.close()
    cnx.close()

