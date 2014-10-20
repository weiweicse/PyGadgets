import sys # for argument parsing
import codecs # decoding

source_encoding_types = ['cp932',
'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2',
'iso2022_jp_2004', 'iso2022_jp_3', 'iso2022_jp_ext',
'shift_jis', 'shift_jis_2004', 'shift_jisx0213',
'utf_8', 'utf_16'] # potential utf-32

target_encoding_type = 'utf_8'

"""
print file with filename using target encoding type,
try various encoding types.
"""
def convert(filename):
    for src_type in source_encoding_types:
        try:
            f = codecs.open(filename, 'r', encoding=src_type)
            lines = f.read()
            print lines.encode(target_encoding_type)
            break
        except UnicodeDecodeError:
            sys.stderr.write(src_type + " doesn't work.\n")
        except UnicodeEncodeError:
            print "Cannot convert to utf-8."

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '[Usage]: python convert.py filename'
        sys.exit()
    filename = sys.argv[1]
    convert(filename)
