# Bananna colector
![Trained agent](https://github.com/eduardodisanti/deep_reinforcement_learning_nd/blob/master/p1_banana/banana_collector.gif)

### Introduction

This project shows how to train the Banana colector in an Udacity modified (from Unity's) Bannana-colector environment.
The goal of the agent is to collect as many yellow bananas while avoiding blue bananas.

![Trained Agent][image1]

A reward of **+1** is provided for collecting a yellow banana, and a reward of **-1** is provided for collecting a blue banana.  There is no reward, positive or negative for moving or time.
The environment is a square world and the state space has 37 dimensions including the agent speed and a [ray-based]( https://en.wikipedia.org/wiki/Ray_tracing_(graphics)) perception of objects arround the agent forward direction.
The agent can perform four actions:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

### Files description
***Navigation.ipynb***
	Contains the necessary code to train the agent and show results.
***dqn_agent.py***
	Defines the DQN agent to solve the environment.
***model.py***
	Defines the Neural Network that the agents uses to generalize actions.
***auxs.py***
	Some helper functions like moving average.
***play_banana.ipynb***
	A notebook to see the agent in action.
***train_agent_headless.py***
	Contains code for training the agent that can be run standalone .

### Training the agent

*Refer to "Setting up the environment" section to download the environment for this project if you don't have the Unity environment installed.*

 - On the Jupiter notebook, 
		 Open the Navigation notebook and run all cells 
		 During the training a graph will be displayed and updated at the end of every episode.  (img)
		 
			or
- run the train_agent_headless.py using the command *python  train_agent_headless.py*, 

The training will stop when the agent reach an average of 13 on las 100 scenarios. (Will happen around 340 episodes) 

## Agent characteristics

### Algorithm
The agent uses a  [Deep Q-Learning algorithm](https://storage.googleapis.com/deepmind-media/dqn/DQNNaturePaper.pdf)
The neural network that estimate the action-value function has following architecture:

|  Layer | Neurons Size  | Type | Activation | Comment |
|--------|-------|------|------------|---------|
|Input  |    37 | | | according to the space state dimension | 
|Hidden 1  |  32 | Linear | ReLU |
|Hidden 2  |  32 | Linear | ReLU |
|Output  |  4 | Linear | ReLU | One for each action

The  optimization algorithm used was **Adam**
Chossen learning rate **5e-4**
#### Hyperparameters
-   Discount factor, $\gamma$ 0.99
-   Soft-update ratio, $\tau$     0.001
-   Network update interval
    -  Local every **4** time steps.
    -  Target every **4** time steps.
-   Replay buffer size  **64**
-   Minibatch size **64**
-   $\epsilon$ configuration and anealing for **e-greedy policy**
    -   Start          : 1
    -   Minumin.  : 0.01
    -   Decay rate: 0.995
    - 
With the above hyperparameters, the average score of the last 100 episodes reached 13.03 after 321 episodes.
The agent performed actions acording to this table:
| Action | Frequency |
| --|---|
| 0 | 76283 |
| 1 | 3030 |
| 2 | 791 |
| 3 | 20996 |

(image)

## Apendices
### Setting up the environment
1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

You need only select the environment that matches your operating system:
- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Windows_x86_64.zip)

Then, place the file in the `p1_navigation/` folder in the DRLND GitHub repository, and unzip (or decompress) the file.  Next, open `Navigation_Pixels.ipynb` and follow the instructions to learn how to use the Python API to control the agent.

(_For AWS_) If you'd like to train the agent on AWS, you must follow the instructions to [set up X Server](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above.

2. Place the file in the DRLND GitHub repository, in the `p1_navigation/` folder, and unzip (or decompress) the file. 