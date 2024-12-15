#037
#049
#052
#063
#066
import curses
import pygame
from threading import Thread
from curses import wrapper
from components.GameMenu import GameMenu
from SelectClass import SelectClass

def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("BG_music.mp3")  
    pygame.mixer.music.play(-1)


def main(stdscr):
    menu =  GameMenu()

    stdscr.clear()
    menu.GetGameLogo(stdscr)
    selected_option = menu.GetGameMenu(stdscr,['StartGame','Exit'])
    if selected_option == 0:
        stdscr.clear()
        curses.wrapper(SelectClass)
        stdscr.refresh()
    elif selected_option == 1:
        exit()
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    music_thread = Thread(target=play_music, daemon=True)
    music_thread.start()


    curses.wrapper(main)