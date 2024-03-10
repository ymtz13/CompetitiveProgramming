from qiskit import QuantumCircuit
from math import asin, sqrt


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(2)
    # Write your code here:
    theta = asin(1 / sqrt(3))
    qc.ry(theta * 2, 0)
    qc.x(0)
    qc.ch(0, 1)
    qc.x(0)

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
