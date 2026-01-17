"""
## HIGH-LEVEL LANGUAGE DEMO (Python)
"""
def demo_high_level():
    print("\n🆙 HIGH-LEVEL LANGUAGE (Python)")
    print("─" * 45)
    
    # Readable, English-like
    principal = 10000
    rate = 0.05
    years = 5
    
    # Simple math (no complex syntax)
    amount = principal * (1 + rate) ** years
    
    print(f"  principal = ${principal:,}")
    print(f"  rate      = {rate:.1%}")
    print(f"  years     = {years}")
    print(f"  amount    = ${amount:,.2f}")
    print("  ✅ English-like, automatic memory!")

"""
## PSEUDOCODE → REAL CODE
"""
def demo_pseudocode_to_code():
    print("\n📝 PSEUDOCODE → PYTHON CODE")
    print("─" * 45)
    
    print("PSEUDOCODE:")
    print("  1. RECEIVE principal, rate, years")
    print("  2. IF principal <= 0 THEN ERROR")
    print("  3. amount = principal * (1+rate)^years")
    print("  4. DISPLAY amount")
    
    print("\n→ PYTHON:")
    def compound_interest(principal, rate, years):
        if principal <= 0:
            return "ERROR: Invalid principal"
        amount = principal * (1 + rate) ** years
        return amount
    
    result = compound_interest(10000, 0.05, 5)
    print(f"  Result: ${result:,.2f}")

"""
## LOW-LEVEL STYLE SIMULATION
"""
def demo_low_level_style():
    print("\n🔧 LOW-LEVEL STYLE (C-like Simulation)")
    print("─" * 45)
    
    # Simulate manual memory management
    print("  Manual memory (like C):")
    principal = 10000
    rate = 0.05
    years = 5
    
    # "Pointer" simulation
    principal_addr = id(principal)
    print(f"  principal address: {hex(principal_addr)}")
    
    # Manual calculation steps
    power = 1 + rate  # Step 1
    for i in range(years):
        power *= (1 + rate)
    amount = principal * power
    
    print(f"  amount = ${amount:,.2f}")
    print("  ⚠️  More complex, faster execution")

"""
## FLOWCHART EXECUTION SIMULATION
"""
def demo_flowchart():
    print("\n🗺️  FLOWCHART EXECUTION")
    print("─" * 45)
    
    print("Running flowchart logic:")
    print("  [START]")
    print("    ↓")
    print("  Input → Process → Decision → Output")
    
    # Flowchart simulation
    balance = 5000
    withdrawal = 6000
    
    print(f"  Balance: ${balance}")
    print(f"  Withdraw: ${withdrawal}")
    
    if withdrawal > balance:
        print("  ❌ DECISION: Insufficient funds!")
    else:
        print("  ✅ DECISION: Approved!")
        balance -= withdrawal
        print(f"  New balance: ${balance}")

def main():
    print("# 1. INTRODUCTION TO PROGRAMMING")
    print("# High-Level vs Low-Level + Algorithms")
    print("=" * 50)
    
    demo_high_level()
    demo_pseudocode_to_code()
    demo_low_level_style()
    demo_flowchart()
    
    print("\n🎯 READY FOR CORE BUILDING BLOCKS!")
    print("🏭 Next: Variables fill the memory warehouse!")

if __name__ == "__main__":
    main()