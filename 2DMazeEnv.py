import numpy as np
import sys
from six import StringIO, b
from sets import Set

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
            
        def set_color(self, wall, color):
            assert wall in [0, 1, 2, 3]
            if wall == 0:
                self._left_color = color    
            elif wall = 1:
                self._down_color = color
            elif wall = 2:
                self._right_color = color
            elif wall = 3:
                self._up_color = color
            
    
        def get_color(self, wall):
            assert wall in [0, 1, 2, 3]
            if wall == 0:
                return self._left_color
            elif wall = 1:
                return self._down_color
            elif wall = 2:
                return self._right_color
            elif wall = 3:
                return self._up_color

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
        self._create_maze()       
 
    def _create_maze(self):
        stack = []
        longest_path = []
        curr_state_index = 0
        backtracked_indices = Set()
        while len(backtracked_indices) < self._num_rows*self._num_cols:
            unvisited_neighbors = self._get_unvisited_neighbors(curr_state_index)
            neighbors = self._get_neighbors(curr_state_index)
            unvisited_neighbors = self._get_unvisited(neighbors)
            if len(unvisited_neighbors) > 0:
                prev_state_index = curr_state_index
                curr_state_index = np.random.choice(curr_state_neighbors, 1)
                action = neighbors.index(curr_state_index) 
                self._transitions[prev_state_index][action] = curr_state_index
                self._states[prev_state_index].set_color(action, BLACK)
                
            else:
                # backtrack
                # at end of backtrack, append all to Set()
                # update longest_path if longer than longest 
              
        

    def _get_neighbors(self, state_index):
        neighbors = []
        row = state_index/self._num_cols
        col = state_index % self._num_cols
        for n in [-1, 1]:
            neighbor_col = col + n
            if neighbor_col > 0 and neighbor_col < self._num_cols:
                neighbors.append(row*self._num_cols + neighbor_col)
            else:
                neighbors.append(-1)
            neighbor_row = row + -1*n #to make order conform to actions
            if neighbor_row > 0 and neighbor_row < self._num_rows:
                neighbors.append(neighbor_row*self._num_cols + col)
            else:
                neighbors.append(-1)

        return neighbors
                
            
    def _get_unvisited(self, indices_list): #returns list of indices of unvisited neighbors
        return filter(lambda x: x != -1 and self._states[x].get_is_visited(), indices_list)
        '''
        unvisited = []
        neighbor_indices = self._get_neighbors(state_index)
        for neighbor_index in neighbor_indices:
            if neighbor_index == -1:
                continue
            if !self._states[neighbor_index].get_is_visited():
                unvisited.append(neighbor_index)
        return unvisited
        ''' 
        
        
        
            
            
         
        
         

class 2DMazeEnv(discrete.DiscreteEnv):

    #incur penalty for every action that is taken.

    def __init__(self, desc=None, map_rows=10, map_cols=10, num_colors=4, text_directions=['left', 'right']):
    
        P = #table of transitions, new state given by P[state][action]
        isd = #initial state distribution
        super(2DMazeEnv, self).__init__(map_rows*map_cols, 4, P, isd)
        

    def _render(self, mode='human', close=False, is_test=False):

    def _get_obs() 
