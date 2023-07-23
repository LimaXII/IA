# qlearningAgents.py
# ------------------
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


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        self.q_values = util.Counter()

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        return self.q_values[(state, action)]

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        legal_actions = self.getLegalActions(state)
        # Se não possuir ações possíveis
        if len(legal_actions) == 0:
          return 0.0
        # Variável que irá guardar o valor máximo de todas as ações.
        max_action = float('-inf')
        # Para cada ação, verifica se o valor dessa ação é maior do que todos os outros valores já vistos, se sim, troca o valor de max_action
        for action in legal_actions:
          value_action = self.getQValue(state, action)
          if value_action > max_action:
            max_action = value_action
        return max_action

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        legal_actions = self.getLegalActions(state)
        # Se não possuir ações possíveis
        if len(legal_actions) == 0:
          return None
        # Variável que irá guardar o valor máximo de todas as ações.
        max_action = float('-inf')
        # Para cada ação
        for action in legal_actions:
          value_action = self.getQValue(state, action)
          # Se o valor da ação for maior ou igual a todas as outras ações já vistas
          if value_action >= max_action:
            # Se o valor for o mesmo, desempata aleatoriamente
            if value_action == max_action:
              best_action = random.choice([action, best_action])
            else:
              best_action = action
            # max_action é atualizado com o maior valor de ação
            max_action = value_action
        return best_action

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        "*** YOUR CODE HERE ***"
        legalActions = self.getLegalActions(state)
        # Probabilidade p de fazer uma ação aleatória
        if util.flipCoin(self.epsilon):
          action = random.choice(legalActions)
        # Probabilidade (p-1) de fazer a melhor ação
        else:
          action = self.getPolicy(state)
          
        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        if not nextState:
          # Q(s,a) <- Q(s,a) + a[r - Q(s,a)]
          self.q_values[(state, action)] += self.alpha * (reward - self.getQValue(state, action))
        else:
          # Q(s,a) <- Q(s,a) + a[r + y.max{a'}Q(s',a') - Q(s,a)]
          self.q_values[(state, action)] += self.alpha * (reward + self.discount * self.getValue(nextState) - self.getQValue(state, action))

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        sum = 0
        features = self.featExtractor.getFeatures(state = state, action = action)
        for feature in features:
           sum += features[feature] * self.weights[feature]
        return sum

        util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
            Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"

        # Calcula a diferença
        difference = (reward + self.discount * self.getValue(state = nextState)) - self.getQValue(state = state, action = action)
        features = self.featExtractor.getFeatures(state = state, action = action)
        # Para cada feature, atualiza o valor do seu peso.
        for feature in features:
            self.weights[feature] = self.weights[feature] + self.alpha * difference * features[feature]


    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass
