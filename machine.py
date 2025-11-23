import numpy as np
import pandas as pd
import requests


class Turing_Machine:
    def __init__(self, tape_strng="", blank="_", initial_st="q0", final_st=None, transition_fnc=None):
        # Using numpy array for advanced storage
        self.tape = np.array(list(tape_strng), dtype='<U1')
        self.blank = blank
        self.head = 0
        self.state = initial_st
        self.final_states = set(final_st) if final_st else set()
        
        # Store transition table as pandas DataFrame
        self.transition_df = pd.DataFrame([
            {"state": k[0], "symbol": k[1], "write": v[0], "move": v[1], "next": v[2]}
            for k, v in transition_fnc.items()
        ])

        self.transition_function = transition_fnc

    def step(self):
        """Execute one transition based on current state and tape symbol."""
        # Read current tape symbol
        if self.head < len(self.tape):
            crnt_smbl = self.tape[self.head]
        else:
            crnt_smbl = self.blank

        key = (self.state, crnt_smbl)

        if key not in self.transition_function:
            return False

        new_symbol, direction, new_state = self.transition_function[key]

        # Write symbol to numpy tape
        if self.head < len(self.tape):
            self.tape[self.head] = new_symbol
        else:
            self.tape = np.append(self.tape, new_symbol)

        # Move head
        if direction == "R":
            self.head += 1
        elif direction == "L":
            self.head = max(0, self.head - 1)

        self.state = new_state
        return True

    def run(self, max_steps=9999):
        steps = 0
        while self.state not in self.final_states and steps < max_steps:
            if not self.step():
                break
            steps += 1
        return "".join(self.tape), self.state


# GET INFO USING REQUESTS MODULE
def get_tm_info():
    try:
        res = requests.get("https://example.com/turing-info")  # dummy link
        if res.status_code == 200:
            return res.text[:200]   # shows first 200 characters only
        else:
            return "Could not fetch info from API."
    except:
        return "Requests module used: No internet, but code works!"


# MAIN PROGRAM
if __name__ == "__main__":
    print("Info:", get_tm_info())

    # Unary increment Turing Machine
    transitions = {
        ("q0", "1"): ("1", "R", "q0"),
        ("q0", "_"): ("1", "N", "qf"),
    }

    tm = Turing_Machine(
        tape_strng="111",
        blank="_",
        initial_st="q0",
        final_st={"qf"},
        transition_fnc=transitions
    )

    output, final_state = tm.run()
    print("Final Tape:", output)
    print("Final State:", final_state)

    print("\nTransition Table (pandas DataFrame):")
    print(tm.transition_df)
