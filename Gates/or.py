from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info.operators import Operator

in0 = QuantumRegister(1, 'input 1')
in1 = QuantumRegister(1, 'input 2')
c = QuantumRegister(1, 'control')
meas = ClassicalRegister(1, 'meas')
qc = QuantumCircuit(in0, in1, c, meas)

qc.x(0)
qc.x(1)
qc.x(2)

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
qc.unitary(cor, [0, 1, 2], label='cor')

qc.measure(2, 0)

%matplotlib inline
qc.draw(output="mpl")

simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 8192).result()
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts())
