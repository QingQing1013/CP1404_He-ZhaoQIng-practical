# CP1404 Practical 01 Solutions

This folder contains complete, beginner-friendly solutions for the exercises:

- `temperatures.py`
- `sales_bonus.py`
- `broken_score.py`
- `loops.py`
- `shop_calculator.py`
- `menus.py`
- `electricity_bill.py` (practice)
- `sequences.py` (extension)

## Boundary tests

### `sales_bonus.py`

| Sales | Expected bonus |
|---:|---:|
| 500 | $50.00 |
| 999.99 | $100.00 after rounding |
| 1000 | $150.00 |
| 2000 | $300.00 |
| -1 | Program ends |

### `broken_score.py`

| Score | Expected result |
|---:|---|
| -1 | Invalid score |
| 0 | Bad |
| 49.99 | Bad |
| 50 | Passable |
| 89.99 | Passable |
| 90 | Excellent |
| 100 | Excellent |
| 101 | Invalid score |

### `shop_calculator.py`

- A negative item count prints `Invalid number of items!` and asks again.
- A total of exactly $100 receives no discount.
- A total greater than $100 receives a 10% discount.
- Inputs `100`, `35.56`, and `3.24` produce `$124.92` after the discount.

Run a file in PyCharm by opening it, right-clicking in the editor, and choosing
**Run**, or use `python3 filename.py` in a terminal.
