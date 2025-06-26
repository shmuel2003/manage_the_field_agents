import mysql.connector
from models.agent import Agent

class AgentDAL:
    def __init__(self, host='localhost', user='root', password='', database='eagleEyeDB'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)

    def add_agent(self, agent: Agent):
        query = """
        INSERT INTO agents (codeName, realName, location, status, missionsCompleted)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (agent.code_name, agent.real_name, agent.location, agent.status, agent.missions_completed)
        self.cursor.execute(query, values)
        self.conn.commit()

    def get_all_agents(self):
        self.cursor.execute("SELECT * FROM agents")
        results = self.cursor.fetchall()
        return [Agent(**row) for row in results]

    def get_agent_by_id(self, agent_id):
        self.cursor.execute("SELECT * FROM agents WHERE id = %s", (agent_id,))
        row = self.cursor.fetchone()
        return Agent(**row) if row else None

    def update_agent(self, agent: Agent):
        query = """
        UPDATE agents SET codeName=%s, realName=%s, location=%s, status=%s, missionsCompleted=%s
        WHERE id=%s
        """
        values = (agent.code_name, agent.real_name, agent.location, agent.status, agent.missions_completed, agent.id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_agent(self, agent_id):
        self.cursor.execute("DELETE FROM agents WHERE id = %s", (agent_id,))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()