from dal.agent_dal import AgentDAL
from models.agent import Agent

def print_menu():
    print("\n--- Eagle Eye Agent Management ---")
    print("1. Add Agent")
    print("2. View All Agents")
    print("3. View Agent by ID")
    print("4. Update Agent")
    print("5. Delete Agent")
    print("6. Exit")

def main():
    dal = AgentDAL()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            code_name = input("Code Name: ")
            real_name = input("Real Name: ")
            location = input("Location: ")
            status = input("Status (Active/Injured/Missing/Retired): ")
            missions = int(input("Missions Completed: "))
            agent = Agent(code_name, real_name, location, status, missions)
            dal.add_agent(agent)
            print("Agent added successfully.")

        elif choice == '2':
            agents = dal.get_all_agents()
            for agent in agents:
                print(agent)

        elif choice == '3':
            agent_id = int(input("Enter Agent ID: "))
            agent = dal.get_agent_by_id(agent_id)
            print(agent if agent else "Agent not found.")

        elif choice == '4':
            agent_id = int(input("Enter Agent ID to update: "))
            agent = dal.get_agent_by_id(agent_id)
            if agent:
                print("Current info:", agent)
                agent.code_name = input("New Code Name: ")
                agent.real_name = input("New Real Name: ")
                agent.location = input("New Location: ")
                agent.status = input("New Status: ")
                agent.missions_completed = int(input("New Missions Completed: "))
                dal.update_agent(agent)
                print("Agent updated.")
            else:
                print("Agent not found.")

        elif choice == '5':
            agent_id = int(input("Enter Agent ID to delete: "))
            dal.delete_agent(agent_id)
            print("Agent deleted.")

        elif choice == '6':
            dal.close()
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()