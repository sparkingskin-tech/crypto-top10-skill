---
name: crypto-top10
description: Run Top10 crypto daily/QA workflows using a stable wrapper script. Use when the user asks for 主流币日更、Top10看板、Top3机会、关键买卖区、成交量验证、链上巨鲸/机构/ETF视角、BTC/ETH/BNB深挖.
---

# Crypto Top10 Skill

## Run

Use the wrapper instead of calling service scripts directly.

```bash
python3 /Users/skin/Projects/量化/skills/crypto-top10/scripts/run.py daily
```

## Supported intents

- `brief`
- `daily`
- `full`
- `top10`
- `top3`
- `zones`
- `volume`
- `events`
- `whales`
- `institutions`
- `derivatives`
- `flows`
- `deep-btc`
- `deep-eth`
- `deep-bnb`

## Rules

- Distinguish spot-led moves from leverage-led moves.
- Always check whether move has volume support.
- If refresh fails and cached data exists, explicitly state that cache is being used.
