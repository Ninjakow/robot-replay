from record import Recorder
from log import Log
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--refresh_rate", "--rate", "-r", default=20, type=float,
                    help="Time interval between each data point in seconds")
parser.add_argument("--directory", "--dir", "-f", type=str, default="",
                    help="Directory to save log files")
parser.add_argument("--server", "--ip", type=str,
                    default="roborio-4774-frc.local", help="ip of the roborio")
parser.add_argument("--camera", "--cam", "-c", action="append", type=str,
                    help="ip of camera server")

args = parser.parse_args()

if args.camera is None:
    args.camera = ["http://10.47.74.36:1181/stream.mjpg",
                   "http://10.47.74.36:1182/stream.mjpg"]  # [0,1] testing

current_time = time.strftime("%H-%M-%S %d-%m-%y")
streams = [Recorder(args.directory + "cam" + str(num) + "-" + current_time +
                    ".mp4", stream, int(max(args.refresh_rate, 1)))
           for num, stream in enumerate(args.camera, start=1)]

logger = Log(4774)

if __name__ == "__main__":
    while True:
        start = time.monotonic()

        for stream in streams:
            stream.record()

        logger.log()

        elapsed = time.monotonic() - start
        if 1/args.refresh_rate - elapsed > 0:
            time.sleep(1/args.refresh_rate - elapsed)
