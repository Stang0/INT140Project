import curses
from components.GameLogic import BattleSystem
from components.ClassSelect import CharClass
def SelectClass(stdscr):
    menu = CharClass()
    Class,status = menu.SelectClass(stdscr)
    if Class == '1 - Warrior':
        stdscr.clear()
        BattleSystem(Class,status).game_loop(stdscr)
        stdscr.refresh()
    elif Class == '2 - Mage':
        stdscr.clear()
        BattleSystem(Class,status).game_loop(stdscr)
        stdscr.refresh()
    elif Class == '3 - Ranger':
        stdscr.clear()
        BattleSystem(Class,status).game_loop(stdscr)
        stdscr.refresh()
    elif Class == '4 - Rogue':
        stdscr.clear()
        BattleSystem(Class,status).game_loop(stdscr)
        stdscr.refresh()
    stdscr.refresh()


if __name__ == "__main__":
    curses.wrapper(SelectClass)
