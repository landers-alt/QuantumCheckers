import copy
from io import BytesIO

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, Rectangle
from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from qiskit_aer.backends.aer_simulator import AerSimulator

SUPPORTED_GATES = ['x', 'y', 'z', 'h', 'cz']

class QuantumGame():
    def __init__(self,
                 initialize: list[tuple[int, str]],
                 allowed_gates: list[str] = SUPPORTED_GATES,
                 shots: int = 1024,
                 backend=None,
                 rectangle_length: float = None,
                 circle_radius: float = None):

        self.circuit = self.create_circuit()

        self.allowed_gates = allowed_gates

        self.backend = AerSimulator() if backend is None else backend
        self.shots = shots

        self.probabilities = None

        self.rectangle_length = rectangle_length or 0.98*np.sqrt(2)
        self.circle_radius = circle_radius or 0.6

        self.grid_figure = plt.figure(figsize=(8, 5), dpi=100)
        self.grid_figure.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.ax = self.grid_figure.add_subplot(111)
        self.ax.set_xlim(-3.5, 4.5)
        self.ax.set_ylim(-1.5, 3.5)
        self.ax.set_axis_off()

        self.box_coords = {
            'ZI':(-0.5, -0.5),
            'XI':(-1.5, 0.5),
            'IZ':( 1.5, -0.5),
            'IX':( 2.5, 0.5),
            'ZZ':( 0.5, 0.5),
            'ZX':( 1.5, 1.5),
            'XZ':(-0.5, 1.5),
            'XX':( 0.5, 2.5)
        }

        for qbit, gate in initialize:
            self.apply_gate(qbit, gate)

    def create_circuit(self) -> QuantumCircuit:

        self.qr = QuantumRegister(2, 'q')
        self.cr = ClassicalRegister(2)
        qc = QuantumCircuit(self.qr, self.cr)

        return qc

    def draw_circuit(self) -> BytesIO:
        figure = self.circuit.draw(output='mpl')

        out_buffer = BytesIO()
        figure.savefig(out_buffer)
        out_buffer.seek(0)

        return out_buffer

    def update_grid(self, run_kwargs: dict = {}) -> None:
        self.run_circuit(**run_kwargs)

        points = {}
        for pauli in self.box_coords:
            prob = (1-self.probabilities[pauli])/2
            color=(prob,prob,prob)
            points[pauli] = self.ax.add_patch(Circle(self.box_coords[pauli], self.circle_radius, color=color, zorder=10))

        for pauli in self.box_coords:
            color = (60/255,120/255,216/255) if 'I' not in pauli else (17/255,85/255,204/255)
            self.ax.add_patch(Rectangle((self.box_coords[pauli][0], self.box_coords[pauli][1]-1), self.rectangle_length, self.rectangle_length, angle=45, color=color))

    def draw_grid(self) -> BytesIO:
        self.update_grid()
        out_buffer = BytesIO()
        self.grid_figure.savefig(out_buffer, transparent=True)
        out_buffer.seek(0)

        return out_buffer

    def apply_gate(self, qubit_idx: int, gate: str, **params) -> None:
        assert gate in self.allowed_gates, f'Gate {gate} not supported'

        getattr(self.circuit, gate)(qubit_idx, **params)

    def run_circuit(self, **kwargs) -> None:
        self.probabilities = {}

        corr = ['ZZ','ZX','XZ','XX']
        identities = ['ZI', 'XI', 'IZ', 'IX']

        results = {}
        for basis in corr:
            temp_circuit = copy.deepcopy(self.circuit)
            for i in range(2):
                if basis[i] == 'X':
                    temp_circuit.h(i)

            temp_circuit.barrier()
            temp_circuit.measure(self.qr, self.cr)

            job = self.backend.run(temp_circuit, shots=self.shots, **kwargs)
            results[basis] = job.result().get_counts()

            for key, value in results[basis].items():
                results[basis][key] = value/self.shots

        probabilities = {}
        for identity in identities:
            probabilities[identity] = 0
            for basis, counts in results.items():
                if basis[(identity.index('I') + 1) % 2] != identity[(identity.index('I') + 1) % 2]:
                    continue
                for string, count in counts.items():
                    if string[identity.index('I')] == '1':
                        probabilities[identity] += count/2

        for basis in corr:
            probabilities[basis] = 0
            for string, probability in results[basis].items():
                if string[0] != string[1]:
                    probabilities[basis] += probability

        for basis, probability in probabilities.items():
            self.probabilities[basis] = 1-2*probability
