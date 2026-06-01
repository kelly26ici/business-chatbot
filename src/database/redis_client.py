from upstash_redis import Redis
from src.config.settings import REDIS_URL, REDIS_TOKEN

redis = Redis(url=REDIS_URL, token=REDIS_TOKEN)