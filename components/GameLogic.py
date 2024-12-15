import curses
import random

class BattleSystem:
    def __init__(self,Class,status):
        status_dict = {key.strip(): int(value.strip()) for key, value in (item.split(":") for item in status)}
        self.status = status_dict
        if Class == '1 - Warrior':
            self.player = {
                "class": Class,
                "HP": 120,
                "SP": 100,
                "Status": self.status,
                "ATK": (7, 8),
                "skills": [
                    {"name": "Slash", "sp_cost": 0, "desc": "50% STR", "damage": lambda ATK: ATK * 0.5},
                    {"name": "Power Strike", "sp_cost": 10, "desc": "ATK * STRStatus", "damage": lambda STR: STR * self.status["STR"]},
                ],
            }
        elif Class == '2 - Mage':
            self.player = {
                "class": Class,
                "HP": 80,
                "SP": 100,
                "Status": self.status,
                "ATK": (15, 18),
                "skills": [
                    {"name": "Basic Magic", "sp_cost": 0, "desc": "50% ATK", "damage": lambda ATK: ATK * 0.5},
                    {"name": "Super Magic", "sp_cost": 30, "desc": "500% INT", "damage": lambda ATK: self.status["INT"] * 50},
                ],
            }
        elif Class == '3 - Ranger':
            self.player = {
                "class": Class,
                "HP": 100,
                "SP": 100,
                "Status": self.status,
                "ATK": (4, 8),
                "skills": [
                    {"name": "Wind Arrow", "sp_cost": 0, "desc": "50% ATK", "damage": lambda ATK: ATK * 0.5},
                    {"name": "Magic Arrow", "sp_cost": 15, "desc": "INT * DEX", "damage": lambda ATK: int(self.status["INT"]) * int(self.status["DEX"]) },
                ],
            }
        elif Class == '4 - Rogue':
            self.player = {
                "class": Class,
                "HP": 110,
                "SP": 100,
                "Status": self.status,
                "ATK": (5, 10),
                "skills": [
                    {"name": "Knife", "sp_cost": 0, "desc": "50% ATK", "damage": lambda ATK: ATK * 0.5},
                    {"name": "Flying knife", "sp_cost": 5, "desc": "Dex * 2 ", "damage":lambda ATK:   int(self.status["DEX"])* 2},
                ],
            }
        self.enemy = ''
        self.current_selection = 0
        self.log = []  
    def game_loop(self, stdscr):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)   
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)    

   
        enemies = [
            {"name": "Blue Slime", "HP": 50, "ATK": (5, 10)},
            {"name": "Goblin", "HP": 80, "ATK": (8, 12)},
            {"name": "Boss Dragon", "HP": 150, "ATK": (20, 30)},

        ]
        
        for i, enemy in enumerate(enemies):  
            self.enemy = enemy
            self.log = [f"A wild {self.enemy['name']} appears!"]
            
       
            self.battle_menu(stdscr)

        
            if self.player["HP"] <= 0:
                break
         
            if i < len(enemies) - 1:  
                self.log.append(f"You defeat the {enemy['name']}! Prepare for the next battle.")
            else:  
                self.log.append(f"You defeat the {enemy['name']}! You have completed the game!")

            stdscr.clear()
            self.draw_ui(stdscr)
            self.draw_log(stdscr)
            stdscr.addstr(10, 4, "Press any key to continue.", curses.color_pair(1) | curses.A_BOLD)
            stdscr.refresh()
            stdscr.getch()

     
        stdscr.clear()
        self.draw_ui(stdscr)
        self.draw_log(stdscr)
        if self.player["HP"] > 0:
            stdscr.addstr(10, 4, "Congratulations! You completed the game!", curses.color_pair(1) | curses.A_BOLD)
        else:
            stdscr.addstr(10, 4, "Game Over! Better luck next time.", curses.color_pair(3) | curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch()
    def battle_menu(self, stdscr):
        
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)   
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)   

        while True:
            stdscr.clear()
            self.draw_ui(stdscr)
            self.draw_log(stdscr)
            stdscr.refresh()

            key = stdscr.getch()

           
            if key == curses.KEY_UP:
                self.current_selection = (self.current_selection - 1) % len(self.player["skills"])
            elif key == curses.KEY_DOWN:
                self.current_selection = (self.current_selection + 1) % len(self.player["skills"])
            elif key in [10, 13]:  
                self.player_turn(self.player["skills"][self.current_selection])
                if self.enemy["HP"] <= 0:  
                    self.log.append(f"You defeated the {self.enemy['name']}!")
                    break

                self.enemy_turn()
                if self.player["HP"] <= 0: 
                    self.log.append("You were defeated!")
                    break


        stdscr.clear()
        self.draw_ui(stdscr)
        self.draw_log(stdscr)
        if self.player["HP"] > 0:
            stdscr.addstr(10, 4, "You Win! Press any key to exit.", curses.color_pair(1) | curses.A_BOLD)
        else:
            stdscr.addstr(10, 4, "Game Over! Press any key to exit.", curses.color_pair(3) | curses.A_BOLD)
        stdscr.refresh()
        stdscr.getch() 

    def draw_ui(self, stdscr):
        height, width = stdscr.getmaxyx()

   
        stdscr.addstr(2, 2, "PLAYER", curses.A_BOLD)
        stdscr.addstr(3, 2, f"HP: {self.player['HP']} / SP: {self.player['SP']}", curses.color_pair(1))

        stdscr.addstr(2, width // 2, f"ENEMY: {self.enemy['name']}", curses.A_BOLD)
        stdscr.addstr(3, width // 2, f"HP: {self.enemy['HP']}", curses.color_pair(1))
        stdscr.addstr(4, width // 2, f"ATK: {self.enemy['ATK'][0]} - {self.enemy['ATK'][1]}")

        menu_y = 6
        stdscr.addstr(menu_y, 2, "Choose your action:", curses.A_BOLD)
        for i, skill in enumerate(self.player["skills"]):
            option_text = f"[{i + 1}] {skill['name']} - {skill['desc']} (SP: {skill['sp_cost']})"
            if i == self.current_selection:
                stdscr.addstr(menu_y + i + 1, 4, option_text, curses.A_REVERSE)
            else:
                stdscr.addstr(menu_y + i + 1, 4, option_text)
    def draw_log(self, stdscr):
        height, width = stdscr.getmaxyx()
        log_y = height - 8
        stdscr.addstr(log_y, 2, "Battle Log:", curses.A_BOLD)
        for i, log in enumerate(self.log[-5:]): 
            stdscr.addstr(log_y + i + 1, 4, log)

    def player_turn(self, skill):
        if self.player["SP"] >= skill["sp_cost"]:
            self.player["SP"] -= skill["sp_cost"]
            damage = int(skill["damage"](random.randint(*self.player["ATK"])))
            self.enemy["HP"] -= damage
            self.log.append(f"You used {skill['name']}! It dealt {damage} damage!")
        else:
            self.log.append(f"Not enough SP to use {skill['name']}!")
    def enemy_turn(self):
        damage = random.randint(*self.enemy["ATK"])
        self.player["HP"] -= damage
        self.log.append(f"The {self.enemy['name']} attack  {damage} damage!")
