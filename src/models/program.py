
class Program:
    '''
    Training program.
    '''
    def __init__(self, name, duration, sessions_per_week, slots_per_session, content):
        self.name = name
        self.duration = duration
        self.sessions_per_week = sessions_per_week 
        self.slots_per_session = slots_per_session
        self.content = content

    def get_slot(self, program_week, week_session, slot_number):
        return self.content.loc[program_week, week_session, slot_number].to_dict()

    def get_slots(self, program_week, week_session):
        slots = []
        for s in range(1, self.slots_per_session+1):
            slots.append(self.get_slot(program_week, week_session, s))
        return slots
