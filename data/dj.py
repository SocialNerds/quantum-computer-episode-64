# Import the Qiskit SDK.
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute

# Create a Quantum Register with 3 qubits.
q = QuantumRegister(3)
# Create a Classical Register with 3 bits.
c = ClassicalRegister(3)
# Create a Quantum Circuit.
qc = QuantumCircuit(q, c)

# Add a H gate on all qubits, putting this qubit in superposition.
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

# Applying Oracle.
qc.h(q[2])
qc.z(q[0])
qc.cx(q[1], q[2])
qc.h(q[2])

# Applying hadamard gate again.
qc.h(q[0])
qc.h(q[1])
qc.h(q[2])

# Add a Measure gate to see the state.
qc.measure(q, c)

# Compile and run the Quantum circuit on a simulator backend.
job_sim = execute(qc, "local_qasm_simulator")
sim_result = job_sim.result()

# Show the results.
print("simulation: ", sim_result)
print(sim_result.get_counts(qc))