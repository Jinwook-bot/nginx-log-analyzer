
import sys
import re
from collections import Counter

# Nginx 기본 access.log 형식 분석
log_pattern = re.compile(
    r'^(?P<ip>\S+) \S+ \S+ \[[^\]]+\] '
    r'"(?P<request>[^"]*)" (?P<status>\d{3})'
)

total = 0
skipped = 0

status_counts = Counter()
ip_counts = Counter()
path_counts = Counter()
error_404_ips = Counter()

# 로그 데이터를 한 줄씩 읽기
for line in sys.stdin:
    match = log_pattern.match(line)

    if not match:
        skipped += 1
        continue

    total += 1

    ip = match.group("ip")
    status = int(match.group("status"))
    request = match.group("request").split()

    path = request[1] if len(request) >= 2 else "unknown"

    status_counts[status] += 1
    ip_counts[ip] += 1
    path_counts[path] += 1

    if status == 404:
        error_404_ips[ip] += 1

# 결과 출력
print("\n===== NGINX LOG ANALYSIS =====")

print(f"\nTotal requests: {total}")
print(f"Skipped lines: {skipped}")

print("\n[HTTP Status Codes]")
for status, count in sorted(status_counts.items()):
    print(f"{status}: {count}")

print("\n[Top 5 Client IPs]")
for ip, count in ip_counts.most_common(5):
    print(f"{ip}: {count} requests")

print("\n[Top 5 Requested URLs]")
for path, count in path_counts.most_common(5):
    print(f"{path}: {count} requests")

if total > 0:
    client_errors = sum(
        count for status, count in status_counts.items()
        if 400 <= status < 500
    )

    server_errors = sum(
        count for status, count in status_counts.items()
        if 500 <= status < 600
    )

    print("\n[Error Rates]")
    print(f"4xx: {client_errors / total * 100:.2f}%")
    print(f"5xx: {server_errors / total * 100:.2f}%")

print("\n[Repeated 404 Detection]")
found = False

for ip, count in error_404_ips.most_common():
    if count >= 5:
        print(f"CHECK: {ip} generated {count} 404 errors")
        found = True

if not found:
    print("No IP with 5 or more 404 errors")

print("\n===== ANALYSIS COMPLETE =====")
