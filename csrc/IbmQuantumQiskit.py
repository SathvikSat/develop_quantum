import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit import IBMQ
from qiskit.visualization import plot_histogram

#Use Aer's qasm_simulator
simulator = QasmSimulator()

# Create a Qauntum Circuit acting on q register
# intialise 2 qubits in zero state; with 2 classical bits set to zero;
#and the circuit is quantum circuit
#QuantumCircuit( int, int)

circuit = QuantumCircuit(2, 2)

#Creating the Bell's Entanglement state


#Add a H gate on qubit 0
circuit.h(0)

#Add a CX ( CNOT ) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

#Map the quantum measurements to classical bits
#if you pass the entire quantum and classical registers  to measure
# the ith qubit result will be stored in ith classical bit.
circuit.measure( [0, 1], [0, 1] )

#compile the circuit down to low-level QASM instructions
# supported by backend ( not needed for simple circuits)


compiled_circuit = transpile( circuit, simulator)

#execute the circuit on the qasm simulator
# shots maybe for the expected value of the measurement
job = simulator.run( compiled_circuit, shots=1000)

result = job.result()

#return counts
counts = result.get_counts(compiled_circuit)
print("\n Total count for 00 and 11 are: \n",counts)

#Draw the circuit
circuit.draw()

plot_histogram(counts)
if(0):
    provider = IBMQ.load_account()
    backend = provider.get_backend('ibmq_qasm_simulator')

print("Hello IBM Quantum")
