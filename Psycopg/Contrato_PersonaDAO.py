from psycopg2.contrato_persona import contrato_persona
from psycopg2.cursorDelPool import CursorDelPool
from psycopg2.logger_base import log

class ContratoPersonaDAO:

    _SELECCIONAR= "SELECT * FROM contrato ORDER BY id"
    _INSERTAR = "INSERT INTO contrato(id_persona,id_contrato) VALUES (%s, %s)"
    

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contrato_persona = []
            for r in registros:
                contrato = contrato_persona(r[0],r[1])
                contrato.append(contrato)
            return contrato
    
    @classmethod
    def insertar(cls,contrato_persona):
        with CursorDelPool() as cursor:
            valores = (contrato_persona.id_persona,contrato_persona.id_contrato)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount