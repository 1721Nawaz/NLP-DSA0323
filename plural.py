class FSM:
    def __init__(self):
        self.states = {}
        self.start_state = None
        self.current_state = None

    def add_state(self, name, transitions, is_final=False):
        self.states[name] = {"transitions": transitions, "is_final": is_final}
        if self.start_state is None:
            self.start_state = name

    def set_start(self, name):
        self.start_state = name

    def reset(self):
        self.current_state = self.start_state

    def process(self, char):
        if self.current_state and char in self.states[self.current_state]["transitions"]:
            self.current_state = self.states[self.current_state]["transitions"][char]
        else:
            self.current_state = None  # No valid transition

    def is_final(self):
        return self.current_state and self.states[self.current_state]["is_final"]


def pluralize_noun(noun):
    """
    A basic finite state machine to generate plural forms of nouns.
    """
  
    fsm = FSM()


    fsm.add_state("start", {"s": "ends_in_s", "y": "ends_in_y", "default": "default_plural"})
    fsm.add_state("ends_in_s", {}, is_final=True)  # Handles "glass" -> "glasses"
    fsm.add_state("ends_in_y", {}, is_final=True)  # Handles "party" -> "parties"
    fsm.add_state("default_plural", {}, is_final=True)  # Handles "cat" -> "cats"

   
    fsm.reset()
    last_char = noun[-1]
    if last_char in fsm.states["start"]["transitions"]:
        fsm.process(last_char)
    else:
        fsm.process("default")


    if fsm.current_state == "ends_in_s":
        return noun + "es"
    elif fsm.current_state == "ends_in_y":
        return noun[:-1] + "ies"
    elif fsm.current_state == "default_plural":
        return noun + "s"
    else:
        return noun  # No change if no rules apply



nouns = ["cat", "dog", "glass", "party", "bus", "box"]

for noun in nouns:
    plural = pluralize_noun(noun)
    print(f"Singular: {noun}, Plural: {plural}")
