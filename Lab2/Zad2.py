import sys

def get_mean_size():

    total_size = 0
    file_count = 0

    for i, line in enumerate(sys.stdin):

        if i == 0:
            continue

        parts = line.split()

        if len(parts) >= 5:
            try:
                size = int(parts[4])
                total_size += size
                file_count += 1
            except ValueError:
                continue

    if file_count == 0:
        print("Не удалось определить размер файлов (возможно, каталог пуст)")
    else:
        mean_size = total_size / file_count
        print(f"Средний размер файла: {mean_size:.2f} байт")

if __name__ == '__main__':
    get_mean_size()