import psycopg2
import datetime 
import  Settings
class Connector:

    def __init__(self) -> None:
        try:
            self.conn=psycopg2.connect(
                host=Settings.DATABASES['default']['HOST'], 
                port=Settings.DATABASES['default']['PORT'],
                user=Settings.DATABASES['default']['USER'],
                password=Settings.DATABASES['default']['PASSWORD'],
                dbname=Settings.DATABASES['default']['NAME']
            )
            
        except Exception as e:
            print(e)
            exit

    def upsert(self,node_id:int,node_name:str,checkpoint:datetime):
        cursor=self.conn.cursor()
        try:
            cursor.execute("insert into  nodedetails(id,node_name,checkpoint) values (%s,%s,%s) on conflict(id,node_name) do update set checkpoint=%s",(node_id,node_name,checkpoint,checkpoint))
            print("UPSERTED NODE STATUS ")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)

    def insert(self,node:str,checkpoint:datetime):
        cursor=self.conn.cursor()
        try:
            cursor.execute("insert into  NodeDetails(node_name,checkpoint) values (%s,%s)",(node,checkpoint))
            print("INSERTED NODE STATUS ")
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
    def get(self,node:str=None):
        cursor=self.conn.cursor()
        if node is not None:
            try:
                result=cursor.execute("select * from NodeDetails").fetchall()
                return result
            except Exception as e:
                print(e)
                return None

        else:
            try:
                result=cursor.execute("select * from NodeDetails where node=(%s)",(node,)).fetchall()
                return result
            except Exception as e:
                print(e)
                return None
            
            



        