```markdown
# 🧠 6. Advanced Paradigms (Part 2)
## Math Robots + Type Safety Checkers ➗🛡️

## 🎯 FUNCTIONAL = MATH ROBOTS (NEVER Change Boxes!) ➗✨

**Simple English**: **Math robots** that **copy your boxes**, do math, **give new boxes back**. **Your original boxes stay safe forever!**

```

🏭 NORMAL ROBOTS (Change your boxes 😱):
shares = 100
shares = shares * 2     \# YOUR BOX CHANGED!
print(shares)  \# 200 😱

➗ MATH ROBOTS (Copy + safe 😊):
shares = 100
new_shares = shares * 2  \# YOUR BOX STILL 100!
print(shares)  \# 100 😊

```

## PURE FUNCTIONS ➗ (Math Robot Rules)

```

MATH ROBOT RULES:
✅ Same input → ALWAYS same output
✅ Never changes YOUR boxes (immutable)
✅ No side effects (no printing inside robot)

def double_shares(shares):
return shares * 2     \# Pure! Safe!

double_shares(100)  \# Always returns 200

```

## MAP = "Copy + Transform Factory" 🔄

```

Array of shares:[^1][^2]

MAP FACTORY:
Input:[^2][^1]
Copy → Transform → New Array
↓
Output:   (Original safe!)[^1]

Original:   ← UNCHANGED! ✨[^2][^1]

```

## RECURSION 🔄 (Robot Calls Itself)

```

REAL LIFE: "Count backwards: 5→4→3→2→1→STOP"

def countdown(n):
if n == 0:
return "BLASTOFF!"    \# Base case (STOP)
print(n)
return countdown(n-1)    \# Robot calls itself!

countdown(5)

# 5, 4, 3, 2, 1, BLASTOFF!

```

## 🛡️ TYPING = SAFETY CHECKERS (Find Bugs Early!)

**Simple English**: **Grammar police** that check your boxes **before** or **during** robot work.

```

STATIC TYPING (Java) = CHECK BEFORE START:
int shares = 100        \# Grammar police: "OK, integer box"
shares = "AAPL"         \# 🚨 ERROR BEFORE RUNNING!

DYNAMIC TYPING (Python) = CHECK DURING WORK:
shares = 100           \# OK
shares = "AAPL"        \# 😱 CRASH during work!

```

## TYPING COMPARISON 🛡️⚡

```

┌─────────────────┬──────────────────────┬──────────────────────┐
│ Type    │ Check │ Example              │ Finance Use           │
├─────────┼───────┼──────────────────────┼──────────────────────┤
│ Static  │Before │ int shares = 100     │ Bank systems (SAFE)   │
│ Dynamic │During │ shares = 100         │ Analysis scripts (FAST)│
└─────────┴───────┴──────────────────────┴──────────────────────┘

```

```

STATIC (Java):
✅ Finds bugs BEFORE crash
✅ Faster robot work
❌ Must declare box type first
❌ Slower to write

DYNAMIC (Python):
✅ Super fast to write
✅ Flexible box changes
❌ Bugs found DURING crash
❌ Slower robot work

```

## 🏭 FUNCTIONAL WAREHOUSE (Safe Math!)

```

🏭 BEFORE MATH ROBOT:
┌─────────┐ ┌─────────┐
│ shares  │ │  price  │
│    │ │ [150.25]│
└─────────┘ └─────────┘

➗ MATH ROBOT WORKS:
[ROBOT copies → math → new box]
│
┌──────────────┐
│   total      │ 15025  ← NEW SAFE BOX!
└──────────────┘

🏭 AFTER (Originals safe!):
┌─────────┐ ┌─────────┐ ┌──────────────┐
│ shares  │ │  price  │ │   total      │
│    │ │ [150.25]│ │       │
└─────────┘ └─────────┘ └──────────────┘

```

## 💰 FINANCE MATH ROBOTS

```


# Pure robot (always same result)

def calc_return(principal, rate, years):
return principal * (1 + rate) ** years

# Safe transformation (map)

shares =[^1]
values = list(map(lambda s: s * 150, shares))

# Original shares safe![^1]

# Recursion (compound interest daily)

def compound_daily(principal, rate, days):
if days == 0:
return principal
return compound_daily(principal * (1 + rate/365), rate, days-1)

```

## 💡 SUPER SIMPLE SUMMARY

```

➗ FUNCTIONAL = MATH ROBOTS
✅ Copy your boxes (safe!)
✅ Always same input → same output
✅ map() = Copy + transform factory
✅ Recursion = Robot calls itself

🛡️ STATIC TYPING = Grammar police BEFORE work
🛡️ DYNAMIC TYPING = Grammar police DURING work

🏭 BEFORE: Robots change your boxes 😱
🏭 AFTER:  Math robots → New safe boxes 😊

🎯 FINANCE PERFECT: Pure profit calc, safe data transforms!

```