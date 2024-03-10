from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.h(0)

    return qc


# """
from qiskit import Aer, execute


def simulate(qc: QuantumCircuit):
    simulator = Aer.get_backend("statevector_simulator")
    statevector = execute(qc, simulator).result().get_statevector(qc)
    print(statevector)
    sv(statevector)


def sv(statevector):
    for i, c in enumerate(statevector):
        print(f"|{i:01b}>:", c)


simulate(solve())
# """
