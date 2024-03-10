from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    qc.h(0)
    qc.cx(0, 1)

    return qc


# """
from qiskit import Aer, execute


def simulate(qc: QuantumCircuit):
    simulator = Aer.get_backend("statevector_simulator")
    statevector = execute(qc, simulator).result().get_statevector(qc)
    sv(statevector)


def sv(statevector):
    dim = statevector.num_qubits
    ket = f"|{{:0{dim}b}}>"
    for i, c in enumerate(statevector.data):
        print(ket.format(i), c)


simulate(solve())
# """
