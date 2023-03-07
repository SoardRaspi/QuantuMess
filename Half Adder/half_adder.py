from qiskit import *
from pylatexenc import *
from qiskit.tools.visualization import plot_histogram

qc = QuantumCircuit(3, 2)
qc.x(0)
qc.x(1)

qc.ccx(0, 1, 2)
qc.cx(0, 1)

qc.barrier()
qc.measure(2, 1)
qc.measure(1, 0)

%matplotlib inline

qc.draw(output = "mpl")

simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 1).result()
plot_histogram(result.get_counts())
