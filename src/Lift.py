'''Simple Lift'''

def stages_to_move(call_data):
    for i in range(len(call_data)):
        if call_data[i]['call']:
            if call_data[i]['floor'] > call_data[i]['current_state']:
                stages_count = call_data[i]['floor'] - call_data[i]['current_state']
                print('Stage : ',stages_count)
            else:
                print("Invalid Data for : ",call_data[i])
        else:
            if call_data[i]['floor'] < call_data[i]['current_state']:
                stages_count = call_data[i]['current_state'] - call_data[i]['floor']
                print('Stage : ', stages_count)
            else:
                print("Invalid Data for : ", call_data[i])

data = [{'call':True,'floor':4,'current_state':1},{'call':False,'floor':0,'current_state':4}]

stages_to_move(data)