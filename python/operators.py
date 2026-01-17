"""
## 1. ARITHMETIC OPERATORS 🧮
"""
def demo_arithmetic():
    print("\n🧮 1. MATH TOOLS (Arithmetic Operators)")
    print("─" * 45)
    
    shares = 100
    price = 150.25
    
    total = shares * price           # Multiply tool
    profit = total * 0.10            # 10% profit
    tax = profit * 0.30              # Tax tool
    net = profit - tax               # Subtract tool
    
    print(f"  shares * price   = {shares} * ${price} = ${total:,.0f}")
    print(f"  total * 0.10     = ${total:,.0f} * 10% = ${profit:,.0f}")
    print(f"  profit - tax     = ${profit:,.0f} - ${tax:,.0f} = ${net:,.0f}")

"""
## 2. COMPARISON OPERATORS ⚖️
"""
def demo_comparison():
    print("\n⚖️  2. JUDGE TOOLS (Comparison)")
    print("─" * 45)
    
    balance = 1250.75
    withdrawal = 1000
    
    print(f"  balance = ${balance}")
    print(f"  withdrawal = ${withdrawal}")
    print()
    
    print(f"  {balance} == {withdrawal} ? {balance == withdrawal}")
    print(f"  {balance} >  {withdrawal} ? {balance > withdrawal}")
    print(f"  {balance} >= 1000     ? {balance >= 1000}")
    print(f"  {withdrawal} <= {balance} ? {withdrawal <= balance}")

"""
## 3. LOGICAL OPERATORS 🎭
"""
def demo_logical():
    print("\n🎭 3. DECISION TOOLS (Logical)")
    print("─" * 45)
    
    profit = 1200
    tax_rate = 0.25
    balance = 500
    
    good_profit = profit > 1000
    low_tax = tax_rate < 0.30
    enough_balance = balance > 0
    
    buy = good_profit and low_tax and enough_balance
    
    print(f"  profit > 1000     = {good_profit}")
    print(f"  tax < 0.30        = {low_tax}")
    print(f"  balance > 0       = {enough_balance}")
    print()
    print(f"  ALL TRUE? (and)   = {buy}")

"""
## 4. ASSIGNMENT OPERATORS ➡️
"""
def demo_assignment():
    print("\n➡️  4. PUT TOOLS (Assignment)")
    print("─" * 45)
    
    total = 10000
    print(f"  total = 10000")
    
    total += 2500           # total = total + 2500
    print(f"  total += 2500    = {total:,.0f}")
    
    total *= 1.05           # total = total * 1.05
    print(f"  total *= 1.05    = {total:,.0f}")
    
    total -= 500            # total = total - 500
    print(f"  total -= 500     = {total:,.0f}")

"""
## 5. EXPRESSION vs STATEMENT 🎯
"""
def demo_expression_statement():
    print("\n🎯 5. EXPRESSION vs STATEMENT")
    print("─" * 45)
    
    price = 150
    shares = 100
    
    # Expression (gives value)
    value = price * shares
    print(f"  EXPRESSION: price * shares = {price} * {shares} = {value}")
    
    # Statement (does action)
    total = price * shares
    print(f"  STATEMENT: total = price * shares  ← SAVED IN BOX!")

"""
## 🏢 COMPLETE FINANCE WORKFLOW
"""
def demo_complete():
    print("\n🏢 6. COMPLETE FINANCE WORKFLOW")
    print("─" * 45)
    
    TAX_RATE = 0.30
    shares = 150
    buy_price = 145.50
    sell_price = 152.75
    
    # Math operators
    cost = shares * buy_price
    revenue = shares * sell_price
    gross_profit = revenue - cost
    
    # Comparison operators
    profitable = gross_profit > 0
    good_return = (gross_profit / cost) > 0.05
    
    # Logical operators
    buy_recommended = profitable and good_return
    
    # Assignment operators
    net_profit = gross_profit * (1 - TAX_RATE)
    
    print(f"  Shares:      {shares}")
    print(f"  Buy Price:   ${buy_price}")
    print(f"  Sell Price:  ${sell_price}")
    print(f"  Gross P&L:   ${gross_profit:,.0f}")
    print(f"  Profitable:  {profitable}")
    print(f"  Good Return: {good_return}")
    print(f"  Buy?         {buy_recommended}")
    print(f"  Net Profit:  ${net_profit:,.0f}")

def main():
    print("# 🔧 OPERATORS - Tools for Memory Boxes")
    print("# Watch math, decisions, and assignments!")
    print("=" * 50)
    
    demo_arithmetic()
    demo_comparison()
    demo_logical()
    demo_assignment()
    demo_expression_statement()
    demo_complete()
    
    print("\n✅ OPERATORS READY!")
    print("👑 Next: Control Flow = Boss of the boxes!")

if __name__ == "__main__":
    main()