import os, json, soundfile

AMPLITUDE_CUTOFF = 2**5

def normalize(data: list) -> list:
    return [int(elem * 32767 / AMPLITUDE_CUTOFF) for elem in data]

def generate_c_code(fp: str, frames: list, loop_start: int, loop_stop: int):
    filename = "sample_22kHz_" + fp
    header = open(os.path.join("sample_headers", filename + ".h"), "w+")
    source = open(os.path.join("sample_sources", filename + ".c"), "w+")
    FP = fp.upper()
    attacco_frames = ','.join(str(x) for x in frames[:loop_start]) 
    corpo_frames =  ','.join(str(x) for x in frames[loop_start:loop_stop])
    header.write(f'''#ifndef SAMPLE_{FP}_22KHZ_H
#define SAMPLE_{FP}_22KHZ_H

#include <stdint.h>

#define SAMPLE_{FP}_22KHZ_ATTACCO_L {str(loop_start)}
#define SAMPLE_{FP}_22KHZ_CORPO_L {str(loop_stop - loop_start)}

extern int16_t sample_{fp}_22kHz_attacco[SAMPLE_{FP}_22KHZ_ATTACCO_L];
extern int16_t sample_{fp}_22kHz_corpo[SAMPLE_{FP}_22KHZ_CORPO_L];

#endif // SAMPLE_{FP}_22KHZ_H

''')
    source.write(f'''#include "{filename}.h"

int16_t sample_{fp}_22kHz_attacco[SAMPLE_{FP}_22KHZ_ATTACCO_L] = {{
    {attacco_frames}
}};

int16_t sample_{fp}_22kHz_corpo[SAMPLE_{FP}_22KHZ_CORPO_L] = {{
    {corpo_frames}
}};
''')

if __name__ == "__main__":
    files = os.listdir()
    loop_point_data = json.load(open("loop_points.json", "r"))
    for file in files:
        if file.endswith(".wav"):
            [fp, _] = file.split(".")
            (x, y) = soundfile.read(file)
            lp = loop_point_data[fp]["lp_start"]
            ls = loop_point_data[fp]["lp_stop"]
            generate_c_code(fp.replace("#", "_sharp"), normalize(x), lp, ls)

