# Coffee Machine Simulator

A command-line coffee machine simulator built using Python.

## Features
- Supports espresso, latte, and cappuccino
- Coin-operated payment system
- Resource tracking
- Change calculation
- Resource refill functionality
- Generate machine usage report

## Workflow
- User selects a drink
- Machine checks if enough resources are available
- User inserts coins
- Payment is validated
- Resources are deducted after successful purchase
- Drink is served

## Additional Commands
- `report` → Displays current machine resources
- `refill` → Refills machine resources
- `off` → Turns off the machine

## Limitations
- Uses a simplified machine resource system
- Does not validate invalid coin inputs

## How to Run

```bash
python coffee_machine.py
```