from neo4j import Hospital

class Database(object):

#driver de la base de datos
#referencia de neo4j
	def __init__(self,uri,user,password):
		self._driver=Hospital.driver(uri,auth=(user,password))

#se cierra la base de datos Hospital
#referencia de neo4j
	def close(self):
		self._driver.close()
#referencia de neo4j
	def print_greeting(self,message):
		with self._driver.session.write_transaction(self,_create_and_return_greeting,message)
  #referencia de neo4j 
    @static method
    def _create_and_return_greeting(tx,message):
    	result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]	
        