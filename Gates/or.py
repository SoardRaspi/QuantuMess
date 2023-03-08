from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info.operators import Operator

qc = QuantumCircuit(3, 1)

qc.x(0)
qc.x(1)
qc.x(2)

cor = Operator([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0]
])
qc.unitary(cor, [0, 1, 2], label='cor')

qc.measure(2, 0)

%matplotlib inline
qc.draw(output="mpl")
