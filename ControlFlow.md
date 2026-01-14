```markdown
# 🧠 4. Control Flow
## The BOSS That Tells Boxes What To Do Next 👑🛤️

## 🎯 CONTROL FLOW = TRAFFIC COP FOR YOUR WAREHOUSE 👮‍♂️

**Simple English**: Normally computer reads boxes **top to bottom**. Control flow = **BOSS** that says "Skip this!" or "Repeat that!" or "Do this only if..."

```

🏭 WITHOUT BOSS (Boring straight line):
Box1 → Box2 → Box3 → Box4 → END

👑 WITH BOSS (Smart decisions):
Box1 → [CHECK?] → Box3 → [REPEAT?] → Box2 → END

```

## 1. CONDITIONALS if/else 🤔 (Decision Boxes)

**Simple English**: **"If this box says YES, do this. Else do that."**

```

REAL LIFE: "If balance > 0, withdraw money. Else show error."

```

**Box Diagram**:
```

profit = 1200    ↑
│ YES (1200 > 1000)
┌─────────────┐  │
│  BUY STOCK  │◄─┘
└─────────────┘
│ NO
▼
┌─────────────┐
│  HOLD CASH  │
└─────────────┘

```

**Syntax** (like English sentence):
```

if (condition is TRUE):
do this
else:
do that

```

**Finance Examples**:
```

if balance >= withdrawal:
balance = balance - withdrawal    \# Happy path
else:
print("❌ Insufficient funds!")

```

**Multiple Choices** (like traffic light):
```

if profit > 2000:
print("🚀 SUPER BUY!")
elif profit > 500:           \# elif = "else if"
print("✅ GOOD BUY")
else:
print("⏸️  HOLD")

```

## 2. LOOPS 🔄 (Repeat Tools)

**Simple English**: **"Keep doing this until box says STOP"**

### FOR LOOP (Known Number of Times)
```

REAL LIFE: "Check 100 shares one by one"

for each share in 100 shares:
check if profitable

```

**Box Diagram**:
```

shares = [100, 50, 75, 25, ...]  (100 boxes)
│
┌────▼────┐
│ CHECK   │ → Next → Next → ... → 100 times
│ SHARE   │
└────┬────┘
│
[DONE]

```

### WHILE LOOP (Until Condition Met)
```

REAL LIFE: "Keep withdrawing \$100 until balance < 100"

while balance > 100:
withdraw 100

```

**Box Diagram**:
```

balance = 1250
↑
│ YES (>100)
┌─────────────┐
│ withdraw 100│◄───
└─────────────┘    ▲
│           │ NO
▼           │
balance -= 100 ─┘

```

### DO-WHILE (Do First, Check Later)
```

REAL LIFE: "Withdraw once, THEN check if enough money"

do:
withdraw 100
while balance > 0

```

## 🛤️ COMPLETE CONTROL FLOW ROADMAP

```

🏭 START PROGRAM
│
┌────▼────┐
│ Load    │  ← Load boxes (variables)
│ Boxes   │
└────┬────┘
│
┌────▼────┐ YES
│ if      │────────┐
│ profit  │        │
│ > 1000? │        │ NO
└────┬────┘        ▼
│        ┌─────────────┐
▼        │ Print "HOLD"│
┌────▼────┐   └─────────────┘
│ FOR each│◄────┤
│ share   │     │
└────┬────┘     │
│          │
┌────▼────┐     │
│ Check   │     │
│ share   │     │
└────┬────┘     │
▼          │
[END]───────────┘

```

## 💰 FINANCE WORKFLOW EXAMPLE

```

if market_open:
for each stock in portfolio:
if stock.profit > target:
buy_more(stock)
else:
sell(stock)
else:
print("Market closed")

```

## 🎯 TRUTH TABLES (Boss Decision Rules)

```

AND RULE: ALL must be TRUE
┌──────┬──────┬────────┐
│ A    │ B    │ A and B│
├──────┼──────┼────────┤
│ TRUE │ TRUE │ TRUE   │
│ TRUE │ FALSE│ FALSE  │
│ FALSE│ TRUE │ FALSE  │
│ FALSE│ FALSE│ FALSE  │
└──────┴──────┴────────┘

OR RULE: AT LEAST ONE TRUE
┌──────┬──────┬────────┐
│ A    │ B    │ A or B │
├──────┼──────┼────────┤
│ TRUE │ TRUE │ TRUE   │
│ TRUE │ FALSE│ TRUE   │
│ FALSE│ TRUE │ TRUE   │
│ FALSE│ FALSE│ FALSE  │
└──────┴──────┴────────┘

```

## 💡 SUPER SIMPLE SUMMARY

```

👑 CONTROL FLOW = BOSS OF BOXES

🤔 IF/ELSE = "If box YES → do A, else do B"
🔄 FOR LOOP = "Do this X times"
🔄 WHILE = "Keep doing until box says STOP"
🛤️ PATH = Straight → Decision → Loop → END

🏭 WAREHOUSE BOSS SAYS:
"Check profit box → If good → Loop through shares → END"

```