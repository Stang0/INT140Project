import curses
class GameMenu:
    def __init__(self):
        self._GameLogo = """
                                                                                                j                                                     
                                                                                                f      f                                              
                                                                                                ff     jf                                              
                                                                                                ffj    ff                                               
                                                                                                jff  rfff    jffffffffffffj                              
                                                                                                ffff tfff  ffffffff                                        
                                                                                            ffjj fff rfffffjj      tjfjffffjfjfffft                     
                                                                                            ffff tjfj ffffffff  jffffffffffffffffffffffff                 
                                                                                        ffffjf ffj jffffffffffffffffffffft               f              
                                                                                        ffffjfffffjfffjfffffffffffffffffjffffffffffffft                  
                                                                                        ffffjffffffffffjffffffffffffffffffffffffffffffffffffjt            
                                                                                    rfffffffffffffff ffffffffffffffffffffffffffffffffffffffffff         
                                                                                    fffffffffffffffffffff      ffffffffffffffffffffffff     ffffff      
                                                                                    jffffffffffffffffffffff          ffffffffffffffffjjjfj        fff    
                                                                                    fffffffffffffffffffffffffjfffffffj fffffffffffffffffff           fj  
                                                                                    jfffffffffffffffffffffffffffffjf        fffjffffffffffffffft         f 
                                                                                    fffffffffffjffffffffffffffjft             jfffffffffffffffffff         
                                                                                    fffffjfjfffffffffffffffffffffffffffff      fffffffffffffffffffj       
                                                                                    rfffff  jffffffffffffffffffj  ffjffjffff    fffffffffffffffffffff     
                                                                                    ffffjfjfffjfffffffffffffffff    fffffffjff   fffffffffjffjff fffff    
                                                                                jfffffffffffffffffffffjf     ffj   tffffff jf  ffffffffffffftfj  jffft  
                                                                                fffffffffffffffffffffjfjf             ffffff  f  ffjjfffffffffj     fff  
                                                                                jfffffffffffftffffffff               f  jfffff   f jf ffffffffffff     fff 
                                                                            jffffffffff ffffffft                  j  ffffff     ff ffffffffffffft    ffj
                                                                            jfffffffffffj jfffff                     fffffffff     j  jffffffffffffff    ff
                                                                            ffffffffffffffffff                       ffffffffr     f ffffffffffffffff    jf
                                                                            ffffffffff fffff                   fj  ffffffff f      ffjffffffffffffff    f
                                                                            fffjffffffff rfjf               ff   fffffff  ff     j  fffffffffffffffj   f
                                                                                jffffff                   ffff fffffff  ff        ffffffffffff ffff   j
                                                                                ffffff                fffffffffff   fff        fffffffffffff  fff    
                                                                                    f                  fffffffffj    tfff        ffffffffffffffj fff    
                                                                                                    ffffffffff   fffff        fffffffffffffffff  fff   
                                                                                                    fffffffff  fjffff    fjfjfjffffffjffffffffff   fr   
                                                                                                    fffffffj fffffjf        fffffffffjjffr ffffff   f    
                                                                                                    tffffffftffffj    jjfjfffffffffffffff   jffff    f    
                                                                                                    ffjffff ffff           ffffffffj ffj    fffff   ff    
                                                                                                    jjffjf fff            fffffffj  jff    fffffr   j     
                                                                                                    jffff fff         ffffffff   fff      fffff   r      
                                                                                                    jfftffjffff  tffffjf     jfff      j fffff           
                                                                                                    ffffffffffj                      fj jffff            
                                                                                                    fffffffffff                    ff  ffff              
                                                                                                    f ffffjjfffff              fff   ffff               
                                                                                                        ffffffjf ffffjff   ffffff   ffff                 
                                                                                                        ffffffffffffffffffff    ffj                    
                                                                                                            jfffffjjffff      ffj                     
"""
        
        self.current_selection = 0

    def GetGameLogo(self,stdscr)->str:
        stdscr.addstr(0,0,self._GameLogo)
    def GetGameMenu(self,stdscr,Menu):
        Menu = Menu
        height, width = stdscr.getmaxyx()
        Menu_y = height - len(Menu) - 2
        Menu_x = width / 2 

        while True:
            for i, menu_item in enumerate(Menu):
                if i == self.current_selection:
                    stdscr.addstr(Menu_y + i, int(Menu_x - len(menu_item) // 2), menu_item, curses.A_REVERSE)
                else:
                    stdscr.addstr(Menu_y + i,int( Menu_x - len(menu_item) // 2), menu_item)

            stdscr.refresh()

            key = stdscr.getch()

            if key == curses.KEY_UP:
                if self.current_selection < 1:
                    self.current_selection = (self.current_selection + 1) 
                self.current_selection = (self.current_selection - 1) 
            elif key == curses.KEY_DOWN:
                if self.current_selection > len(Menu)-2:
                    self.current_selection = (self.current_selection - 1) 
                self.current_selection = (self.current_selection + 1) 
            elif key == curses.KEY_ENTER or key in [10, 13]:  
                return self.current_selection