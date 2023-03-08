from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info.operators import Operator
from qiskit.tools.visualization import plot_histogram

circuit = QuantumCircuit(1, 1)

x_gate = Operator([
    [0, 1],
    [1, 0]
])
circuit.unitary(x_gate, 0, label='x_gate')
circuit.measure(0, 0)

%matplotlib inline
circuit.draw(output = "mpl")

simulator = Aer.get_backend("qasm_simulator")
result = execute(circuit, backend = simulator, shots = 1).result()
plot_histogram(result.get_counts())
