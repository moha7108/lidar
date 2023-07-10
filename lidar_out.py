import json
from rplidar import RPLidar

lidar = RPLidar('/dev/ttyUSB0')

try:
    print('Recording measurements... Press Ctrl+C to stop.')
    # Fetch 10 measurements for the example
    for i, measurement in enumerate(lidar.iter_measurements()):
        if i > 10:
            break
        print(json.dumps(measurement))
except KeyboardInterrupt:
    print('Stopping.')
lidar.stop()
lidar.disconnect()