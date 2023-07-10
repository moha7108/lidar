import json
from rplidar import RPLidar

RELEVANT_ANGLES = [270,90,356,180] #Front(270) Back(90) Left(360), right(180)
lidar = RPLidar('/dev/ttyUSB0')


#distance Calibration
front_raw_min, front_raw_max, front_dist_min, front_dist_max = 200, 500, 0,10
back_raw_min, back_raw_max, back_dist_min, back_dist_max  = 200, 500,0,10
left_raw__min, left_raw_max, left_dist_min, left_dist_max  = 200,500,0,10
right_raw_min, right_raw_max, right_dist_min, right_dist_max  = 200,500,0,10

def map_range(x, in_min, in_max, out_min, out_max):
  
  return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min 


if __name__=="main":
    
    print('Recording measurements... Press Ctrl+C to stop.')


    while True:
        try:
            # Fetch 10 measurements for the example
            for scan in lidar.iter_scans():

                relevant_out = {"Front": None, "Back": None, "Left":None, "Right":None}

                
                for measurement in scan:
                    quality, angle, distance = measurement
                    angle = int(angle)


                    # relevant_out = {"quality": quality, "angle": angle, "distance": distance}
                    # print(json.dumps(relevant_out))

                    if angle in RELEVANT_ANGLES:

                        if angle == 270:
                            orientation = "Front" 
                        elif angle == 90:
                            orientation = "Back"
                        elif angle == 180:
                            orientation = "Right"
                        elif angle == 356:
                            orientation = "Left"

                        relevant_out[orientation] = distance

                        # relevant_out = {"quality": quality, "angle": angle, "distance": distance}
                    
                print(json.dumps(relevant_out))

        except KeyboardInterrupt:
            print('Stopping.')
        lidar.stop()
        lidar.disconnect()