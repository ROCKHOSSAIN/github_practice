def transaction_decorator(func):
    def wrapper(*args, **kwargs):
        print("--- Transaction Initiated ---")
        
        # ১. আসল ফাংশনটি রান করে তার রিটার্ন ভ্যালু একটি ভ্যারিয়েবলে রাখুন
        result = func(*args, **kwargs) 
        
        print("--- Transaction Completed ---")
        
        # ২. wrapper থেকে সেই রেজাল্টটি রিটার্ন করে দিন
        return result 
        
    return wrapper

@transaction_decorator
def make_payment(amount):
    print(f"Processing payment of ${amount}...")
    return "SUCCESS" # আসল রিটার্ন ভ্যালু

# রান করা যাক
status = make_payment(150)
print(f"Final Status: {status}")