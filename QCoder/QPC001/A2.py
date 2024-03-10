from qiskit import QuantumCircuit
from qiskit.circuit.library import HGate


def solve(n: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for i in range(n):
        qc.h(i)

    return qc


# """
from qiskit import Aer, execute


def simulate(qc: QuantumCircuit):
    simulator = Aer.get_backend("statevector_simulator")
    statevector = execute(qc, simulator).result().get_statevector(qc)
    print(statevector)
    print(dir(statevector))
    print(statevector.data)
    print(statevector.dim)
    print(statevector.dims)
    sv(statevector)


def sv(statevector):
    dim = statevector.num_qubits
    ket = f"|{{:0{dim}b}}>"
    for i, c in enumerate(statevector.data):
        print(ket.format(i), c)


simulate(solve(3))
# """
