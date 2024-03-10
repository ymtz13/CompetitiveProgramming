from qiskit import QuantumCircuit
from math import pi, asin, sqrt, floor


def oracle(qc: QuantumCircuit, n: int, L: int) -> QuantumCircuit:
    K = L - 1

    xgates = []
    for i in range(n - 1, -1, -1):
        if (K >> i) & 1:
            continue

        if i < n - 1:
            qc.mcp(pi, list(range(i + 1, n)), i)
        else:
            qc.z(i)

        xgates.append(i)
        qc.x(i)

    for i in xgates:
        qc.x(i)

    return qc


def solve(n: int, L: int) -> QuantumCircuit:
    qc = QuantumCircuit(n)
    # Write your code here:
    for i in range(n):
        qc.h(i)

    theta = asin(sqrt(L / (1 << n)))
    r = floor(pi / (4 * theta))
    # print(theta, r)

    for _ in range(r):
        oracle(qc, n, L)

        for i in range(n):
            qc.h(i)
            qc.x(i)

        if n > 1:
            qc.mcp(pi, list(range(n - 1)), n - 1)
        else:
            qc.z(n - 1)

        for i in range(n):
            qc.x(i)
            qc.h(i)

    return qc


# """
from qiskit import Aer, execute


def simulate(qc: QuantumCircuit):
    simulator = Aer.get_backend("statevector_simulator")
    statevector = execute(qc, simulator).result().get_statevector(qc)
    sv(statevector)
    print(f"depth: {qc.depth()}")


def sv(statevector):
    dim = statevector.num_qubits
    ket = f"|{{:0{dim}b}}>"
    for i, c in enumerate(statevector.data):
        print(ket.format(i), c)


n, L = map(int, input().split())
simulate(solve(n, L))
# """
