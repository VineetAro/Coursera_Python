"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # List to remove all Zeros and adding the cells 
    lst_1 = []
    
    # List to Move added cells to the left and adding missing Zeors
    lst_2 = []
        
    # Create a list without zeros "lst_1"
    for dummy_l in line:
        if dummy_l != 0:
            lst_1.append(dummy_l)
            
    # update lst_1 by adding the matching cells pairs if there value is same.
    for dummy_ran in range(0,len(lst_1)-1):
        if  len(lst_1)-1 >= 1:
            if lst_1[dummy_ran] == lst_1[dummy_ran+1]:
                lst_1[dummy_ran] = lst_1[dummy_ran]*2
                lst_1[dummy_ran+1] = 0
    # create a new list "lst_2" to remove all zeros and move the value to the left.
    for dummy_lst in lst_1:
        if dummy_lst != 0:
            lst_2.append(dummy_lst)
    
    # add missing zeros in lst_2
    while len(lst_2)<len(line):
        lst_2.append(0)
    
    return lst_2


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.height = grid_height
        self.width = grid_width
       
        key_up = [(0,col) for col in range(grid_width)]
        key_down = [(grid_height-1,col) for col in range(grid_width)]
        key_left = [(row,0) for row in range(grid_height)]
        key_right = [(row, (grid_width-1)) for row in range(grid_height)]
        self.dict_indices = {UP:key_up,
                            DOWN:key_down,
                            RIGHT: key_right,
                            LEFT: key_left} 
        
        self.reset()
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.grid = [[0 for col in range(self.width)]
                      for row in range(self.height)]
             
        self.new_tile()
        self.new_tile()            

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        out = ''
        for row in self.grid:
            for entry in row:
                out += str(entry) + '\t'
            out += '\n'
        return out

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        temp_list = []
        change=0
                   
        move_direction = OFFSETS[direction]
        start_indices = list(self.dict_indices[direction])
        
        if direction == UP or direction == DOWN:
            num_steps = self.height            
        else:
            num_steps = self.width 
   
        
        for tile in self.dict_indices[direction]:
            for step in range(num_steps):
                row = tile[0] + step * move_direction[0]
                col = tile[1]+ step * move_direction[1]
                temp_list.append(self.grid[row][col])
                m_t_lst = merge(temp_list)
            temp_list = []
           
        
            for step in range(num_steps):
                row = tile[0] + step * move_direction[0]
                col = tile[1]+ step * move_direction[1]
                if self.grid[row][col] != m_t_lst[step]:
                    self.grid[row][col] = m_t_lst[step]
                    change += 1
                
        if change >0:
            self.new_tile()
        
        
            
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # rand_row gives a random row 
        # rand_col gives a random col 
        # rand_num generates a random number 90 % it generates 2
        rand_row = random.randrange((self.height))
        rand_col = random.randrange((self.width))
        rand_num = random.choice([2] * 90 + [4] * 10)
      
        
        """Iterate throught the list to find if atleast one square with value zero 
        exists. 
        if 0 exists in num 
        for element in self.grid: element = [0,0,0], [0,0,2]
            for num in element: [0,0,0]
                num = 0
               
        """
        if 0 in [num for elem in self.grid for num in elem]:
            if self.get_tile(rand_row, rand_col) == 0:
                self.set_tile(rand_row, rand_col, rand_num)
            else:
                self.new_tile()
        else:
            pass
     

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
            
        return self.grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

                
                
                
