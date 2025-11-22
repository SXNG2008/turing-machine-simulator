class TuringMachine:
    def __init__(self, tape_string="", blank_symbol="_", initial_state="q0", final_states=None, transition_function=None):
        self.tape = list(tape_string)
        self.blank_symbol = blank_symbol
        self.head = 0
        self.state = initial_state
        self.final_states = set(final_states) if final_states else set()
        self.transition_function = transition_function if transition_function else {}

    def step(self):
        """Execute one transition based on current state and tape symbol."""
        current_symbol = self.tape[self.head] if self.head < len(self.tape) else self.blank_symbol
        
        key = (self.state, current_symbol)
        if key not in self.transition_function:
            return False  # No valid transition → halt

        new_symbol, direction, new_state = self.transition_function[key]

        # Write symbol
        if self.head < len(self.tape):
            self.tape[self.head] = new_symbol
        else:
            self.tape.append(new_symbol)

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

if __name__ == "__main__":
    # Example: Unary increment Turing Machine (adds 1 to the end)
    tm = TuringMachine(
        tape_string="111",
        blank_symbol="_",
        initial_state="q0",
        final_states={"qf"},
        transition_function={
            ("q0", "1"): ("1", "R", "q0"),
            ("q0", "_"): ("1", "N", "qf"),
        }
    )

    output, final_state = tm.run()
    print("Final Tape:", output)
    print("Final State:", final_state)

