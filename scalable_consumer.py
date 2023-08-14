import os
import multiprocessing
import heapq

pwd = os.getcwd()

source_directory = os.path.join(pwd, 'data')
destination_directory = os.path.join(pwd, 'output')
output_file = 'final_output.txt'

def merge_segments(segment_files, output_file):
    file_handles = [open(file, 'r') for file in segment_files]
    with open(output_file, 'w') as output:
        heap = []
        for idx, file_handle in enumerate(file_handles):
            line = file_handle.readline().strip()
            if line:
                values = map(int, line.split())
                for value in values:
                    heapq.heappush(heap, (value, idx))

        while heap:
            value, file_idx = heapq.heappop(heap)
            output.write(f"{value}\n")
            next_line = file_handles[file_idx].readline().strip()
            if next_line:
                values = map(int, next_line.split())
                for value in values:
                    heapq.heappush(heap, (value, file_idx))

    for file_handle in file_handles:
        file_handle.close()


def process_segment(segment_file, output_file):
    merge_segments([segment_file], output_file)


if __name__ == '__main__':
    segment_files = [f for f in os.listdir(source_directory) if f.startswith('segment')]
    segment_files.sort()

    output_files = [os.path.join(destination_directory, f'output{i}.txt') for i in range(1, len(segment_files) + 1)]

    processes = []
    for segment_file, output_file in zip(segment_files, output_files):
        process = multiprocessing.Process(target=process_segment, args=(os.path.join(source_directory, segment_file), output_file))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    merge_segments(output_files, os.path.join(destination_directory, output_file))
    print("sorted files moved to destination")
