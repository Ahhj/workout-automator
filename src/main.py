import pandas as pd
from gspread_pandas import Spread, Client

from . import authenticate

from .models import TrainingProgram, TrainingBlock
from .services import SessionGenerator

client = Client()

# TODO: clarify naming convention e.g. training/block/sessions
session_template_name = 'session_template'
program_name = 'powerbuilding1'
block_number = 1

# Program # TODO: refactor into class
program = client.open(program_name)
program_summary = dict(program.worksheet('Summary').get_all_values())

# Parse program header
num_weeks = int(program_summary['NumberOfWeeks'])
sessions_per_week = int(program_summary['SessionsPerWeek'])
slots_per_session = int(program_summary['SlotsPerSession'])
gpp_slots_per_session = int(program_summary['GppSlotsPerSession'])

program_data = pd.DataFrame(program.worksheet('Program').get_all_records())
program_data.set_index(['Week', 'Session', 'Slot'], inplace=True)

training_program = TrainingProgram(program_name, num_weeks, sessions_per_week, slots_per_session, data=program_data)
training_block = TrainingBlock(block_number, training_program)

# Session template
session_template = client.open(session_template_name)

session_generator = SessionGenerator(client, training_block, session_template)
session_generator.generate(7, 3)

# Generate program session
# for week in range(1, num_weeks+1):
#     for session in range(1, sessions_per_week+1):
#         generate_session(week, session)
