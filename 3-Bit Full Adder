from qiskit import *
from pylatexenc import *

qc = QuantumCircuit(4, 2)

qc.x(0)
qc.x(1)
qc.x(2)
qc.barrier()

qc.ccx(0, 1, 3)
qc.cx(0, 1)
qc.ccx(1, 2, 3)
qc.cx(1, 2)
qc.barrier()

qc.measure(2, 0)
qc.measure(3, 1)

%matplotlib inline
qc.draw(output = "mpl")

from qiskit.tools.visualization import plot_histogram
simulator = Aer.get_backend("qasm_simulator")
result = execute(qc, backend = simulator, shots = 1).result()

plot_histogram(result.get_counts())
