from stats import read_valid, warmest_city, average_by_city
import sys

lines = sys.stdin.read().splitlines()

valid_records = read_valid(lines)

parsed_count = len(valid_records)
error_count = len(lines) - parsed_count

warmest = warmest_city(valid_records)
averages = average_by_city(valid_records)
warmest_temp = averages[warmest]

print(parsed_count)
print(error_count)
print(f"{warmest_temp:.1f}")
