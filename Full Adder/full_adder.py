from qiskit import *
from pylatexenc import *
from qiskit.tools.visualization import plot_histogram
from qiskit.quantum_info.operators import Operator

in1 = QuantumRegister(1, "input 1")
in2 = QuantumRegister(1, "input 2")
in3 = QuantumRegister(1, "input 3")
rest = QuantumRegister(6)
meas = ClassicalRegister(2, "meas")

# qc = QuantumCircuit(9, 2)
qc = QuantumCircuit(in1, in2, in3, rest, meas)

# Inputs
qc.x(0)
qc.x(1)
qc.x(2)

qc.cx(0, 3)
qc.cx(1, 3)
qc.ccx(0, 1, 4)
qc.barrier()

qc.cx(2, 5)
qc.cx(3, 5)
qc.ccx(2, 3, 6)
qc.barrier()

cor = Operator([
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0]
])
qc.unitary(cor, [4, 6, 8], label='cor')
qc.barrier()
qc.measure([5, 8], [0, 1])

%matplotlib inline
qc.draw(output="mpl")

simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 1).result()
plot_histogram(result.get_counts())
