import heapq
import os

def merge_segments(source_directory, destination_directory):
    segment_files = [f for f in os.listdir(source_directory) if f.startswith('segment')]
    segment_files.sort()

    file_handles = [open(os.path.join(source_directory, f), 'r') for f in segment_files]
    output_file = os.path.join(destination_directory, 'sorted_output.txt')

    with open(output_file, 'w') as output:
        heap = []
        for idx, fh in enumerate(file_handles):
            line = fh.readline().strip()
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

    for fh in file_handles:
        fh.close()


pwd = os.getcwd()

source_directory = os.path.join(pwd, 'data')
destination_directory = os.path.join(pwd, 'output')
merge_segments(source_directory, destination_directory)
print("sorted_output.txt file moved to destination")