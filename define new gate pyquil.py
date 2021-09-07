import numpy as np
from pyquil import Program
from pyquil.quil import DefGate

# First we define the new gate from a matrix
sqrt_x = np.array([[ 0.5+0.5j, 0.5-0.5j],
                   [ 0.5-0.5j, 0.5+0.5j]])
# Get the Quil definition for the new gate


sqrt_x_definition = DefGate("SQRT-X", sqrt_x)
# Get the gate constructor
SQRT_X = sqrt_x_definition.get_constructor()
# Then we can use the new gate
p = Program()
p += sqrt_x_definition
p += SQRT_X(0)
print(p)



# Below we can define tensor multiplication of X0 and sqrt of X1
#A multi-qubit defgate example
x_gate_matrix = np.array(([0.0, 1.0], [1.0, 0.0]))
sqrt_x = np.array([[ 0.5+0.5j, 0.5-0.5j],
                   [ 0.5-0.5j, 0.5+0.5j]])
x_sqrt_x = np.kron(x_gate_matrix, sqrt_x)

x_sqrt_x_definition = DefGate("X-SQRT-X", x_sqrt_x)
X_SQRT_X = x_sqrt_x_definition.get_constructor()
# Then we can use the new gate
P = Program(X_sqrt_x_definition, X_SQRT_X(0,1))