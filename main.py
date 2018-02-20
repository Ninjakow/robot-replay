from record import Recorder
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--refresh_rate', '-r', default=0.1, type=float, help="Time interval between each data point in seconds")
parser.add_argument("--directory", "--dir", "-f", type=str, help="Directory to save log files")

args = parser.parse_args()
server = "roborio-4774-frc.local"

if args.directory is None:
    args.directory = "replays/testing/"

main_camera = Recorder(args.directory + "main_cam.avi", "http://10.47.74.36:1181/stream.mjpg", 1 / args.refresh_rate)  # 1 / args.refresh_rate)
vision_camera = Recorder(args.directory + "vision_cam.avi", "http://10.47.74.36:1182/stream.mjpg", 1 / args.refresh_rate)

if __name__ == "__main__":
    while True:
        start = time.monotonic()

        main_camera.record()
        vision_camera.record()

        elapsed = time.monotonic() - start
        if args.refresh_rate - elapsed > 0:
            time.sleep(args.refresh_rate - elapsed)
