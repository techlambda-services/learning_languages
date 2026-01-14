# `programming-fundamentals-operators.md`

```markdown
# 🧠 3. Operators and Symbols
## Tools That Play With Your Memory Boxes 🔧🎮

## 🎯 OPERATORS = TOOLS FOR BOX CONTENTS 🛠️

**Simple English**: Operators are like **TOOLS** that take things from boxes, **do work**, and **put results back** in new boxes.

```

🏭 MEMORY WAREHOUSE BEFORE:
┌─────────┐ ┌─────────┐
│   100   │ │  150.25 │
│ shares  │ │  price  │
└─────────┘ └─────────┘

🔧 + TOOL: 100 + 150.25 = 250.25 (NEW BOX CREATED!)

```

## 1. ARITHMETIC OPERATORS 🧮 (Math Tools)

**Simple English**: Tools that do **basic math** on box contents.

```

┌────────────┬──────────────────────┬──────────────────────┐
│ Tool │ Name      │ What it does       │ Finance Example      │
├──────┼────────────┼────────────────────┼──────────────────────┤
│ +    │ Addition  │ Add box contents   │ shares + price       │
│ -    │ Subtract │ Take away          │ profit - tax         │
│ *    │ Multiply │ Repeated addition  │ shares * price       │
│ /    │ Divide   │ Split evenly       │ profit / shares      │
│ %    │ Modulo   │ Remainder          │ day % 5 = 0 (Friday) │
└──────┴────────────┴────────────────────┴──────────────────────┘

```

**Live Warehouse Example**:
```

BEFORE:                    TOOL WORK:              AFTER:
┌─────────┐ ┌─────────┐    🔧 * TOOL              ┌──────────────┐
│   100   │ │  150.25 │ → 100 * 150.25 → 15025  │   15025.0    │
│ shares  │ │  price  │                        │   total      │
└─────────┘ └─────────┘                        └──────────────┘

```

## 2. COMPARISON OPERATORS ⚖️ (Judge Tools)

**Simple English**: Tools that **compare** box contents and give **YES/NO** answer.

```

┌────────────┬──────────────────────┬──────────────────────┐
│ Tool │ Name      │ Question Asked     │ Finance Example      │
├──────┼────────────┼────────────────────┼──────────────────────┤
│ ==   │ Equal     │ Are they same?     │ price == target?     │
│ !=   │ Not Equal│ Are they different?│ ticker != "JUNK"?    │
│ >    │ Greater  │ Is left bigger?    │ profit > 1000?       │
│ <    │ Less     │ Is left smaller?   │ loss < 500?          │
│ >=   │ Greater/ │ Is left bigger/eq? │ balance >= 0?        │
│ <=   │ Less/eq  │ Is left smaller/eq?| rate <= 0.10?        │
└──────┴────────────┴────────────────────┴──────────────────────┘

```

**Result = YES/NO Box**:
```

price = 152     target = 150
152 > 150 ?  →  [YES]  (True box created!)

```

## 3. LOGICAL OPERATORS 🎭 (Decision Tools)

**Simple English**: Tools that **combine YES/NO answers** from comparison tools.

```

┌────────────┬──────────────────────┬──────────────────────┐
│ Tool │ Name      │ What it does       │ Finance Example          │
├──────┼────────────┼────────────────────┼──────────────────────────┤
│ and  │ AND      │ ALL must be YES    │ profit > 1000 AND tax < 0.3 │
│ or   │ OR       │ AT LEAST ONE YES   │ buy OR sell              │
│ not  │ NOT      │ Flip YES to NO     │ NOT (loss > 1000)        │
└──────┴────────────┴────────────────────┴──────────────────────┘

```

**Truth Table** (AND example):
```

A       B      A and B
YES    YES     YES
YES    NO      NO
NO     YES     NO
NO     NO      NO

```

## 4. ASSIGNMENT OPERATORS ➡️ (Put Tools)

**Simple English**: Tools that **PUT RESULTS** back into boxes.

```

┌────────────┬──────────────────────┬──────────────────────┐
│ Tool │ Name      │ What it does       │ Example               │
├──────┼────────────┼────────────────────┼───────────────────────┤
│ =    │ Assign   │ Put in empty box   │ total = 15025         │
│ +=   │ Add/Assign│ Add AND put back  │ total += 100  (total=total+100) │
│ -=   │ Sub/Assign│ Subtract AND put  │ balance -= tax        │
│ *=   │ Mul/Assign│ Multiply AND put  │ shares *= 2           │
│ /=   │ Div/Assign│ Divide AND put    │ avg_price /= shares   │
└──────┴────────────┴────────────────────┴──────────────────────┘

```

## 5. SYMBOLS 🏷️ (Grammar Rules)

**Simple English**: **Punctuation marks** that tell Python **where sentences end**.

```

;     End sentence (C/Java, Python uses NEW LINE)
{}    Group boxes together (code block)
()    Hold arguments (group things)

# Note (ignored by computer)

""    Word box boundaries

```

## EXPRESSION vs STATEMENT 🎯

```

EXPRESSION = GIVES VALUE (like math problem)
price * shares          → 150 * 100 = 15000 (VALUE)

STATEMENT = DOES ACTION (like command)
total = price * shares  → PUT 15000 in total box (ACTION)

```

## 🏢 COMPLETE WAREHOUSE WORKFLOW

```

🏭 START: Empty Warehouse
┌─────────┐ ┌─────────┐
│ shares  │ │  price  │
│    │ │ [150.25]│
└─────────┘ └─────────┘

🔧 STEP 1: Math Tool (*)
total = shares * price
┌──────────────┐
│    15025     │ ← NEW BOX!
│    total     │
└──────────────┘

🔧 STEP 2: Compare Tool (>)
is_good = total > 10000
┌─────────┐
│  True   │ ← YES/NO BOX!
│ is_good │
└─────────┘

🔧 STEP 3: Decision Tool (and)
buy = is_good and tax_low
┌─────────┐
│  True   │
│   buy   │
└─────────┘

```

## 💡 SUPER SIMPLE SUMMARY

```

🔧 MATH TOOLS: +, -, *, /, % (calculator)
⚖️  COMPARE TOOLS: ==, !=, >, < (judge)
🎭 DECISION TOOLS: and, or, not (combine yes/no)
➡️  PUT TOOLS: =, +=, -= (save results)
🏷️  GRAMMAR: ; {} () \# "" (punctuation)

🎯 EXPRESSION = Answer   |  STATEMENT = Command
150*100 = 15000         |  total = 150*100

```