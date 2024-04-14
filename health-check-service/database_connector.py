import psycopg2


class Connector:

    def __init__(self, database:str,host:str="localhost", port:str="5432", password:str="password", user="root") -> None:
        try:
            self.conn=psycopg2.connect(host=host, user=user, password=password)
            cursor=self.conn.cursor()
            cursor.execute("create table if not exists health(node varchar(20) primary key, status bool not null)")
            
        except Exception as e:
            print(e)
            exit

    def insert(self,node:str,status:bool=False):

        cursor=self.conn.cursor()
        try:
            
            cursor.execute("insert into health (node,status) values (%s,%s)",(node,status))
            self.conn.commit()
            print("inserted")
        except Exception as e:
            self.conn.rollback()
            print(e)
    
    def get(self,node:str=None):
        cursor=self.conn.cursor()
        if node is not None:
            try:
                result=cursor.execute("select * from health").fetchall()
                return result
            except Exception as e:
                print(e)
                return None

        else:
            try:
                result=cursor.execute("select * from health where node=(%s)",(node,)).fetchall()
                return result
            except Exception as e:
                print(e)
                return None
            
            



        