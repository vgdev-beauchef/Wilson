__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"

class StoryStateMachine:

    class StoryState:
        def __init__(self, leyend, trigger, option, yes_fun, no_fun, yes_state, no_state):
            self.trigger = trigger
            self.leyend = leyend
            self.option = option
            self.yes_fun = yes_fun
            self.no_fun = no_fun
            self. next_yes_state = yes_state
            self. next_no_state = no_state
            


    def __init__(self, ui, log, ope, inv, world, dayLimit, init_state):
        self.log_mod = log
        self.opt_mod = ope
        #self.inv_mod = inv
        #self.world = world
        self.ui = ui

        #self.dayLimit = dayLimit
        self.state = init_state

    def changeState(self, current_time, step, pos):
        if(not self.state==None and self.state.trigger(step, current_time, pos)):
            log.add_event(self.state.leyend)
            self.opt_mod.clearWindow()
            self.opt_mod.setOption(self.state.option[0], self.state.option[1], self.state.option[2])
            while 1:
                self.ui.draw()
                q = get_input()
                if q == 'y':
                    self.state.yes_fun()
                    self.state=self.next_yes_state
                    break
                elif q == 'n':
                    self.state.no_fun()
                    self.state=self.next_no_state
                    break
            self.opt_mod.clearWindow()
