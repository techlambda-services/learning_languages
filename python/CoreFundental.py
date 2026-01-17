

"""
## 1. LITERALS DEMO 📦
"""
def demo_literals():
    print("\n📦 1. LITERALS (No Memory Box Needed)Ishank")
    
    print("─" * 45)
    
    shares = 100                    # Integer literal
    rate = 0.0525                   # Float literal
    ticker = "AAPL"                 # String literal
    profitable = True               # Boolean literal
    
    print(f"  shares  = {shares:>5}   ← Integer Literal")
    print(f"  rate    = {rate:>7.4f}  ← Float Literal")
    print(f"  ticker  = '{ticker}'    ← String Literal")
    print(f"  profitable = {profitable} ← Boolean Literal")

"""
## 2. VARIABLES - STEP BY STEP 🏭
"""
def demo_variables():
    print("\n🏭 2. VARIABLES - Watch Boxes Fill!")
    print("─" * 45)
    
    # Step-by-step lifecycle
    balance = None
    print(f"  STEP 1: Empty    balance = {balance} @ {hex(id(balance))}")
    
    balance = 1000.50
    addr1 = id(balance)
    print(f"  STEP 2: Fill     balance = ${balance:,.2f} @ {hex(addr1)}")
    
    balance = 12500.75
    addr2 = id(balance)
    status = "✅ SAME BOX!" if addr1 == addr2 else "🔄 NEW BOX"
    print(f"  STEP 3: Change   balance = ${balance:,.2f} @ {hex(addr2)} {status}")

"""
## 3. CONSTANTS 🔒
"""
def demo_constants():
    print("\n🔒 3. CONSTANTS (UPPER_CASE = Don't Touch!)")
    print("─" * 45)
    
    TAX_RATE = 0.30
    MAX_SHARES = 1000
    
    print(f"  TAX_RATE    = {TAX_RATE} @ {hex(id(TAX_RATE))}")
    print(f"  MAX_SHARES  = {MAX_SHARES} @ {hex(id(MAX_SHARES))}")
    print("  👉 UPPER_CASE = Team contract: NEVER CHANGE!")

"""
## 4. KEYWORDS vs IDENTIFIERS 🚫✅
"""
def demo_keywords_identifiers():
    print("\n🚫✅ 4. KEYWORDS vs IDENTIFIERS")
    print("─" * 45)
    
    print("✅ YOUR LABELS (Valid Identifiers):")
    portfolio_value = 25000
    calc_roi = 0.12
    print(f"  portfolio_value = ${portfolio_value:,.0f}")
    print(f"  calc_roi        = {calc_roi:.1%}")
    
    print("\n🚫 FACTORY LABELS (Keywords - Cannot Use):")
    print("  if, for, True, False, return, class")

"""
## 5. DATA TYPES - BOX SIZES 📏
"""
def demo_data_types():
    import sys
    print("\n📏 5. DATA TYPES = Different Box Sizes")
    print("─" * 45)
    
    portfolio = {
        'shares': 100,
        'price': 150.25,
        'ticker': 'AAPL',
        'active': True
    }
    
    print("  Name     | Value | Type | Size | Address")
    print("  ─────────┼───────┼──────┼──────┼─────────")
    for name, value in portfolio.items():
        size = sys.getsizeof(value)
        print(f"  {name:<8} | {str(value):<5} | {type(value).__name__:<4} | {size:>3}B | {hex(id(value))}")

"""
## 6. COMPLETE FINANCE WAREHOUSE 🏢
"""
def demo_complete_portfolio():
    print("\n🏢 6. COMPLETE PORTFOLIO WAREHOUSE")
    print("─" * 45)
    
    # All concepts together
    TAX_RATE = 0.30
    shares = 150
    avg_price = 145.50
    current_price = 152.75
    
    total_cost = shares * avg_price
    current_value = shares * current_price
    profit = current_value - total_cost
    net_profit = profit * (1 - TAX_RATE)
    
    print(f"  Shares:         {shares:,}")
    print(f"  Avg Price:      ${avg_price:>8,.2f}")
    print(f"  Current Price:  ${current_price:>8,.2f}")
    print(f"  Total Cost:     ${total_cost:>9,.2f}")
    print(f"  Market Value:   ${current_value:>9,.2f}")
    print(f"  Gross Profit:   ${profit:>9,.2f} ({profit/total_cost:.1%})")
    print(f"  Net Profit:     ${net_profit:>9,.2f}")
    print(f"  TAX_RATE box:   {hex(id(TAX_RATE))}")

def main():
    print("# 🏭 MEMORY WAREHOUSE DEMO")
    print("# Run to SEE live memory addresses!")
    print("=" * 50)
    
    demo_literals()
    demo_variables()
    demo_constants()
    demo_keywords_identifiers()
    demo_data_types()
    demo_complete_portfolio()
    
    print("\n✅ WAREHOUSE READY!")
    print("📦 Boxes created, labeled, filled!")
    print("🔧 Next: OPERATORS manipulate box contents!")

if __name__ == "__main__":
    main()




