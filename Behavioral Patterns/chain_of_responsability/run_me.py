# -*- coding: UTF-8 -*-
class call_chain:

    def answer(self, call):

        answered_call = MachineAnswer(
            CommomAnswer(TechnicalAnswer())).answer(call)
        return answered_call


if __name__ == '__main__':

    from chain_of_responsability.customer_service import MachineAnswer, CommomAnswer, TechnicalAnswer
    from chain_of_responsability.call import Call

    call_hard = Call('hard')
    call_easy = Call('easy')
    call_medium = Call('medium')

    call_center = call_chain()

    answerd_call = call_center.answer(call_hard)

    print("Your call was answered in, {0} minutes by {1}! Complexity: {2}!".format(
        answerd_call.on_call,
        answerd_call.answered_by,
        answerd_call.complexity.upper()
    ))

    answerd_call = call_center.answer(call_easy)

    print("Your call was answered in, {0} minutes by {1}! Complexity: {2}".format(
        answerd_call.on_call,
        answerd_call.answered_by,
        answerd_call.complexity.upper()
    ))

    answerd_call = call_center.answer(call_medium)

    print("Your call was answered in, {0} minutes by {1}! Complexity: {2}".format(
        answerd_call.on_call,
        answerd_call.answered_by,
        answerd_call.complexity.upper()
    ))
