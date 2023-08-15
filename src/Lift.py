'''Simple Lift'''

# 1 Simple lift with Up and Down Functionality
#  Assumptions:
# when program runs lift will be on 0 floor.
# user will input int floor only 1-10 will be supported.
# It will remember where it is and will ask for next value i.e floor number
# Once given it will go to that floor and remembers that floor and so on.
# Only valid values are expected for the sake of time

# current_floor = 0
# while True:
#     requested_floor = int(input('Enter go to floor:'))
#     if 0 < requested_floor <= 10:
#         if requested_floor > current_floor:
#             print(f'Going {requested_floor-current_floor} Floor Up!')
#         elif requested_floor < current_floor:
#             print(f'Going {current_floor-requested_floor} Floor Down!')
#         else:
#             print('Invalid Floor Requested!!')
#         current_floor = requested_floor


# 2 Get data in below format and operate lift
data = [{'call': True, 'floor': 4, 'current_state': 1}, {'call': True, 'floor': 0, 'current_state': 4}]
def lift_processor(data):
    for d in data:
        if d['call']:
            if d['floor'] > d['current_state']:
                print(f"Going {d['floor'] - d['current_state']} Floor Up!")
            elif d['floor'] < d['current_state']:
                print(f"Going {d['current_state'] - d['floor']} Floor Down!")
            else:
                print('Same Floor')
# lift_processor(data)



# Dont know what was the question
def stages_to_move(call_data):
    for i in range(len(call_data)):
        if call_data[i]['call']:
            if call_data[i]['floor'] > call_data[i]['current_state']:
                stages_count = call_data[i]['floor'] - call_data[i]['current_state']
                print('Stage : ', stages_count)
            else:
                print("Invalid Data for : ", call_data[i])
        else:
            if call_data[i]['floor'] < call_data[i]['current_state']:
                stages_count = call_data[i]['current_state'] - call_data[i]['floor']
                print('Stage : ', stages_count)
            else:
                print("Invalid Data for : ", call_data[i])


# data = [{'call': True, 'floor': 4, 'current_state': 1}, {'call': False, 'floor': 0, 'current_state': 4}]
stages_to_move(data)
