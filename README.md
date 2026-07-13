# MyGames

A small collection of beginner-friendly Python games built with **Pygame** and **Tkinter**.

## Games Included

| Folder | Game | Framework | Run Command |
|---|---|---|---|
| `space_alien_V1` | Alien Space Shooter | Pygame | `python alien_space.py` |
| `fightingGame` | 2-Player Fighting Game | Pygame | `python main.py` |
| `jumper` | Endless Runner | Pygame | `python main.py` |
| `shooterGame` | Target Shooter | Pygame | `python main.py` |
| `snakeTK` | Snake | Tkinter | `python snake.py` |
| `tiktaktokTK` | Tic-Tac-Toe | Tkinter | `python tiktaktok.py` |

## Requirements

- Python **3.10+**
- `pip`
- A desktop environment (these games open GUI windows)

Install dependencies:

```bash
pip install -r requirements.txt
```

## Quick Start

1. Clone the repo.
2. Install dependencies.
3. Open the game folder you want.
4. Run the script shown in the table above.

Example:

```bash
cd fightingGame
python main.py
```

> Important: run each game from inside its own folder so local asset paths (images/audio/fonts) load correctly.

## Controls

### Space Alien (`space_alien_V1`)
- Move: Arrow keys
- Shoot: `Space`
- Mega bullet: `C`
- Start: Click **Play** button

### Fighting Game (`fightingGame`)
- **Player 1 (Cat):**
  - Move: `A` / `D`
  - Jump: `W`
  - Attack: `K` / `L`
- **Player 2 (Skull):**
  - Move: Left / Right arrows
  - Jump: Up arrow
  - Attack: `N` / `M`

### Jumper (`jumper`)
- Jump: `Space`
- Start from menu: `Space`

### Shooter (`shooterGame`)
- Aim: Mouse
- Shoot / start: Left click

### Snake (`snakeTK`)
- Move: Arrow keys

### Tic-Tac-Toe (`tiktaktokTK`)
- Play: Mouse clicks
- Reset: `reset` button

## Project Notes

- This is a multi-game sandbox project focused on learning and experimenting.
- Code style and naming are intentionally simple and may vary between folders.
- Asset files are stored next to each game for easier local execution.

## Troubleshooting

- **`ModuleNotFoundError: No module named pygame`**
  - Run: `pip install -r requirements.txt`
- **Assets not loading (`No file ... found`)**
  - Make sure you are running the game from its own folder.
- **No game window appears**
  - Ensure you are running in a GUI-enabled environment (not a headless terminal).

## License

This project currently has no explicit license file.
