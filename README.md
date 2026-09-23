# 📐 Introduction to Technical Physics — HAMK

> Study materials, formulas, solved exercises and Python scripts for the Technical Physics course at HAMK University of Applied Sciences.

---

## 📚 Topics Covered

| Topic | Formulas | Exercises | Script |
|-------|----------|-----------|--------|
| Kinematics | [📄](formulas/kinematics.md) | [📝](exercises/) | [🐍](scripts/kinematics_solver.py) |
| Dynamics | [📄](formulas/dynamics.md) | [📝](exercises/) | — |
| Thermodynamics | [📄](formulas/thermodynamics.md) | [📝](exercises/) | [🐍](scripts/thermodynamics.py) |

---

## 🗂️ Folder Structure

```
hamk-technical-physics/
├── formulas/          # Quick-reference formula sheets
│   ├── kinematics.md
│   ├── dynamics.md
│   └── thermodynamics.md
├── exercises/         # Solved and unsolved problems
│   └── template.md   # Use this for every new exercise
├── notes/             # Lecture notes
│   ├── units-and-conversions.md
│   └── lecture-template.md
└── scripts/           # Python calculators
    ├── kinematics_solver.py
    └── thermodynamics.py
```

---

## 🚀 Quick Start

### Run a Python script
```bash
# Solve a kinematics problem
python scripts/kinematics_solver.py

# Calculate ideal gas properties
python scripts/thermodynamics.py
```

### Add a new exercise
1. Copy `exercises/template.md`
2. Rename it (e.g. `exercises/ex01-free-fall.md`)
3. Fill in the given data, method and solution

---

## 🔢 Most Used Formulas

### Kinematics
$$v = v_0 + a \cdot t$$
$$s = v_0 t + \frac{1}{2} a t^2$$

### Dynamics
$$F = m \cdot a$$
$$W = F \cdot d \cdot \cos\theta$$

### Thermodynamics
$$pV = nRT \quad (R = 8.314 \text{ J/mol·K})$$
$$Q = m \cdot c \cdot \Delta T$$

---

## 📌 Study Tips

- Always **draw a diagram** before applying formulas
- Check **units** at every step (SI units)
- Use the **template** in `exercises/` for consistent problem-solving
- The Python scripts can **verify your manual calculations**

---

*HAMK — Hämeenlinna University of Applied Sciences*
