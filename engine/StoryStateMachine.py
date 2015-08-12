__author__ = 'Agustin Antoine'
__email__ = "antoineagustin@gmail.com"

import StoryState
from gfx import *

class StoryStateMachine:           


    def __init__(self, ui, log, ope, init_state):
        self.log_mod = log
        self.opt_mod = ope
        #self.inv_mod = inv
        #self.world = world
        self.ui = ui

        #self.dayLimit = dayLimit
        self.state = init_state

    def computeStoryState(self, current_time, step, x, y):
        if(not self.state==None and self.state.trigger(current_time, step, x, y)):
            self.log_mod.add_event(self.state.leyend)
            self.opt_mod.clearWindow()
            self.opt_mod.setOption(self.state.option[0], self.state.option[1], self.state.option[2])
            while 1:
                self.ui.draw()
                q = get_input()
                if q == 'y':
                    self.state.yes_fun()
                    self.state=self.state.next_yes_state
                    break
                elif q == 'n':
                    self.state.no_fun()
                    self.state=self.state.next_no_state
                    break
            self.opt_mod.clearWindow()
            self.opt_mod.setOption("", "", "")

    def checkIndividualStates(self, current_time, step, x, y, events):
        for s in events:
            if(s.trigger(current_time, step, x, y)):
                self.log_mod.add_event(s.leyend)
                self.opt_mod.clearWindow()
                self.opt_mod.setOption(s.option[0], s.option[1], s.option[2])
                while 1:
                    self.ui.draw()
                    q = InputMap.key(get_input())
                    if q == 'yes':
                        s.yes_fun()
                        break
                    elif q == 'no':
                        s.no_fun()
                        break
                self.opt_mod.clearWindow()
                self.opt_mod.setOption("", "", "")