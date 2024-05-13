import redis
from redis.commands.json.path import Path
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query
import time
import pandas as pd



r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# one_p = pd.read_csv("cf747a25-b6c6-46ea-b60e-81ce35ced1e3.csv",sep = ',')

# one_p["keywords"]

# schema = (
#     TextField("$.campaignId", as_name="campaignId"), 
#     TextField("$.keyword", as_name="keyword"), 
# )


rs = r.ft("idx:campaign")
# rs.dropindex("idx:campaign")
# rs.create_index(
#     schema,
#     definition=IndexDefinition(
#         prefix=["campaign:"], index_type=IndexType.JSON
#     )
# )

# for i in range(100000):
#     campaign = {
#         "campaignId": str(i),
#         "keyword": one_p["keywords"][i]
#     }
#     r.json().set("campaign:"+str(i), Path.root_path(), campaign)


# r.json().set("campaign:2", Path.root_path(), campaign2)
# r.json().set("campaign:3", Path.root_path(), campaign3)


start = time.time()
for i in range(10000):
    res = rs.search(
        Query("@kw:fire tv")
    )
end = time.time()

print("latency: "+str((end-start)))
