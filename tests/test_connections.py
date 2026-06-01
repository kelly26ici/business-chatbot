from src.database.supabase_client import supabase
from src.database.redis_client import redis

# Test Supabase
response = supabase.table("customers").select("*").execute()
print("Supabase connected:", response)

# Test Redis
redis.set("test", "hello")
value = redis.get("test")
print("Redis connected:", value)