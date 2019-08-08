from numpy import mat
from math import sin, cos, radians

def rot_y(de):
    t = mat([
                [ cos(de), 0, sin(de)],
                [ 0,       1,       0],
                [-sin(de), 0, cos(de)]
                                        ])
    return t


def rot_z(de):
    t = mat([
                [cos(de), -sin(de), 0],
                [sin(de),  cos(de), 0],
                [ 0,       0,       1]
                                        ])
    return t



def transf(x, y, z, a_degree, b_degree):
    a, b = radians(a_degree), radians(b_degree)
    nozzle_length = 3
    nozzle_offset = 7
    table_x_offset = 30
    table_z_offset = 48

    point_init = mat([nozzle_length, 0 , -nozzle_offset]).T

    point_after = rot_z(b) * rot_y(a) * point_init\
                    + mat([x, y, -z]).T

    axis_trans = mat([-table_x_offset, 0, table_z_offset]).T
    point_table = point_after + axis_trans

    print(point_table)



    vector = rot_z(b) * rot_y(a) * mat([1, 0, 0]).T
    print(vector)

    return point_table, vector
