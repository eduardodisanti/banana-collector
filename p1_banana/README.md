# Bananna colector

<center>
	<img src="https://github.com/eduardodisanti/deep_reinforcement_learning_nd/blob/master/p1_banana/media/banana_collector.gif" alt="drawing" width="480"/>
</center>

## Introduction

This project shows how to train the Banana colector environment in the Udacity modified (from Unity's Bannana-colector) environment.
The goal of the agent is to collect as many yellow bananas while avoiding blue bananas. The environment grants positive rewards for yellow bananas and negative for blue ones.
This project trains the agent to play the game using [ray-based](https://en.wikipedia.org/wiki/Ray_tracing_(graphics)) perception of objects arround the agent forward direction. Check [Report file](https://github.com/eduardodisanti/deep_reinforcement_learning_nd/blob/master/p1_banana/report/Report.pdf) for technical specifications, algorithm, hyperparameters and architecture of the neural network.

## Files description

|  File | Description | Location |
|-------|-------------|----------|
| Navigation.ipynb  | Notebook that trains the model and track progress | /p1_banana |
| play_banana.ipynb  | A notebook to see the agent in action and assess it | /p1_banana |
| dqn_agent.py  | Defines the DQN agent to solve the environment. | /p1_banana/code |
| model.py  | Defines the Neural Network that the agents uses to generalize actions. | /p1_banana/code |
| auxs.py  | Some helper functions like moving average. | /p1_banana/code |
| train_agent_headless.py  | Contains code for training the agent that can be run standalone | /p1_banana/code |
| Report.pdf  | Technical paper and training report | /p1_banana/report |
| banana_raytracing_eds.pt | Saved weights of the agent neural network | /p1_banana/model
| banana_play.m4v | A video showing the trained agend | /p1_banana/media

## Instructions 
*Refer to "Setting up the environment" section to download the environment for this project in case you don't have the Unity environment installed.*

### Training the agent

- Training in a Jupyter notebook (recommended), 
	Open the Navigation notebook and run all cells <br/>
	During the training a graph will be displayed, updated at the end of every episode.<br/>
	At the end of the training a final figure with appear showing the rewards, average, moving average and goal<br/>
	<center>
		<img src="https://github.com/eduardodisanti/deep_reinforcement_learning_nd/blob/master/p1_banana/report/training2.png" alt="training report" width="320"/>
	</center>
	
- Training from the command line,
	Execute *cd code*<br/>
	Run the train_agent_headless.py using the command *python train_agent_headless.py*<br/>
	During the training the progress of the training will be written to the console. <br/>

The training will stop when the agent reach an average of 13 on last 100 scenarios. (Will happen around 330 episodes) 

### Assesing the agent

In a jupyter notebook open play_banana.ipynb and run all cells.<br>
At the end of 100 trails of 2000 steps each, a report will be shown containing the returns achieved by the agent.
<img src="https://github.com/eduardodisanti/deep_reinforcement_learning_nd/blob/master/p1_banana/report/play_scores.png" alt="drawing" width="320"/><br/>

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

(_For AWS_) If you'd like to train the agent on AWS, you must follow the instructions to [set up X Server](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above.

2. Then, place the files and folders of this repository in the `p1_navigation/` folder in the DRLND GitHub repository, you can overwrite any file in conflict.  Next, open `Navigation.ipynb` to train the agent.


