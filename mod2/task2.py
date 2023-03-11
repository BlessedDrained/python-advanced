from statistics import mean
import sys


def get_file_size_from_bytes(b):
    kib = float(1000)
    mib = float(kib ** 2)
    gib = float(kib ** 3)
    tb = float(kib ** 4)

    if b < kib:
        return '{0} B'.format(b)
    elif kib <= b < mib:
        return '{0:.2f} KiB'.format(b / kib)
    elif mib <= b < gib:
        return '{0:.2f} MiB'.format(b / mib)
    elif gib <= b < tb:
        return '{0:.2f} GiB'.format(b / gib)
    elif tb <= b:
        return '{0:.2f} TB'.format(b / tb)


def get_mean_file_size(files_info):
    try:
        mean_file_size = mean([float(x.split()[4]) for x in files_info])
        return get_file_size_from_bytes(mean_file_size)
    except:
        return -1


if __name__ == '__main__':
    data = sys.stdin.readlines()[1:]
    print(get_mean_file_size(data))
