import unittest
from unittest.mock import patch
from GameLogic import BattleSystem
import random

class TestBattleSystem(unittest.TestCase):

    def setUp(self):
        
        self.status = ["STR:10", "DEX:8", "INT:5"]
        self.warrior = BattleSystem('1 - Warrior', self.status)
        self.mage = BattleSystem('2 - Mage', self.status)
        self.ranger = BattleSystem('3 - Ranger', self.status)
        self.rogue = BattleSystem('4 - Rogue', self.status)
        self.enemy = {"name": "Test Enemy", "HP": 100, "ATK": (10, 20)}

    def test_status_initialization(self):
       
        expected_status = {"STR": 10, "DEX": 8, "INT": 5}
        self.assertEqual(self.warrior.status, expected_status)

    def test_warrior_skill_damage(self):
     
        self.warrior.enemy = self.enemy
        skill = self.warrior.player["skills"][1]  
        damage = skill["damage"](10)  
        self.assertEqual(damage, 100) 

    def test_mage_skill_damage(self):
       
        self.mage.enemy = self.enemy
        skill = self.mage.player["skills"][1]  
        damage = skill["damage"](5)  
        self.assertEqual(damage, 250)  

    def test_ranger_skill_damage(self):
        
        self.ranger.enemy = self.enemy
        skill = self.ranger.player["skills"][1] 
        damage = skill["damage"](4)   
        self.assertEqual(damage, 40)  

    def test_rogue_skill_damage(self):
        self.rogue.enemy = self.enemy
        skill = self.rogue.player["skills"][1]  
        damage = skill["damage"](4)   
        self.assertEqual(damage, 16)   

    @patch('random.randint', return_value=10)
    def test_player_turn(self, mock_randint):
        self.warrior.enemy = self.enemy
        skill = self.warrior.player["skills"][0]  
        self.warrior.player_turn(skill)
        self.assertEqual(self.enemy["HP"], 95)   

    @patch('random.randint', return_value=15)
    def test_enemy_turn(self, mock_randint):
        self.warrior.enemy = self.enemy
        self.warrior.enemy_turn()
        self.assertEqual(self.warrior.player["HP"], 105)  
if __name__ == "__main__":
    unittest.main()
