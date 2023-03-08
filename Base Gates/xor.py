from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info.operators import Operator

qc = QuantumCircuit(2, 1)

qc.x([0, 1])

# Method 1
# cx = Operator([
#     [1, 0, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, 1, 0],
#     [0, 1, 0, 0]
# ])

# Method 2
# cx = Operator([
#     [1, 0, 0, 0],
#     [0, 1, 0, 0],
#     [0, 0, 0, 1],
#     [0, 0, 1, 0]
# ])

# Method 3
cx = Operator([
    [1, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0]
])
qc.unitary(cx, [0, 1], label='cx')

qc.measure(1, 0)

%matplotlib inline
qc.draw(output="mpl")

simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 8192).result()
from qiskit.tools.visualization import plot_histogram
plot_histogram(result.get_counts())
