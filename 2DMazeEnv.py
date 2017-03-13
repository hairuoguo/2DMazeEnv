import numpy as np
import sys
from six import StringIO, b

from gym import utils
from gym.envs.toy_text import discrete

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

#random map environment with start and goal
#start in upper left corner, goal in lower right

class Maze():
    
    class State():
        def __init__(self, coordinates, up, down, left, right, is_start=False, is_goal=False):
            self._coordinates = coordinates
            self._up = up
            self._down = down
            self._left = left
            self._right = right
            self._is_start = is_start
            self._is_goal = is_goal

        def _get_coordinates(self):
            return self._coordinates

        def _get_up(self):
            return self._up
        
        def _get_down(self):
            return self._down

        def _get_left(self):
            return self._left

        def _get_right(self):
            return self._right

    def __init__(self, map_rows, map_cols, colors, text_directions, is_test):
        self._is_test = is_test
        self._map_rows = map_rows
        self._map_cols = map_cols
        self._text_directions = text_directions
        self._states = []
        self._colors_to_directions = 
        for row, col in xrange(self._map_rows), xrange(self._map_cols):
         
        
        #create maze, hae directions based on whether test or not
         


class 2DMazeEnv(discrete.DiscreteEnv):

    #incur penalty for every action that is taken.

    def __init__(self, desc=None, map_rows=10, map_cols=10, num_colors=4, text_directions=['left', 'right']):
    
        

    def _render(self, mode='human', close=False, is_test=False):

    def _get_obs() 
