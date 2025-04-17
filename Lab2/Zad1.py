import os

def get_summary_rss(ps_output_file_path: str) -> str:
    total_rss = 0
    with open(ps_output_file_path, 'r') as file:
        lines = file.readlines()[1:]

        for line in lines:
            columns = line.split()
            rss_kb = int(columns[5])
            total_rss += rss_kb
    return convert_to_human_readable(total_rss * 1024)

def convert_to_human_readable(size_bytes: int) -> str:
    units = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    unit_index = 0

    while size_bytes >= 1024 and unit_index < len(units) - 1:
        size_bytes /= 1024
        unit_index += 1

    return f"{size_bytes:.2f} {units[unit_index]}"

if __name__ == '__main__':
    ps_output_file_path = 'output_file.txt'

    if os.path.exists(ps_output_file_path):
        result = get_summary_rss(ps_output_file_path)
        print(f"Суммарный объем потребляемой памяти: {result}")
