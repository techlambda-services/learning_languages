```markdown
# 🧠 5. Functions
## Worker Robots That Do Repeated Jobs 🤖🔄

## 🎯 FUNCTIONS = TRAINED WORKER ROBOTS 🤖

**Simple English**: Instead of telling computer **every step every time**, you **train a robot** once, then say **"Robot, do your job!"**

```

🏭 WITHOUT ROBOT (Repeat work 10 times):
calculate profit for AAPL
calculate profit for GOOG
calculate profit for TSLA
... (boring, 100 times!)

🤖 WITH ROBOT (Train once, use 100 times):
TRAIN ROBOT: "Hey robot, when I give shares + price, calculate profit"
USE ROBOT:  robot.calculate(AAPL)
robot.calculate(GOOG)
robot.calculate(TSLA)

```

## ROBOT PARTS 🏗️

```

def calculate_profit(shares, price):   ← Robot name + tools it needs
total = shares * price             ← Robot's job
profit = total * 0.10              ← Robot's job
return profit                      ← Give result back

result = calculate_profit(100, 150)    ← "Robot, do your job!"

```

**4 Robot Parts**:
```

1. ROBOT NAME: calculate_profit
2. INPUT TOOLS: shares, price (things robot needs)
3. JOB STEPS: total = shares * price
4. RESULT BOX: return profit (thing robot gives back)
```

## 🏭 WAREHOUSE ROBOT WORKFLOW

```

🏭 BEFORE CALLING ROBOT:
┌─────────┐ ┌─────────┐
│ shares  │ │  price  │
│    │ │ [150.25]│
└─────────┘ └─────────┘

🤖 ROBOT CALLED:
[ROBOT WORKSPACE]
┌─────────┐ ┌─────────┐ ┌──────────────┐
│ shares  │ │  price  │ │   profit     │ ← NEW BOX!
│    │ │ [150.25]│ │    1502.5    │
└─────────┘ └─────────┘ └──────────────┘

🏭 AFTER ROBOT FINISHED:
┌──────────────┐
│   profit     │ ← Robot gave back result box!
│    1502.5    │
└──────────────┘

```

## PARAMETERS 🛠️ (Robot Tools)

**Simple English**: **Things you give robot** to do its job.

```

robot.calculate_profit(shares=100, price=150)
↑↑
Tool1 Tool2

```

**Default Tools** (Robot has backup tools):
```

def calculate_profit(shares, price=150):  \# price has backup value
return shares * price * 0.10

robot.calculate_profit(100)              \# Uses backup price=150

```

## LOCAL vs GLOBAL BOXES 🌍📦

**Simple English**: **Robot has its own private boxes**. Main program boxes stay safe.

```

def robot_job():
my_box = 100          \# Robot's private box (disappears when done)
return my_box * 2

outside_box = 50         \# Main program's box (stays forever)
result = robot_job()     \# Robot works, outside_box unchanged!

```

```

🏭 MAIN WAREHOUSE:       🤖 ROBOT WORKSPACE:
┌─────────┐              ┌─────────┐ ┌──────────┐
│outside  │              │ my_box  │ │ result   │
│     │              │    │ │     │[^1]
└─────────┘              └─────────┘ └──────────┘
│                         │
UNCHANGED!               DESTROYED!

```

## COMPLETE FINANCE ROBOT FACTORY 🏭

```

ROBOT 1: Portfolio Calculator
def calc_portfolio(shares, price, tax_rate=0.30):
total = shares * price
profit = total * 0.10
net = profit * (1 - tax_rate)
return net

ROBOT 2: Risk Checker
def check_risk(total_value):
if total_value > 100000:
return "⚠️  HIGH RISK"
return "✅ SAFE"

FACTORY LINE:
portfolio1 = calc_portfolio(100, 150)    \# Robot 1
risk = check_risk(portfolio1)            \# Robot 2
print(risk)                              \# "✅ SAFE"

```

## ROBOT CALLING HIERARCHY 📊

```

🏭 MAIN PROGRAM (Boss)
│
┌────▼────┐
│CALL     │
│ROBOT1   │
└────┬────┘
│ RESULT
┌────▼────┐
│CALL     │
│ROBOT2   │
└────┬────┘
│
[FINAL RESULT]

```

## 💡 SUPER SIMPLE SUMMARY

```

🤖 FUNCTION = TRAINED WORKER ROBOT

1. TRAIN: def robot_name(tool1, tool2):
2. JOB:    do calculations with tools
3. GIVE BACK: return result_box
4. USE:    result = robot_name(100, 150)

🏭 ROBOT RULES:
✅ Robot gets COPIES of your boxes (safe!)
✅ Robot makes PRIVATE boxes (disappear after job)
✅ Robot gives back RESULT BOX
✅ Call robot 1000 times = same robot, different inputs!

🎯 BEFORE: Repeat 100 lines of code
🎯 AFTER: 1 robot + 100 calls = CLEAN!

```