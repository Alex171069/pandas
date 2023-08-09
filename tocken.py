from pytrends.request import TrendReq
import seaborn
# for styling
seaborn.set_style("darkgrid")

kw = ['java', 'C#']
pt = TrendReq(hl="en-US", tz=360)   # en-US
pt.build_payload(kw, timeframe="all")
# rt = pt.related_topics()
# rq = pt.related_queries()
# rq = pt.suggestions("python")

# rq = pt.multirange_interest_over_time()
rq = pt.realtime_trending_searches()
print(rq)
# print(rq[kw]["top"])
