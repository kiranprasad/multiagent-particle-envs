from multiagent.policy.policy import Policy
import numpy as np

class RandomPolicy(Policy):
    def __init__(self, env, agent_index):
        super(RandomPolicy, self).__init__()
        self.env = env
    
    def action(self, obs):
        # use observation

        u = int(np.random.random_integers(0,4))
        return u