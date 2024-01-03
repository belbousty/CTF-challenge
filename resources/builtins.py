import sys
import random

def generate_tools():
    w = []
    with open('weapons.txt', 'r') as weapon_file:
        weapons = weapon_file.readlines()
    for i in range(0, 5):
        n = random.randint(0, 100)
        w.append(weapons[n].strip())
    return w

def prompt():
    print("---> In case you need Help agent, enter 'help'")
    while True:
        MyInput = raw_input('>>> ')
        if MyInput == "help":
            print('[+] GET [agent_name] : get details of tools and weapons you can use for the mission')
            print('[+] QUIT: exit and destroy this prompt')
        elif MyInput == "QUIT":
            sys.exit()
        elif MyInput == "GET":
            tools = generate_tools()
            print("Agent, your weapons for this mission are :")
            for i in range(0, len(tools)):
                print("    - {}".format(tools[i]))
        else:
            try:
                exec(MyInput)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    prompt()
