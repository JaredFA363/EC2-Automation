import os
import sys
import time
import requests


URL = os.getenv("MONITOR_URL") or (len(sys.argv) > 1 and sys.argv[1])
TIMEOUT = float(os.getenv("TIMEOUT", "5"))
RETRIES = int(os.getenv("RETRIES", "2"))
SLEEP_BETWEEN = float(os.getenv("SLEEP_BETWEEN", "1.5"))


if not URL:
    print("MONITOR_URL not provided. Set env var or pass as first arg.")
sys.exit(2)


last_exc = None
for attempt in range(1, RETRIES + 2):
    start = time.time()
    try:
        r = requests.get(URL, timeout=TIMEOUT)
        latency_ms = int((time.time() - start) * 1000)
        ok = r.status_code == 200
        print(f"attempt={attempt} status={r.status_code} latency_ms={latency_ms}")
        if ok:
            sys.exit(0)
    except Exception as e:
        last_exc = e
        print(f"attempt={attempt} error={e}")
    time.sleep(SLEEP_BETWEEN)


print(f"FAILED: {URL} - last_error={last_exc}")
sys.exit(1)