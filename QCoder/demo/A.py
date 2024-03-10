from qiskit import QuantumCircuit


def solve() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    # Write your code here:
    qc.x(0)

    return qc


"""
from qiskit import Aer, execute


def simulate(qc: QuantumCircuit):
    simulator = Aer.get_backend("statevector_simulator")
    statevector = execute(qc, simulator).result().get_statevector(qc)
    print(statevector)


if __name__ == "__main__":
    simulate(solve())
"""
