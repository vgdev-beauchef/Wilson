class StoryState:
    def __init__(self, leyend, trigger, option, yes_fun, no_fun, yes_state, no_state):
        self.trigger = trigger
        self.leyend = leyend
        self.option = option
        self.yes_fun = yes_fun
        self.no_fun = no_fun
        self. next_yes_state = yes_state
        self. next_no_state = no_state