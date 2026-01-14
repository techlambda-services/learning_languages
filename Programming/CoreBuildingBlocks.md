```markdown
# 🧠 2. Core Building Blocks
## Simple English "Memory Warehouse" 🏭📦

## 🎯 EVERYTHING IS A BOX IN MEMORY WAREHOUSE! 🏭

**Simple English**: Computer memory = giant warehouse full of **empty boxes**. Programming = **labeling boxes** and **putting things inside**.

```

🏭 MEMORY WAREHOUSE:
Box \#1234  Box \#1238  Box \#1240
[EMPTY]   [EMPTY]    [EMPTY]

```

## 1. LITERALS 📦 (Ready-Made Things - No Box Needed!)

**Simple English**: Numbers/words written **directly in your sentence**. No need to create box first.

```

Your sentence: "I have 100 shares worth \$150"
📦 100  ← Ready-made number (LITERAL)
📦 \$150 ← Ready-made number (LITERAL)
📦 "shares" ← Ready-made word (LITERAL)

```

**Examples**:
```

42       ← Number box (integer)
3.14     ← Decimal box (float)
"USD"    ← Word box (string)
true     ← Yes/No box (boolean)

```

```

✅ SIMPLE: shares = 100     (100 is ready-made number)
❌ WRONG: shares = box1    (box1 needs to be created first)

```

## 2. VARIABLES 🏷️ (Labeled Empty Boxes)

**Simple English**: **Empty box with name tag**. Later you can put something inside.

```

BEFORE:                    AFTER:
┌─────────┐                ┌─────────┐
│ EMPTY   │ balance        │ 1000.50 │ balance
└─────────┘                └─────────┘
Box \#1234                   Box \#1234 (same box!)

```

**Naming Rules** (Like naming your pet):
```

✅ GOOD NAMES: my_balance, total_shares, calc_profit
✅ OK NAMES:   balance, shares, price
❌ BAD NAMES:  b, x, y (what do they mean?)

```

**Two Styles**:
```

Python Style: total_shares    (snake_case - words separated by _ )
Java Style:  totalShares     (camelCase - words stuck together)

```

## 3. CONSTANTS 🔒 (Locked Boxes - Don't Touch!)

**Simple English**: Box with **PADLOCK**. Put value once, **never change**.

```

TAX_RATE = 0.30
↑
🔒 LOCKED FOREVER!

┌─────────┐
│  0.30   │ TAX_RATE
│ [LOCKED]│
└─────────┘

```

**Always use BIG LETTERS**:
```

TAX_RATE = 0.30     (Good - everyone knows "don't change")
tax_rate = 0.30     (Confusing - looks like normal variable)

```

## 4. KEYWORDS 🚫 (Factory Labels - Don't Use!)

**Simple English**: **Pre-printed labels** made by Python factory. You **cannot use** for your boxes.

```

✅ YOUR LABELS: my_balance, calc_profit, is_good
🚫 FACTORY LABELS: if, for, True, False, return

❌ WRONG: if = 100     (if is factory label!)
✅ GOOD:  my_if = 100  (your own label)

```

**Common Factory Labels**: `if`, `for`, `True`, `False`, `return`, `class`

## 5. IDENTIFIERS 🆔 (Your Custom Box Labels)

**Simple English**: **Names YOU create** for your boxes. Follow these rules:

```

✅ YES YOU CAN:

- Start with letter or _ : balance, _hidden
- Use letters, numbers, _ : total_shares2026
- Any length: my_very_long_portfolio_name_is_here

❌ NO YOU CAN'T:

- Start with number: 1st_share ❌
- Use spaces: my balance ❌
- Use -: my-balance ❌
- Use factory labels: if, for ❌

```

## 6. DATA TYPES 📦 (Box Sizes)

**Simple English**: Different **box sizes** for different things:

```

┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    100      │    │   150.25    │    │   AAPL      │
│   shares    │    │   price     │    │   ticker    │
│   [NUMBER]  │    │  [DECIMAL]  │    │   [WORD]    │
└─────────────┘    └─────────────┘    └─────────────┘

SMALL BOX   MEDIUM BOX    BIG BOX (for words)

```

**Finance Box Types**:
```

NUMBER box:  100 shares
DECIMAL box: \$150.25 price
WORD box:    "AAPL" ticker
YES/NO box:  true profitable

```

## 🏢 COMPLETE WAREHOUSE EXAMPLE

```

🏭 AFTER RUNNING PROGRAM:
┌──────────────┬──────────────┬──────────────┐
│ Box \#1234    │ Box \#1238    │ Box \#1240    │
├──────────────┼──────────────┼──────────────┤
│    100       │   150.25     │    AAPL      │
│   shares     │   price      │   ticker     │
│  [NUMBER]    │  [DECIMAL]   │   [WORD]     │
└──────────────┴──────────────┴──────────────┘

🔒 Plus locked box:
┌──────────────┐
│    0.30      │ TAX_RATE
│   [LOCKED]   │
└──────────────┘

```

## 💡 SUPER SIMPLE SUMMARY

```

📦 LITERALS = Ready-made things you write directly
🏷️ VARIABLES = Empty boxes you label
🔒 CONSTANTS = Locked boxes (BIG LETTERS)
🚫 KEYWORDS = Factory labels (don't touch)
🆔 IDENTIFIERS = Your names (follow rules)
📦 DATA TYPES = Box sizes

🏭 MAGIC: Same box number = SAME BOX!
Just change what's inside = SUPER SMART!

```