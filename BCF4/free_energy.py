import numpy as np
import math


def import_crd(file_name,dist_size,angle_size,_dist_min,_dist_max,_angle_min,_angle_max,num_traj):

    _dist_angle_matrix = np.zeros((_dist_max - _dist_min + 1, _angle_max - _angle_min + 1))
    with open (file_name, 'r') as fref:
        for i, line in enumerate(fref.readlines()):
            dist, angle = list(map(float,line.split()))
            _dist = int(dist/dist_size)
            _angle = int(angle/angle_size)
            if _dist >= _dist_min and _dist <= _dist_max and _angle >= _angle_min and _angle <= _angle_max:
                _dist_angle_matrix[_dist - _dist_min][_angle - _angle_min] += 1
            else:
                print("dist_angle is not enough")

    return _dist_angle_matrix


def output_energy(file_name_input,file_name_output,_dist_angle_matrix,dist_size,angle_size,_dist_min,_dist_max,_angle_min,_angle_max,num_traj):

    energy = []
    max_point = np.amax(_dist_angle_matrix)
    _max_point = np.log(max_point/num_traj)*0.00198*330 #kB in kcal/mol = 1.38*10^-23*6.022*10^23*0.000238 
    print(_max_point)

    with open (file_name_input, 'r') as fref:
        for i, line in enumerate(fref.readlines()):
            dist, angle = list(map(float,line.split()))
            _dist = int(dist/dist_size)
            _angle = int(angle/angle_size)
            if _dist >= _dist_min and _dist <= _dist_max and _angle >= _angle_min and _angle <= _angle_max:
                energy.append(-np.log(dist_angle_matrix[_dist - _dist_min][_angle - _angle_min]/num_traj)*0.00198*330 + _max_point) 
            else:
                print("dist_angle is not enough")

    
    with open (file_name_output,"w") as fout:
        for i in range(len(energy)):
            fout.write(str(energy[i])+"\n")



if __name__ == '__main__':
    #crd_filename="dist_angle_all_OXX50-TLN100.dat"
    #crd_filename="dist_angle_1-5_TLN180.dat"
    crd_filename="dist_angle_all_OXX1_OXX50-TLN100.dat"
    output_filename="energy.dat"
    dist_size_in_ang = 0.05
    angle_size_in_deg = 2.0
    dist_range = [3.0,18.0]
    angle_range = [0.0,180.0]
    num_traj_total = 50000
    dist_min = int(dist_range[0]/dist_size_in_ang),
    dist_max = int(dist_range[1]/dist_size_in_ang),
    angle_min = int(angle_range[0]/angle_size_in_deg),
    angle_max = int(angle_range[1]/angle_size_in_deg),
    parms = {
            'dist_size' : dist_size_in_ang,
            'angle_size' : angle_size_in_deg,
            '_dist_min' : int(dist_range[0]/dist_size_in_ang),
            '_dist_max' : int(dist_range[1]/dist_size_in_ang),
            '_angle_min' : int(angle_range[0]/angle_size_in_deg),
            '_angle_max' : int(angle_range[1]/angle_size_in_deg),
            'num_traj' : num_traj_total
    }

    dist_angle_matrix = import_crd(crd_filename,**parms)
    output_energy(crd_filename,output_filename,dist_angle_matrix,**parms) 

