from airtest.core.api import *


class BetPage:
    tingzhong_template = Template()
    frog_template = Template()

    bet_button_template = Template()

    money_button_template = Template()
    ok_button_template = Template()

    def __init__(self):
        pass

    def bet(self, chance):
        touch(self.tingzhong_template)

        touch(self.frog_template)

        bet_button = find_all(self.bet_button_template)
        bet_button = sorted(bet_button, key=lambda x: x['result'][0])
        if chance == 0:
            touch(bet_button[0])
        else:
            touch(bet_button[1])

        touch(self.money_button_template)

        touch(self.ok_button_template)
