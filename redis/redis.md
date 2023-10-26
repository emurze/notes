# Redis


## Types

* String
* List
* Set 
* Hash
* Zset


## String

* As Generator - conn.incr('article:')
* cache.get()


## Set

* zset without score system used in (votes, likes) for single or plular 


## Zset

* recommendation system for single or plural
* cache system with where popular at top, but unpopular at bottom
if limit exceeded then unpopular will be deleted


## Hash

* single - just 1 hash
* plural - set of hashes as db


## Commands


### String

* conn.get(key) 
* conn.set(key, value)
* conn.del(key) 
* conn.incr(key)


### Set

* conn.sadd( set , data)
* conn.srem( set , data)
* conn.smembers( set )
* conn.sismember( set , data)


### Zset

* conn.zadd( zset , {key: score})
* conn.zscore( zset , key)
* conn.zincrby( zset , key, score)
* conn.zrange( zset , start, stop)
* conn.zinterstore( zset , { zset : .5}) - use aggregate
* conn.zremrangebyrank( zset , 20_000, -1)
* conn.zcard( zset ) - count


### Hash (DB)

* conn.hmset( hash , {})
* conn.hmset( hash , {'votes': 2}) - Update
* conn.hmget( hash , key_1, key_2)
* conn.hgetall( hash )

### Clean

* conn.expire(key, 60)
* conn.delete(*keys)


## Conclusion

* We should optimize QuerySets | Rows using Redis
* Popular cache system using zset Redis with Limit, 
conn.zremrangebyrank( zset , 20_000, -1), 
conn.zinterstore( zset , { zset : .5})
* Likes, Votes on article using Redis
* Recommendation systems single or plural using Redis
* Always clean cache via Limit and conn.zcard() using Redis
* Don't cache all pages
