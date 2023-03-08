from qiskit import *
from qiskit.quantum_info.operators import Operator

in0 = QuantumRegister(1, 'input 1')
in1 = QuantumRegister(1, 'input 2')
c = QuantumRegister(1, 'control')
meas = ClassicalRegister(1, 'meas')
qc = QuantumCircuit(in0, in1, c, meas)

qc.x(0)
qc.x(1)
qc.x(2)

cand = Operator([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0]
])
qc.unitary(cand, [0, 1, 2], label='cand')

qc.measure(2, 0)

%matplotlib inline
qc.draw(output="mpl")

from qiskit.tools.visualization import plot_histogram
simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 1).result()
plot_histogram(result.get_counts())
