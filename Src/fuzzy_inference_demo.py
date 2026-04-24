import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Inputs
health = ctrl.Antecedent(np.arange(0, 101, 1), 'health')
distance = ctrl.Antecedent(np.arange(0, 101, 1), 'distance')
skill = ctrl.Antecedent(np.arange(0, 101, 1), 'skill')

# Output
aggression = ctrl.Consequent(np.arange(0, 101, 1), 'aggression')

# Membership functions
health['low'] = fuzz.trimf(health.universe, [0, 0, 50])
health['medium'] = fuzz.trimf(health.universe, [25, 50, 75])
health['high'] = fuzz.trimf(health.universe, [50, 100, 100])

distance['close'] = fuzz.trimf(distance.universe, [0, 0, 50])
distance['far'] = fuzz.trimf(distance.universe, [50, 100, 100])

skill['low'] = fuzz.trimf(skill.universe, [0, 0, 50])
skill['high'] = fuzz.trimf(skill.universe, [50, 100, 100])

aggression['defensive'] = fuzz.trimf(aggression.universe, [0, 0, 50])
aggression['aggressive'] = fuzz.trimf(aggression.universe, [50, 100, 100])

# Rules
rule1 = ctrl.Rule(health['low'] & distance['close'], aggression['defensive'])
rule2 = ctrl.Rule(health['high'] & skill['low'], aggression['aggressive'])
rule3 = ctrl.Rule(distance['far'] & skill['high'], aggression['defensive'])

system = ctrl.ControlSystem([rule1, rule2, rule3])
sim = ctrl.ControlSystemSimulation(system)

# Example input
sim.input['health'] = 70
sim.input['distance'] = 30
sim.input['skill'] = 60

sim.compute()
print("Aggression Level:", sim.output['aggression'])