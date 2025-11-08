# -*- coding: utf-8 -*-
# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    # Ensemble pour mémoriser les états déjà visités
    visited = set()
    
    def dfs(state, path):
        """
        Fonction récursive pour explorer le graphe.
        
        Args:
            state: l'état courant
            path: la liste d'actions pour atteindre cet état
            
        Returns:
            Le chemin (liste d'actions) menant à un état but si trouvé, sinon None.
        """
        # Vérifier l'état but
        if problem.isGoalState(state):
            return path
        
        # Marquer l'état courant comme visité pour éviter les cycles
        visited.add(state)
        
        # Examiner chacun des successeurs
        for successor, action, _ in problem.getSuccessors(state):
            if successor not in visited:
                new_path = path + [action]
                result = dfs(successor, new_path)
                if result is not None:
                    return result
        # Aucun chemin trouvé depuis cet état
        return None

    # Lancer la recherche depuis l'état de départ
    start_state = problem.getStartState()
    result = dfs(start_state, [])
    
    # Si aucun chemin n'est trouvé, renvoyer une liste vide
    return result if result is not None else []
    util.raiseNotDefined()

    
def breadthFirstSearch(problem):
    """
    Effectue une recherche en largeur (BFS) sur le problème donné.
    
    Args:
        problem: une instance d'un problème de recherche qui fournit les méthodes
                 getStartState(), isGoalState(state) et getSuccessors(state)
    
    Retourne:
        Une liste d'actions menant de l'état initial à un état but.
    """
    # Importation de la structure de file d'attente depuis utils.py
    from util import Queue
    
    # Initialiser la file d'attente avec le tuple: (état actuel, chemin jusqu'à cet état)
    start_state = problem.getStartState()
    frontier = Queue()
    frontier.push((start_state, []))
    
    # Pour éviter d'explorer plusieurs fois le même état,
    # on enregistre les états visités (ou déjà en attente d'exploration).
    visited = set()
    visited.add(start_state)
    
    while not frontier.isEmpty():
        # On récupère le premier élément de la file d'attente
        current_state, path = frontier.pop()
        
        # Si l'état courant est un état but, retourner le chemin pour y arriver.
        if problem.isGoalState(current_state):
            return path
        
        # Parcourir chacun des successeurs de l'état courant.
        for successor, action, _ in problem.getSuccessors(current_state):
            # Vérifier que le successeur n'a pas déjà été visité pour éviter les doublons.
            if successor not in visited:
                visited.add(successor)
                new_path = path + [action]
                frontier.push((successor, new_path))
    
    # Si aucun chemin menant à un état but n'a été trouvé, retourner une liste vide.
    return []

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
