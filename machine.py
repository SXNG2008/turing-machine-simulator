class TuringMachine:
    def __init__(self, tape_strng="", blank="_", initial_st="q0", final_st=None, transition_fnc=None):
        self.tape = list(tape_strng)
        self.blank = blank
        self.head = 0
        self.state = initial_st
        self.final_states = set(final_st) if final_st else set()
        self.transition_function = transition_fnc if transition_fnc else {}

    def step(self):
        """Execute one transition based on current state and tape symbol."""
        crnt_smbl = self.tape[self.head] if self.head < len(self.tape) else self.blank
        
        key = (self.state, crnt_smbl)
        if key not in self.transition_function:
            return False 

        new_symbol, direction, new_state = self.transition_function[key]

        # Write the symbol
        if self.head < len(self.tape):
            self.tape[self.head] = new_symbol
        else:
            self.tape.append(new_symbol)

        # Move the head
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

if __name__ == "__main__":
    # Example: Unary increment turing machin (ads 1 to the end)
    tm = TuringMachine(
        tape_strng="111",
        blank="_",
        initial_st="q0",
        final_st={"qf"},
        transition_fnc={
            ("q0", "1"): ("1", "R", "q0"),
            ("q0", "_"): ("1", "N", "qf"),
        }
    )

    output, final_state = tm.run()
    print("Final Tape:", output)
    print("Final State:", final_state)
