from qiskit import QuantumCircuit, QuantumRegister


def solve() -> QuantumCircuit:
    x, y = QuantumRegister(1), QuantumRegister(1)
    qc = QuantumCircuit(x, y)
    # Write your code here:
    qc.cx(x, y)

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
