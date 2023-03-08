from qiskit import *
from qiskit.quantum_info.operators import Operator

qc = QuantumCircuit(2, 2)

qc.x(0)

swap = Operator([
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
])
qc.unitary(swap, [0, 1], label='swap')

qc.measure([0, 1], [0, 1])

%matplotlib inline
qc.draw(output="mpl")

from qiskit.tools.visualization import plot_histogram
simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 1).result()
plot_histogram(result.get_counts())
