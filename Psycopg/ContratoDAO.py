from psycopg2.contrato import contrato
from psycopg2.cursorDelPool import CursorDelPool
from psycopg2.logger_base import log

class ContratoDAO:

    _SELECCIONAR= "SELECT * FROM contrato ORDER BY id"
    _INSERTAR = "INSERT INTO contrato(no.contrato,costo,fechaini,fechafin) VALUES (%s, %s, %s)"
    _ACTUALIZAR = "UPDATE contrato SET no.contrato = %s, costo =%s, fechaini =%s,fechafin =%s WHERE id = %s"
    _ELIMINAR = "DELETE FROM contrato WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato = contrato(r[0],r[1],r[2],r[3],r[4])
                contratos.append(contrato)
            return contrato
    
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.no.contrato, contrato.costo ,contrato.fechaini,contrato.fechafin)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.no.contrato, contrato.costo ,contrato.fechaini,contrato.fechafin,  contrato.id)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,contrato):
        with CursorDelPool as cursor:
            valores = (contrato.id,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        