# SPEC collaborative
#
# Graham Scheduler code based on MESA
#
# 2021

from mesa.time import BaseScheduler


class GrahamActivation(BaseScheduler):
    """A scheduler devised by Jeff Graham the simulates concurrent, random activation of 
    pockets of agents. Agents have 'earmarks', identifiers that are associated with local
    ordering of events within one single timestep.
    """

    def step(self) -> None:
        """Executes the step of all agents, one at a time, in
        random order.
        """

        # First, partition the agents according to earmarks
        stages = {}

        for agent in self.agent_buffer(): 
            if not stages[agent.earmark]:
                 stages[agent.earmark] = []

            stages[agent.earmark].append(agent.unique_id)

        # Now, for all earmarks, randomize and execute the action sequentially across all agents
        for earmark in stages.keys():
            for unique_id in self.model.random.shuffle(stages[earmark]):
                self._agents[unique_id].step()

        self.steps += 1
        self.time += 1