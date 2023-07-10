import json
from rplidar import RPLidar

RELEVANT_ANGLES = [0,90,180,270]

lidar = RPLidar('/dev/ttyUSB0')

print('Recording measurements... Press Ctrl+C to stop.')

while True:
    try:
        # Fetch 10 measurements for the example
        for scan in lidar.iter_scans():
            
            relevant_out={}

            for measurement in scan:
                quality, angle, distance = measurement

                if angle in RELEVANT_ANGLES:
                    relevant_out = {"quality": quality, "angle": angle, "distance": distance}
                
                    print(json.dumps(relevant_out))

    except KeyboardInterrupt:
        print('Stopping.')
    lidar.stop()
    lidar.disconnect()