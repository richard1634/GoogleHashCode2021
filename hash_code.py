
import bisect


def solution():
    counter = 0
    my_dict = {}
    car_dict = {}
    car_counter = 0
    with open('exinput.txt') as f:
        line = f.readline()
        while line:
            if counter == 0:
                lines = line.split(" ")
                num_time = int(lines[0])
                num_intersections = int(lines[1])
                num_streets = int(lines[2])
                num_cars = int(lines[3])
                num_points = int(lines[4])

            elif counter >= 1 and counter <= int(num_streets):
                lines = line.split(" ")
                my_dict[lines[2]] = [(int(lines[0]),int(lines[1])),int(lines[3])]
            else:
                lines = line.split(" ")
                if lines[0].isdigit():
                    car_counter += 1
                    for line in lines[1:]:
                        if car_counter not in car_dict:
                            car_dict[car_counter] = [line.strip()]
                        else:
                            car_dict[car_counter].append(line.strip())                    
                else:
                    for line in lines:
                        car_dict[car_counter].append(line.strip()) 
            line = f.readline()
            counter += 1
            
    f.close()
##    print(length,num_intersections,num_streets,num_cars,num_points)
    print(my_dict)
    print(car_dict)

    
    # streets with no wait time or only 1 in-degree
    no_waits = {}
    always_green = set()  
    for k,v in my_dict.items():
        coming_from,in_degree = my_dict[k][0]
        if in_degree not in no_waits:
            no_waits[in_degree] = 1
        else:
            no_waits[in_degree] += 1
    for key in no_waits.keys():
        if no_waits[key] == 1:
            always_green.add(key)
   # print(always_green)

    car_queue = []
    for key,value in car_dict.items():
                         #car_num #curr street idx time
        city_name = car_dict[key][0].strip()
       # print(city_name)
        car_queue.append((key, city_name,0, 0))

    total_intersections = set()
    while car_queue:
        # just go if no wait
       # print(car_queue)
        car = car_queue.pop(0)
        
        car_num, curr_street,idx,time = car
        curr_street = curr_street.strip()
        
        #print(my_dict[curr_street][0][1])
        
        if my_dict[curr_street][0][1] in always_green:
            
            if my_dict[curr_street][0][1] not in total_intersections:
                total_intersections.add(my_dict[curr_street][0][1])
                
            length = len(car_dict[car_num])

          #  print("turn light on at: " + str(my_dict[curr_street][0][1]),car_queue)
            
            if idx + 1 < length:
                
                street_name = car_dict[car_num][idx+1].strip()
                L = my_dict[street_name][1]
                if num_time >= time + L:
                    city_name = car_dict[car_num][idx+1].strip()
                    car_queue.append((key,city_name,idx+1, time + L))
            else:
                L = my_dict[street_name][1]
                print("arrived", time+L)

        else:
            # play with lighting options
         #   print("turn light on at: " + str(my_dict[curr_street][0][1]))
            if my_dict[curr_street][0][1] not in total_intersections:
                total_intersections.add(my_dict[curr_street][0][1])
            if idx + 1 < length:
                
                street_name = car_dict[car_num][idx+1].strip()
                L = my_dict[street_name][1]
                if num_time >= time + L:
                    city_name = car_dict[car_num][idx+1].strip()
                    car_queue.append((key,city_name,idx+1, time + L))
            else:
                print("arrived")
        print(car_queue)
                
       # print(total_intersections)
                                
                                
                    

            
        
     
    

solution()
