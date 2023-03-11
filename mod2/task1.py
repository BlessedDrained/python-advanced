from os import path


def get_summary_rss(file_path: path) -> str:
    with open(file_path) as file:
        bytes = sum(map(float, [x.split()[4] for x in file.readlines()[1:]]))
    kib = float(1000)
    mib = float(kib ** 2)
    gib = float(kib ** 3)
    tb = float(kib ** 4)

    if bytes < kib:
        return '{0} B'.format(bytes)
    elif kib <= bytes < mib:
        return '{0:.2f} KiB'.format(bytes / kib)
    elif mib <= bytes < gib:
        return '{0:.2f} MiB'.format(bytes / mib)
    elif gib <= bytes < tb:
        return '{0:.2f} GiB'.format(bytes / gib)
    elif tb <= bytes:
        return '{0:.2f} TB'.format(bytes / tb)


if __name__ == '__main__':
    print(get_summary_rss('output_file.txt'))
