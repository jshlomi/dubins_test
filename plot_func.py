import numpy as np
import matplotlib.pyplot as plt
def plot_traj(car_speed_kph='70',
              turn_radius='-1',
             final_angle_deg='37',
             gravity_center_h='0.5',
             car_width='1.84'):
    car_speed_kph = float(car_speed_kph)
    total_distance = 94 #meters
    car_speed = (car_speed_kph*1000)/(3600.0) #meter/sec
    car_width = float(car_width)
    gravity_center_h = float(gravity_center_h)
    gravity = 9.8
    min_radius = ((car_speed**2)*(2*gravity_center_h))/(gravity*car_width)
    
    if turn_radius!='-1':
      min_radius = float(turn_radius)

    road_width = 3
    final_angle_deg = 90-float(final_angle_deg)
    final_angle = (2.0*np.pi)*(final_angle_deg/360.0)
    
    circle_center = [ road_width+min_radius*np.cos(np.pi/2-final_angle),
                     total_distance-min_radius*np.sin(np.pi/2-final_angle)]
    
    
    
    x1, y1, theta1 = road_width,total_distance,final_angle
    q1 = (x1, y1, theta1)
    
    fig,ax = plt.subplots(figsize=(45,40))
    
    
    ax.plot([circle_center[0],circle_center[0]-min_radius*np.cos(np.pi/2-final_angle)],
           [circle_center[1],circle_center[1]+min_radius*np.sin(np.pi/2-final_angle)],
           c='k')

    ax.plot([0,0],[0,total_distance],c='k')
    ax.plot([road_width*2,road_width*2],[0,total_distance],c='k')

    for q in [q1]:
        ax.scatter(q[0],q[1],c='r')
        ax.arrow(q[0],q[1],5*np.cos(q[2]),5*np.sin(q[2]),head_width=0.4)


    ax.plot( [circle_center[0]+min_radius*np.cos(x) for x in np.linspace(0,2*np.pi,100)]
              , [circle_center[1]+min_radius*np.sin(x) for x in np.linspace(0,2*np.pi,100)] )
    

    ax.set_xlim(-road_width,6*road_width)
    ax.set_ylim(-total_distance*0.2,total_distance*1.2)
    ax.set_aspect(1)
    plt.show()