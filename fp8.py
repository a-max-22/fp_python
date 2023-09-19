
def calc_dstance(speed_and_time, position, speed, time_passed):
    if position >= len(speed_and_time):
        return 0
    if speed is None:
        speed = speed_and_time[position]
        return calc_dstance(speed_and_time, position + 1, speed, time_passed)
    else:
        current_time = speed_and_time[position] 
        time_delta = current_time - time_passed
        distance_current = time_delta * speed
        return distance_current + calc_dstance(speed_and_time, position + 1, None, current_time) 

def odometer(speed_and_time):
    if len(speed_and_time) % 2 != 0: return None
    
    return calc_dstance(speed_and_time, 0, None, 0)


speed_and_time = [15,1,25,2,30,3,10,5]
kilometers = odometer(speed_and_time)
print(kilometers)
