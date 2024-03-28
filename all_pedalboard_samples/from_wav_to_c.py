import os, json, soundfile

def generate_c_code(fp: str, frames: list, loop_point: int, nframes: int):
    pass

if __name__ == "__main__":
    files = os.listdir()
    loop_point_data = json.load(open("loop_points.json", "r"))
    for file in files:
        if file.endswith(".wav"):
            (x, y) = soundfile.read(file)
            assert(y)
            generate_c_code(file, )

