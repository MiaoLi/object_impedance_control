from time import sleep

import numpy as np

import gym

from object_impedance_control.controllers.object_impedance_controller import MultiAgentObjectImpedanceController

def main():

    env = gym.make('multiagentbox-v0')

    env.reset()

    controller = MultiAgentObjectImpedanceController(3, 80, 10, agent_link_stiffness=20)
    controller.set_desired_object_pos(np.array([0, 0, 1.2]))

    while True:
        state = env._get_state()
        agent_pos = np.reshape(state, (3, -1))[:, :3]
        act_forces = controller.step(agent_pos, agent_force=None)

        env.step(act_forces.flatten())

        sleep(1./240.)


    return True


if __name__ == '__main__':
    main()