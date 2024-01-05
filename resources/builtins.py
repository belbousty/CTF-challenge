from sys import modules
import random

# clearing modules

modules.clear()
del modules
_True = True
_raw_input = raw_input
_BaseException = BaseException

__builtins__.__dict__.clear()
__builtins__ = None


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
    while _True:
        MyInput = _raw_input('>>> ')
        MyInput = MyInput.split()[0][:40]
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
                d = {'re': None}
                exec  're='+MyInput in d
                print  d['re']
            except _BaseException as e:
                print(e)

if __name__ == '__main__':
    prompt()
