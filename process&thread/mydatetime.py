#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from datetime import datetime, timedelta, timezone


def dt2timestamp(dt_str, tz_str):
    dt_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz = int(re.match(r'^UTC([+-]\d+):\d+$', tz_str).group(1))
    dt_utc = dt_dt.replace(tzinfo=timezone(timedelta(hours=tz)))
    return dt_utc.timestamp()

t1 = dt2timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t1)
