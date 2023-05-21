from pytrends.request import TrendReq
import seaborn
# for styling
seaborn.set_style("darkgrid")

kw = "python" 
pt = TrendReq(hl="en-US", tz=360)   # en-US
# pt.build_payload([kw], timeframe="all")
# rt = pt.related_topics()
# rq = pt.related_queries()
# rq = pt.suggestions("python")
rq = pt.get_historical_interest(kw, year_start=2018, month_start=1, day_start=1, hour_start=0, year_end=2023, month_end=2, day_end=1, hour_end=0, cat=0, geo='', gprop='', sleep=0)
print (rq)
# print(rq[kw]["top"])
