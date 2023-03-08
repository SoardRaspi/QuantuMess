from qiskit import *
from pylatexenc import *
from qiskit.tools.visualization import plot_histogram

qc = QuantumCircuit(4, 2)

qc.x([0, 1])
qc.cx(0, 2)
qc.cx(1, 2)
qc.ccx(0, 1, 3)

qc.barrier()
qc.measure([2, 3], [0, 1])

%matplotlib inline
qc.draw(output="mpl")

simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 1).result()
plot_histogram(result.get_counts())
