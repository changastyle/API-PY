def limpiarDictAlchemy(obj):
    dictNvo = {}

    if obj == None:
        return {}

    elif type(obj) == list:

        diccionario = []
        for objLoop in obj:
            diccionario.append(limpiezaProfunda(objLoop.__dict__))
            # diccionario = [o.__dict__ for o in obj]

    else:
        # SOY UN OBJETO COMUN:
        diccionario = obj.__dict__

        dictNvo = limpiezaProfunda(diccionario)


    return dictNvo

def limpiezaProfunda(diccionario):
    dictNvo = {}
    for key in diccionario:
        valor = diccionario[key]
        print(key, "->", valor)

        if key != "_sa_instance_state":
            dictNvo[key]=valor
    return dictNvo
# aleatorio = int(random.random() * 1000)
# email = "nico.grossi" + str(aleatorio) + "@gmail.com"
# operadorNVO = Operador("Nicolas", "1234", email)
#
# mysqlPass = os.getenv("MYSQL-PASS")
# SCHEMA="clinicapp-py"
# DATABASE_URL = f"mysql+pymysql://root:{mysqlPass}@localhost/{SCHEMA}?charset=utf8mb4"
#
# engine = create_engine(DATABASE_URL)
#
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# session = SessionLocal()
#
# session.add(operadorNVO)
# session.flush()
# session.commit()
#
# session.refresh(operadorNVO)
#
# diccionario = operadorNVO.__dict__
# print("Diccionario:" + str(operadorNVO))
# diccionarioNvo = limpiarDictAlchemy(diccionario)
# print("diccionarioNvo:" + str(diccionarioNvo))
# for key in diccionario:
#     print(key, "->", diccionario[key])
# print("Operador Nvo:" + str(operadorNVO.__dict__))

