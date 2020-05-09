import time

unix_time = time.time()
loc_time = time.localtime()
utc_time = time.gmtime()
readable_time = time.asctime()

print('unix time', unix_time)
print('本地時間',loc_time)
print('世界標準時間', utc_time)
print('可閱讀時間', readable_time)

tmp_str = time.strftime('year:%y, %m/%d', loc_time)
print(tmp_str)