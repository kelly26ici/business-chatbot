from src.database.supabase_client import supabase
from src.database.redis_client import redis
from src.models.customer import Customer
from datetime import datetime
import json

def get_customer(phone: str) -> Customer:
    # Check Redis first (fast)
    cached = redis.get(f"customer:{phone}")
    if cached:
        return Customer.from_dict(json.loads(cached))
    
    # Check Supabase (permanent)
    response = supabase.table("customers").select("*").eq("phone", phone).execute()
    
    if response.data:
        customer = Customer.from_dict(response.data[0])
    else:
        # Create new customer
        customer = Customer(phone=phone)
        supabase.table("customers").insert(customer.to_dict()).execute()
        print(f"New customer created: {phone}")
    
    # Cache in Redis
    redis.set(f"customer:{phone}", json.dumps(customer.to_dict()), ex=86400)
    
    return customer


def update_customer(customer: Customer):
    customer.last_seen = datetime.now().isoformat()
    
    # Update Supabase
    supabase.table("customers").update(customer.to_dict()).eq("phone", customer.phone).execute()
    
    # Update Redis cache
    redis.set(f"customer:{customer.phone}", json.dumps(customer.to_dict()), ex=86400)


def save_message(phone: str, role: str, content: str):
    supabase.table("conversations").insert({
        "phone": phone,
        "role": role,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }).execute()


def get_conversation_history(phone: str) -> list:
    # Check Redis first
    cached = redis.get(f"history:{phone}")
    if cached:
        return json.loads(cached)
    
    # Load from Supabase
    response = supabase.table("conversations")\
        .select("role, content")\
        .eq("phone", phone)\
        .order("timestamp")\
        .execute()
    
    history = [{"role": r["role"], "content": r["content"]} for r in response.data]
    
    # Cache in Redis
    redis.set(f"history:{phone}", json.dumps(history), ex=86400)
    
    return history