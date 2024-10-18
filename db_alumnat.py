from client import db_client

def read():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from Alumne")
    
        alumnes = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumnes

def read_id(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "select * from Alumne WHERE idAlumne = %s"
        value = (id,)
        cur.execute(query,value)
    
        alumne = cur.fetchone()

    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumne

def create(idAula,nomAlumne,cicle,curs,grup):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "insert into Alumne (idAula,nomAlumne,cicle,curs,grup) VALUES (%s,%s,%s,%s,%s);"
        values=(idAula,nomAlumne,cicle,curs,grup)
        cur.execute(query,values)
    
        conn.commit()
        alumne_id = cur.lastrowid
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return alumne_id

def update_alumne(id,col):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "update Alumne SET cicle = %s WHERE idAlumne = %s;"
        values=(col,id)
        cur.execute(query,values)
        updated_recs = cur.rowcount
    
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()

    return updated_recs

def delete_alumnat(id):
    try:
        conn = db_client()
        cur = conn.cursor()
        query = "DELETE FROM Alumne WHERE IdAlumne = %s;"
        cur.execute(query,(id,))
        deleted_recs = cur.rowcount
        conn.commit()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
        
    return deleted_recs

def readAll():
    try:
        conn = db_client()
        cur = conn.cursor()
        cur.execute("select * from Alumne INNER JOIN Aula ON Alumne.IdAula = Aula.IdAula;")
    
        alumnes = cur.fetchall()
    
    except Exception as e:
        return {"status": -1, "message": f"Error de connexió:{e}" }
    
    finally:
        conn.close()
    
    return alumnes