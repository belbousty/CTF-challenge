import os
import random


def get_random_mission_from_file(file_path):
    with open(file_path, 'r') as mission_file:
        missions = mission_file.readlines()
    return random.choice(missions).strip()

def main():
    mission_file_path = "/var/mission/missions.txt"
    mission = get_random_mission_from_file(mission_file_path)

    print("Hello Mr 007, with the current ids :\n")
    os.system('id')
    print("Check your Mission at home")
    mission_update_command = f"echo 'Your mission, Agent007, should you choose/decide to accept it, is to {mission}' > /home/agent007/Mission"
    os.system(mission_update_command)

    disclaimer = "As always, should you or any of your task force be caught or killed, the Secretary will disavow any knowledge of your actions. This tape/disc will self-destruct in five/ten seconds.\nGood luck,\nAgent007."
    disclaimer_command = f"echo '{disclaimer}' >> /home/agent007/Mission"
    os.system(disclaimer_command)

if __name__ == "__main__":
    main()
