```markdown
# 🧠 7. Program Structure & Best Practices
## Warehouse Opening + Closing Procedures 🏭🔒

## 🎯 PROGRAM = FACTORY WITH OPENING/CLOSING ROUTINE 🏭⏰

**Simple English**: Every program has **fixed structure** like factory daily routine:
```

9AM: Open gates → Load boxes → Do work → Save results → 5PM: Close gates

```

## PROGRAM ANATOMY 🏗️ (Fixed Skeleton)

```

🏭 FACTORY DAILY ROUTINE:
┌─────────────────────────────┐
│ 1. OPENING (main starts)    │ ← Program begins here!
├─────────────────────────────┤
│ 2. LOAD BOXES (variables)   │
├─────────────────────────────┤
│ 3. DO WORK (logic/robots)   │
├─────────────────────────────┤
│ 4. SHOW RESULTS (print)     │
├─────────────────────────────┤
│ 5. CLEANUP (main ends)      │ ← Program ends here!
└─────────────────────────────┘

```

## 1. MAIN ENTRY POINT 🚪 (Factory Front Door)

**Simple English**: **ONE special box** where computer **always starts reading**.

```

C/C++ Factory Door:
int main() {              // "Hey computer, start here!"
// Do factory work
return 0;            // "Work done, shut down!"
}

Python Factory Door:
if __name__ == "__main__":  \# "If running this file, start here!"
main()

```

**Why `return 0`?**:
```

0 = "Everything OK! 😊"
1 = "Something broke! 😱"

```

## 2. INPUT/OUTPUT 📥📤 (Factory Doors)

**Simple English**: **Gates** where data **comes in** and **goes out**.

```

📥 INPUT (Bring boxes into factory):

- User types numbers
- Read from file
- Get from database
- Receive from internet

📤 OUTPUT (Send boxes out):

- Show on screen
- Save to file
- Send to database
- Email results

```

**Finance Examples**:
```

📥 INPUT: "Enter shares: 100"
📥 INPUT: "Enter price: \$150.25"
📤 OUTPUT: "Total: \$15,025"

```

## 3. COMMENTS 💭 (Sticky Notes on Boxes)

**Simple English**: **Notes** that computer **ignores** but humans read.

```


# SINGLE LINE (Python): Quick note

total = shares * price  \# Calculate portfolio value

/* MULTI LINE (C++): Long explanation

* This function calculates compound interest
* using the formula: P(1+r)^n
*/
def compound_interest(principal, rate, years):

```

**Good Comment Examples**:
```

price = 150.25      \# Current AAPL price (Jan 2026)
TAX_RATE = 0.30     \# Federal tax rate 30%
if balance < 0:     \# Check for overdraft

```

## 4. ERROR HANDLING 🛡️ (Factory Safety Nets)

**Simple English**: **Catch problems** before factory explodes!

```

REAL LIFE: "If machine breaks, press EMERGENCY STOP"

PROGRAM: "If user enters bad data, show friendly error"

```

**Common Factory Problems**:
```

❌ User types "abc" instead of number
❌ File missing (stock data not found)
❌ Network down (API fails)
❌ Divide by zero (shares / 0)

```

**Safety Net Examples**:
```

Python (Simple):
try:
shares = int(input("Shares: "))
except:
print("❌ Please enter NUMBER!")
shares = 0

File Safety:
try:
data = open("stocks.txt")
except FileNotFoundError:
print("❌ Stock file missing!")

```

## 🏭 COMPLETE FACTORY DAILY ROUTINE

```

Python Finance Factory:
┌─────────────────────────────────────┐
│ if __name__ == "__main__":          │ 1. OPEN DOOR
├─────────────────────────────────────┤
│     \# INPUT (Load boxes)            │ 2. LOAD DATA
│     shares = int(input("Shares: ")) │
├─────────────────────────────────────┤
│     \# PROCESS (Do work)             │ 3. DO WORK
│     total = shares * 150.25         │
├─────────────────────────────────────┤
│     \# OUTPUT (Show results)         │ 4. SHOW RESULTS
│     print(f"Value: \${total}")       │
├─────────────────────────────────────┤
│     \# CLEANUP                       │ 5. CLOSE
│ except:                             │
│     print("Error handled!")         │
└─────────────────────────────────────┘

```

## BEST PRACTICES ✅ (Factory Rules)

```

🏭 FACTORY RULES EVERYONE MUST FOLLOW:

1. ONE WAY IN: Always use main() door
2. SHOW YOUR WORK: Print important steps
3. HANDLE BROKEN MACHINES: try/except safety nets
4. STICKY NOTES: Comment confusing steps
5. CLEAN BOX NAMES: shares, not x1 (clear!)
6. CONSTANTS IN BIG LETTERS: TAX_RATE = 0.30
7. SMALL JOBS: One robot = one simple task
```

## 💰 FINANCE FACTORY COMPLETE EXAMPLE

```

🏭 DAILY FINANCE ROUTINE:

1. OPEN: if __name__ == "__main__":
2. INPUT: shares = input_shares()
3. PROCESS: profit = calc_profit(shares, price)
4. DECIDE: if profit > 1000: buy_recommended()
5. OUTPUT: print_portfolio_summary()
6. CLOSE: return 0
```

## 💡 SUPER SIMPLE SUMMARY

```

🏭 PROGRAM = FACTORY WITH ROUTINE:
🚪 1 MAIN DOOR = Where computer starts
📥📤 INPUT/OUTPUT = Factory gates
💭 COMMENTS = Sticky notes (computer ignores)
🛡️ ERROR HANDLING = Safety nets

🏭 DAILY FLOW:
OPEN → LOAD BOXES → WORK → SHOW → CLEANUP → CLOSE

✅ ALWAYS: main() + try/except + clear comments!

```