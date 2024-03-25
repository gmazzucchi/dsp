import csv

AMPLITUDE_CUTOFF = 2**5
OUTFILE = "sample_22kHz5"

def normalize(data: list) -> list:
    return [int(elem * 32767 / AMPLITUDE_CUTOFF) for elem in data]


def dump_to_c(l):
    out = open(OUTFILE + ".c", "w+")
    out.write("#include \"" + OUTFILE + ".h\"\n\nint16_t " +
              OUTFILE + "[" + OUTFILE.upper() + "_SIZE] = {\n")
    for x in l:
        out.write(str(x) + ",\n")
    out.write("};\n")
    out.close()
    upfile = OUTFILE.upper()
    out = open(OUTFILE + ".h", "w+")
    out.write('''#ifndef ''' + upfile +'''_H
#define ''' + upfile + '''_H

#include <stdint.h>

#define ''' + upfile + '''_SIZE ''' + str(len(l)) + '''
#define ''' + upfile + '''_LOOP_POINT 4795

extern int16_t ''' + OUTFILE + '''[''' + upfile + '''_SIZE];

#endif // '''+ upfile +'''_H
''')


if __name__ == "__main__":
    input = open("sample22kHz.csv", "r")
    csvdata = csv.reader(input)
    data = []
    for r in csvdata:
        data.append(float(r[0]))
    nordata = normalize(data)
    dump_to_c(nordata)
