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

simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 8192).result()
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts())
