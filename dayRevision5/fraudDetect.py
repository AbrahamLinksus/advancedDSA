import sys
from collections import deque

def main():
    # DUPLICATE: hash map txnId -> timestamp of first seen
    seen_txns = {}          # txnId -> first-seen timestamp

    # RATE_LIMIT: per-user deque of timestamps
    user_txn_times = {}     # userId -> deque of timestamps

    # MONEY_MULE: per-user deque of (timestamp, recipient) pairs
    user_recipients = {}    # userId -> deque of (ts, recipient)

    # STRUCTURING: per-user deque of timestamps for sub-50000 txns
    user_struct_times = {}  # userId -> deque of timestamps

    # Alert counters
    counts = {
        "DUPLICATE":   0,
        "RATE_LIMIT":  0,
        "MONEY_MULE":  0,
        "STRUCTURING": 0,
    }

    alerts = []  # collect all alert lines in order

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        parts = line.split()
        if len(parts) != 5:
            continue

        txn_id, user_id, recipient, amount_str, ts_str = parts
        amount = float(amount_str)
        ts     = float(ts_str)

        # ----------------------------------------------------------------
        # 1. DUPLICATE — same txnId within 5 seconds of first occurrence
        # ----------------------------------------------------------------
        if txn_id in seen_txns:
            if ts - seen_txns[txn_id] <= 5:
                alerts.append(f"DUPLICATE {txn_id}")
                counts["DUPLICATE"] += 1
            else:
                # Outside the window: treat this as a fresh first-seen
                seen_txns[txn_id] = ts
        else:
            seen_txns[txn_id] = ts

        # ----------------------------------------------------------------
        # 2. RATE_LIMIT — more than 20 txns by a user within 60 seconds
        # ----------------------------------------------------------------
        if user_id not in user_txn_times:
            user_txn_times[user_id] = deque()

        q = user_txn_times[user_id]
        # Evict entries outside the 60-second window
        while q and ts - q[0] > 60:
            q.popleft()

        q.append(ts)

        if len(q) > 20:
            alerts.append(f"RATE_LIMIT {txn_id}")
            counts["RATE_LIMIT"] += 1

        # ----------------------------------------------------------------
        # 3. MONEY_MULE — more than 50 unique recipients within 3600 secs
        # ----------------------------------------------------------------
        if user_id not in user_recipients:
            user_recipients[user_id] = deque()

        rq = user_recipients[user_id]
        # Evict entries outside the 3600-second window
        while rq and ts - rq[0][0] > 3600:
            rq.popleft()

        rq.append((ts, recipient))

        # Count unique recipients in the current window
        unique_recips = {r for _, r in rq}
        if len(unique_recips) > 50:
            alerts.append(f"MONEY_MULE {txn_id}")
            counts["MONEY_MULE"] += 1

        # ----------------------------------------------------------------
        # 4. STRUCTURING — 10+ txns under 50000 by a user within 1800 secs
        # ----------------------------------------------------------------
        if amount < 50000:
            if user_id not in user_struct_times:
                user_struct_times[user_id] = deque()

            sq = user_struct_times[user_id]
            # Evict entries outside the 1800-second window
            while sq and ts - sq[0] > 1800:
                sq.popleft()

            sq.append(ts)

            if len(sq) >= 10:
                alerts.append(f"STRUCTURING {txn_id}")
                counts["STRUCTURING"] += 1

    # --- Output ---
    for alert in alerts:
        print(alert)

    print(f"Duplicate Alerts: {counts['DUPLICATE']}")
    print(f"Rate Limit Alerts: {counts['RATE_LIMIT']}")
    print(f"Money Mule Alerts: {counts['MONEY_MULE']}")
    print(f"Structuring Alerts: {counts['STRUCTURING']}")


if __name__ == "__main__":
    main()