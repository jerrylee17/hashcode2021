'''
num_of_intersections -> number of intersections
trafficInfo (object) : 
    (intersection_number, incoming_streets, road, time_it_is_on) (list) :
        intersection_number -> current intersection 
        incoming_streets -> the length of the amount of streets we are going to output
        road -> name of road
        time_it_is_on -> amount of time pre cycle it is on, if road is the only
                        road in the list, this means that the road is always green
                        else that means the road is on for x seconds before the
                        next road turns on
'''

def output(file, intersections):
    with open(file, "w") as outfile:
        # library id
        outfile.write(str(len(intersections))+'\n')
        for intersection in intersections:
            s = ''
            intersection_number = intersection.number
            s += str(intersection_number) + '\n'
            incoming_streets = len(intersection.cycle)
            s += str(incoming_streets) + '\n'
            for r in intersection.cycle:
                s += str(r[0]) + ' ' + str(r[1]) + '\n'
            outfile.write(s)