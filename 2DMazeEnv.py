import numpy as np
import sys
from six import StringIO, b

from gym import utils
from gym.envs.toy_text import discrete

LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

BLACK = "black"
WHITE = "white"
RED = "red"
BLUE = "blue"

#random map environment with start and goal
#start in upper left corner, goal is final state of longest path

class Maze():
    
    class State():
        def __init__(self, is_visited=False, is_start=False, is_goal=False):
            
            self._up_color = BLACK
            self._down_color = BLACK
            self._left_color = BLACK
            self._right_color = BLACK
            self._is_visited = is_visited
            self._is_start = is_start
            self._is_goal = is_goal
            


        def get_up_color(self): 
            return self._up_color
        
        def get_down_color(self):
            return self._down_color

        def get_left_color(self):
            return self._left_color

        def get_right_color(self):
            return self._right_color
    
        def set_up_color(self, color):
            self._up_color = color
        
        def set_down_color(self, color):
            self._down_color = color

        def set_left_color(self, color):
            self._left_color = color
    
        def set_right_color(self, color):
            self._right_color = color

        def get_is_visited(self):
            return self._is_visited



    def __init__(self, num_rows, num_cols, colors, text_directions, is_test):
        self._is_test = is_test
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._text_directions = text_directions
        self._states = [State() for n in xrange(num_rows*num_cols)] 
        self._colors_to_directions = 
        self._transitions = [[n]*4 for n in xrange(num_cols*num_rows)]
        #generate maze using depth-first search algorithm
        #generate maze and path from start to finish using depth-first search
        #trace backwards and generate colors and directions for path
        
    def _create_maze(self):
        stack = []
        longest_path = []
        


    def _get_neighbors(self, state_index):
        neighbors = []
        row = state_index/self._num_cols
        col = state_index % self._num_cols
        for n in [-1, 1]:
            neighbor_row = row + n
            if neighbor_row > 0 and neighbor_row < self._num_rows:
                neighbors.append(neighbor_row*self._num_cols + col)
            neighbor_col = col + n
            if neighbor_col > 0 and neighbor_col < self._num_cols:
                neighbors.append(row*self._num_cols + neighbor_col)

        return neighbors
                
            
    def _unvisited_neighbors(self, state_index): #returns list of indices of unvisited neighbors
        unvisited = []
        neighbor_indices = self._get_neighbors(state_index)
        for neighbor_index in neighbor_indices:
            if !self._states[neighbor_index].get_is_visited():
                unvisited.append(neighbor_index)
        return unvisited
         
        
        
        
            
            
         
        
         

class 2DMazeEnv(discrete.DiscreteEnv):

    #incur penalty for every action that is taken.

    def __init__(self, desc=None, map_rows=10, map_cols=10, num_colors=4, text_directions=['left', 'right']):
    
        P = #table of transitions, new state given by P[state][action]
        isd = #initial state distribution
        super(2DMazeEnv, self).__init__(map_rows*map_cols, 4, P, isd)
        

    def _render(self, mode='human', close=False, is_test=False):

    def _get_obs() 
