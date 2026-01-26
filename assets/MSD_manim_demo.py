from manimlib import *
import numpy as np
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from quera_colors import *
from quera_qubit_lib import *

USE_TWEEZERS = False  # Toggle laser tweezer visuals ON or OFF

class MSDScene(Scene):
    def construct(self):
        array = QubitArray(
            layout="grid",
            rows=5, cols=17,
            qubit_spacing=0.7,
            use_vacancies=True,
            fill_pattern="all"
        )
        self.add(array)
        self.wait(0.1)

        # --- COLUMN‐BASED TRAPEZOIDAL SWAPS (can comment out for speed) ---
        source_cols = [
            [1, 10, 12, 13],
            [4, 8, 11, 15],
            [2, 8, 9, 10, 14],
            [0, 3, 5, 10, 11],
            [0, 2, 4, 6, 8, 12],
        ]
        target_cols = [
            [3, 7, 14, 16],
            [7, 10, 14, 16],
            [4, 6, 7, 13, 16],
            [2, 6, 8, 12, 13],
            [1, 3, 5, 7, 9, 15],
        ]
        for s_cols, t_cols in zip(source_cols, target_cols):
            self.perform_swap_cycle(array, s_cols, t_cols)
            self.wait(0.2)

        # --- ROW‐BASED L‐SHAPED SWAPS (only for faster testing) ---
        source_rows = [[2, 4], [1, 3], [0, 1]]
        target_rows = [[1, 3], [0, 2], [3, 4]]
        for s_rows, t_rows in zip(source_rows, target_rows):
            self.perform_row_swap_cycle(array, s_rows, t_rows)
            self.wait(0.2)

    def perform_swap_cycle(self, array, source_cols, target_cols):
        """Column‐based trapezoidal swaps with optional tweezers."""
        spacing = array.qubit_spacing
        offset = 0.3 * spacing
        col_map = dict(zip(source_cols, target_cols))

        # Identify qubits and prepare tweezers
        active = []   # list of (idx, src_col)
        tweezers = []
        for idx, (q, pos) in enumerate(array.qubits):
            x, _, _ = pos
            for col in source_cols:
                if abs(x - ((col - 8) * spacing)) < 1e-3:
                    active.append((idx, col))
                    if USE_TWEEZERS:
                        tw = DotLaserTweezer().move_to(pos).set_opacity(0)
                        self.add(tw)
                        tweezers.append((tw, idx, col))

        # Pick up
        if USE_TWEEZERS:
            for tw, idx, _ in tweezers:
                tw.move_to(array.get_qubit(idx))
            self.play(*[
                tw.pick_up(array.get_qubit(idx), show=True)[0]
                for tw, idx, _ in tweezers
            ], run_time=0.1)

        # Step 1: DOWN
        if USE_TWEEZERS:
            self.play(*[
                tw.animate.shift(DOWN * offset)
                for tw, _, _ in tweezers
            ], run_time=0.05)
        else:
            moves = [(idx, 0, -offset) for idx, _ in active]
            array.move_qubits(self, moves, run_time=0.05, animate=True)

        # Step 2: HORIZONTAL
        if USE_TWEEZERS:
            h_anims = []
            for tw, _, src in tweezers:
                dx = (col_map[src] - src) * spacing - offset
                h_anims.append(tw.animate.shift(RIGHT * dx))
            self.play(*h_anims, run_time=0.2)
        else:
            moves = []
            for idx, src in active:
                dx = (col_map[src] - src) * spacing - offset
                moves.append((idx, dx, 0))
            array.move_qubits(self, moves, run_time=0.2, animate=True)

        # Step 3: UP
        if USE_TWEEZERS:
            self.play(*[
                tw.animate.shift(UP * offset)
                for tw, _, _ in tweezers
            ], run_time=0.05)
        else:
            moves = [(idx, 0, offset) for idx, _ in active]
            array.move_qubits(self, moves, run_time=0.05, animate=True)

        self.wait(0.1)

        # Reverse: DOWN → HORIZONTAL back → UP
        if USE_TWEEZERS:
            self.play(*[
                tw.animate.shift(DOWN * offset)
                for tw, _, _ in tweezers
            ], run_time=0.05)
            rev_h = []
            for tw, _, src in tweezers:
                dx = (src - col_map[src]) * spacing + offset
                rev_h.append(tw.animate.shift(RIGHT * dx))
            self.play(*rev_h, run_time=0.2)
            self.play(*[
                tw.animate.shift(UP * offset)
                for tw, _, _ in tweezers
            ], run_time=0.05)
        else:
            moves = [(idx, 0, -offset) for idx, _ in active]
            array.move_qubits(self, moves, run_time=0.05, animate=True)
            moves = []
            for idx, src in active:
                dx = (src - col_map[src]) * spacing + offset
                moves.append((idx, dx, 0))
            array.move_qubits(self, moves, run_time=0.2, animate=True)
            moves = [(idx, 0, offset) for idx, _ in active]
            array.move_qubits(self, moves, run_time=0.05, animate=True)

        # Release
        if USE_TWEEZERS:
            self.play(*[
                tw.release(hide=True)[0]
                for tw, _, _ in tweezers
            ], run_time=0.1)


    def perform_row_swap_cycle(self, array, source_rows, target_rows):
        """Row‐based L‐shaped swaps with optional tweezers."""
        spacing = array.qubit_spacing
        offset = 0.3 * spacing
        row_map = dict(zip(source_rows, target_rows))

        active = []    # list of (idx, src_row)
        tweezers = []
        for idx, (q, pos) in enumerate(array.qubits):
            _, y, _ = pos
            for row in source_rows:
                if abs(y - ((2 - row) * spacing)) < 1e-3:
                    active.append((idx, row))
                    if USE_TWEEZERS:
                        tw = DotLaserTweezer().move_to(pos).set_opacity(0)
                        self.add(tw)
                        tweezers.append((tw, idx, row))

        # Pick up
        if USE_TWEEZERS:
            for tw, idx, _ in tweezers:
                tw.move_to(array.get_qubit(idx))
            self.play(*[
                tw.pick_up(array.get_qubit(idx), show=True)[0]
                for tw, idx, _ in tweezers
            ], run_time=0.1)

        # Step 1: RIGHT
        self.play(*[
            tw.animate.shift(RIGHT * offset)
            for tw, _, _ in tweezers
        ], run_time=0.05)

        # Step 2: VERTICAL
        v_anims = []
        for tw, _, src in tweezers:
            dy = (row_map[src] - src) * -spacing
            v_anims.append(tw.animate.shift(UP * dy))
        self.play(*v_anims, run_time=0.2)
        self.wait(0.1)

        # Reverse vertical
        rv = []
        for tw, _, src in tweezers:
            dy = (src - row_map[src]) * -spacing
            rv.append(tw.animate.shift(UP * dy))
        self.play(*rv, run_time=0.2)

        # Step 3: LEFT back
        self.play(*[
            tw.animate.shift(LEFT * offset)
            for tw, _, _ in tweezers
        ], run_time=0.05)

        # Release
        self.play(*[
            tw.release(hide=True)[0]
            for tw, _, _ in tweezers
        ], run_time=0.1)
