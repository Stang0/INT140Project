from components.GameMenu import GameMenu
import curses

class CharClass:
    def __init__(self):
        self._Warrior = """
                                                    Warrior                                              
                                                     *****                                                     
                                                      ***                                                      
                                                      ***                                                      
                                                      ***                                                      
                                                    *******                                                    
                                                 *************                                                 
                                                 **  *****  **                                                 
                                                 *** ***** ***                                                 
                                     *************** ***** ***************                                     
                                    ***************  *****  ***************                                    
                                    *******      *** ***** ***      *******                                    
                                    **** **********  *****  ********** ****                                    
                                    **** **         +**+**+         ** ****                                    
                                    **** **         ***+***         ** ****                                    
                                    **** **         ***+***         ** ****                                    
                                     *** ***        *** ***        *** ***                                     
                                     *******        *** ***        *******                                     
                                     **** **        *** ***        ** ****                                     
                                      *******       *** ***        ******                                      
                                      *******       ***+***       *******                                      
                                       *******     ****+****     *******                                       
                                       **** **     *********     ** ****                                       
                                        **** **    *********    ** ****                                        
                                         **** **   *********   ** ****                                         
                                         ***** *** ********* *** ****#                                         
                                          ****** ************** *****                                          
                                            *****  *********  *****                                            
                                             *********************                                             
                                               *****************                                               
                                                  * ******* *                                                  
                                                    *******                                                    
                                                     *****                                                     
                                                      ***                                                      
                                                      ***     
"""
        self._Mage = """                             Mage                               
                        24664                                   
                      369894                                    
                      48886                                     
                      48886        322                          
                      588896454445   665                        
                      6888888888894   6665                      
                      298889669888965  4994                     
                       49994  6888889   4994                    
                        99    688888899  495                    
                         49666988888888   64                    
                        4988888888888809  33                    
                       998888000 88888894                       
                     680888880 08888888892                      
                   56988888880008888888886                      
                   68888889080 000008888894                     
                   65698888  00086 698888863                    
                      59889 808894  9888894                     
                       4698800088  5988962                      
                         5690 8996690895                        
             4444444454    488  98966     6444444444            
         5469088888888964   644 445    2469888888889646         
    444680888888888888888969  55     569888888888888880894445   
  480888888889880888888888894  1   5698888888888966988888880965 
 4908  8880089  80808888888895    598888888888886  9000080  8006
 68888888888898880 999888888845   688888888888 8966988888880888 
16808896444444469888 98888889    2608888888888889644444449808992
   6442         246699 8888896     08888880896445          445  
                    46988888892   40888808965                   
                      569888886   688888894                     
                        49888896469880996                       
                         688888888888894                        
                         26988888889645                         
                           544444445                                                             
"""
        self._Ranger = """
                                                                      
                                Ranger                                 
                                ....                                  
                               ......                                 
                              ........                                
          ..                  .........                  ..           
         ......              ..........               .....           
         ........            .........:             .......           
         ..........          .. .......           .........           
         ...........            .....            ..........           
          ...........       .............       ...........           
          .........   ........................    ........            
           .. ........................................ ..             
               ......................................                 
             .............      .....     .............               
           ............         .....         ...........             
         ...............        .....        ..............           
       ..........  ......       .....       ...... ..........         
      .........     .....       .....      .....      ........        
     ........        .....      .....     ......        ........      
    .......           .....     .....    ......          ........     
  ........             .....    .....   ......             .......    
 .......                .....   .....  ......               .......   
 .......                ......  ..... ......                 ......   
       ....              ...... ...........              .....        
          ....            ................            ....            
             .....         ..............          ....               
                 ....       ............        ....                  
                    ....     ..........     .....                     
                       ....  ..........   ...                         
                            ............                              
                            ............                              
                             ..........                               
                              .... ....                               
                              ...  ...                                
                                                                           
                                                                                                                                                          
"""
        self._Rogue="""
                                        Rogue                 
                                       ............                   
                                       ......  ...                    
                                     ............                     
                                   ..............                     
                                 ........ ........                    
                    .............................                     
                     ....    ...... ........                          
                       ....     ..........                            
                     ........  .........                              
                   ..............   ...                            ...
                 .......... .....    ...                      ........
                .........     .....  ...                ..............
              .... ....     ........  ..             ....... .... ... 
            .... ....     ..............           .................. 
          .........      .........  ..:.         .... .....  .......  
        ..........     .... ....      .        .... ....     ......   
      ..........     .... ....               ..........     .......   
     .... ....     .... ....                .........     ....:...    
    ... ....     ..........               .... ....     .........     
   .......     ..........               .... ....     ..........      
   ......     .... ....               .... ....      .........        
  .......  ..... ....         ....  ..........     .........          
 .............:....           ..............     .... ....            
 ... .... .......             ............     .... ....              
..............                ...  .....     .........                
........                      ...    ..... ..........                 
...                            ...   ..............                   
                              .........  ........                     
                            ..........     ....                       
                          ...............    ....                     
                      ............................                    
                    ........ ........                                 
                     ..............                                   
                     ...... .....                                     
                    ...  .......                                      
                   ............                                                                                                                      
"""
        self._back="""
               [BACK]
            """
        self.current_selection = 0
        self._AllClass = {"1 - Warrior":self._Warrior,"2 - Mage":self._Mage,"3 - Ranger":self._Ranger,"4 - Rogue":self._Rogue,"0 - Back":self._back}
        self._Class = [
            "1 - Warrior",
            "2 - Mage",
            "3 - Ranger",
            "4 - Rogue",
            "0 - Back"
    ]
        self._ClassStatus = {
          "1 - Warrior": "STR:10,DEX:5,INT:0",
          "2 - Mage": "STR:0,DEX:5,INT:10",
          "3 - Ranger": "STR:5,DEX:10,INT:5",
          "4 - Rogue": "STR:5,DEX:10,INT:0",
          "0 - Back": "",
        }

    def SelectClass(self,stdscr):
          while True:
            stdscr.clear()
            self.GetBorders(stdscr)
            self.draw_options(stdscr)
            self.draw_ascii_art(stdscr)
            self.draw_status(stdscr)
            stdscr.refresh()

            key = stdscr.getch()
            if key == curses.KEY_UP:
                self.current_selection = (self.current_selection - 1) % len(self._Class)
            elif key == curses.KEY_DOWN:
                self.current_selection = (self.current_selection + 1) % len(self._Class)
            elif key in [10, 13]:
                if self._Class[self.current_selection] == "0 - Back":
                  break
                status = self._ClassStatus[self._Class[self.current_selection]]
                SplitStatus = status.split(",")
                return self._Class[self.current_selection] , SplitStatus
                
    def GetBorders(self, stdscr):
        height, width = stdscr.getmaxyx()
        top_border = "+" + "-" * (width - 2) + "+"
        bottom_border = "+" + "-" * (width - 2) + "+"
        stdscr.addstr(0, 0, top_border)
        stdscr.addstr(height - len(self._AllClass) - 5, 0, bottom_border)
    def draw_options(self, stdscr):
        height, width = stdscr.getmaxyx()
        option_y = height - len(self._AllClass) - 3
        for i, option in enumerate(self._AllClass):
            x = width // 2 - len(option) // 2
            y = option_y + i
            if i == self.current_selection:
                stdscr.addstr(y, x, option, curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, option)
    def draw_ascii_art(self, stdscr):
        height, width = stdscr.getmaxyx()
        current_option = self._Class[self.current_selection]
        ascii_art = self._AllClass[current_option]
        art_lines = ascii_art.strip().split("\n")
        art_y = (height // 2) - (len(art_lines) // 2)
        art_x = (width // 2) - (max(len(line) for line in art_lines) // 2)
        for i, line in enumerate(art_lines):
            if 0 <= art_y + i < height - 1:
                stdscr.addstr(art_y + i, art_x, line)
    def draw_status(self, stdscr):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)   
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  
        curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
        STRColor = curses.color_pair(1)
        DEXColor = curses.color_pair(2)
        INTColor = curses.color_pair(3)
        height, width = stdscr.getmaxyx()
        current_option = self._Class[self.current_selection]
        status = self._ClassStatus[current_option]
        if status:
            MenuHeight = height - len(self._AllClass) - 3  
            status_x = width // 2 - len(status) // 2
            SplitStatus = status.split(",")
            offset = 0 
            for Status in SplitStatus:
              key, value = Status.split(":")
              if key == "STR":
                  color = STRColor 
              elif key == "DEX":
                  color = DEXColor
              elif key == "INT":
                  color = INTColor
              else:
                  color = curses.A_NORMAL 
              stdscr.addstr(MenuHeight+5,status_x + offset, f"{key}: ", color)
              offset += len(f"{key}: ")
              stdscr.addstr(MenuHeight+5,status_x + offset, f"{value}", curses.A_BOLD)
              offset += len(f"{value}, ") 