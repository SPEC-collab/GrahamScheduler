# SPEC collaborative
#
# Graham Scheduler code based on MESA
#
# 2021
from mesa import Agent, Model
from spec.grahamscheduler import GrahamActivation


class GrahamModel(Model):
    """A model to test Graham scheduling."""
    def __init__(self, N, P):
        self.num_agents = N
        self.partitions = P
        self.schedule = GrahamActivation(self, self.partitions)

        # Create agents with earmarks
        for i in range(self.num_agents):
            a = GrahamAgent(i, self, i % self.partitions)
            print(f"Adding agent {i}")
            self.schedule.add(a)
 
    def step(self):
        print(f"Model step {self.schedule.steps}")
        self.schedule.step()

class GrahamAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, earmark):
        super().__init__(unique_id, model)
        self.earmark = earmark

    def step(self):
        print(f'My earmark is: {self.earmark}, my unique id is {self.unique_id}')

model = GrahamModel(10, 5)

for i in range(5):
    model.step()

