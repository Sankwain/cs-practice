import sys
from stats import read_valid, average_by_city, warmest_city

lines = sys.stdin.read().splitlines()

valid_records = read_valid(lines)

non_empty_lines = [line for line in lines if line.strip()]
parsed_count = len(valid_records)
error_count = len(non_empty_lines) - parsed_count

warmest = warmest_city(valid_records)
averages = average_by_city(valid_records)
warmest_temp = averages[warmest]

print(parsed_count)
print(error_count)
print(f"{warmest_temp:.1f}")
