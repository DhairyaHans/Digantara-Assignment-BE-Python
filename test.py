from datetime import datetime, timedelta

cur = datetime.strptime("2024-08-01", "%Y-%m-%d")
print(cur)

nxt_mnt = cur + timedelta(days=1)
print(nxt_mnt)