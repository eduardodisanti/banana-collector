import numpy as np
import random
from collections import namedtuple, deque

from model import QNetwork

import torch
import torch.nn.functional as F
import torch.optim as optim

BUFFER_SIZE = int(1e5)  # replay buffer size
BATCH_SIZE = 64         # minibatch size
GAMMA = 0.99            # discount factor
TAU = 1e-3              # for soft update of target parameters
LR = 5e-4               # learning rate 
UPDATE_EVERY = 4        # how often to update the network

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
       """Initialize an Agent object.
        
        Params
        ======
            state_size (int): dimension of each state
            action_size (int): dimension of each action
            seed (int): random seed
        """
        nfilters = [128, 128*2, 128*2]
        self.seed = torch.manual_seed(seed)
        
        self.conv1 = nn.Conv3d(3, nfilters[0], kernel_size=(1, 3, 3), stride=(1,3,3))
        self.bn1 = nn.BatchNorm3d(nfilters[0])
        self.conv2 = nn.Conv3d(nfilters[0], nfilters[1], kernel_size=(1, 3, 3), stride=(1,3,3))
        self.bn2 = nn.BatchNorm3d(nfilters[1])
        self.conv3 = nn.Conv3d(nfilters[1], nfilters[2], kernel_size=(4, 3, 3), stride=(1,3,3))
        self.bn3 = nn.BatchNorm3d(nfilters[2])
        self.conv4 = nn.Conv3d(nfilters[1], nfilters[2], kernel_size=(4, 3, 3), stride=(1,3,3))
        self.bn4 = nn.BatchNorm3d(nfilters[2])
        
        conv_out_size = self._get_conv_out_size(state_size)
        fc = [conv_out_size, 1024]
        self.fc1 = nn.Linear(fc[0], fc[1])
        self.fc2 = nn.Linear(fc[1], action_size)


    def forward(self, state):
        """Build a network that maps state -> action values."""
        
        X = F.relu(self.bn1(self.conv1(state)))
        X = F.relu(self.bn2(self.conv2(X)))
        X = F.relu(self.bn3(self.conv3(X)))
        X = F.relu(self.bn3(self.conv4(X)))
        X = X.view(x.size(0), -1)

        X = F.relu(self.fc1(X))
        A = self.fc2(X)
        
        return A

    # generate input sample and forward to get shape
    def _get_conv_out_size(self, shape):
        x = torch.rand(shape)
        x = self._cnn(x)
        n_size = x.data.view(1, -1).size(1)
        print('Convolution output size:', n_size)
        return n_size
