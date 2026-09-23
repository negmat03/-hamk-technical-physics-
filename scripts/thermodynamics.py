#!/usr/bin/env python3
"""
Thermodynamics Calculator — HAMK Technical Physics
===================================================
Covers:
  - Ideal Gas Law: pV = nRT
  - Heat transfer: Q = m·c·ΔT
  - Thermal expansion: ΔL = α·L₀·ΔT
  - Temperature conversion: °C ↔ K ↔ °F
"""

R = 8.314   # J/(mol·K)  — universal gas constant
g = 9.81    # m/s²

# Specific heat capacities [J/(kg·K)]
SPECIFIC_HEAT = {
    'water':    4186,
    'ice':      2090,
    'steam':    2010,
    'iron':      449,
    'copper':    385,
    'aluminium': 897,
    'glass':     840,
    'air':      1005,
}

# Linear thermal expansion coefficients [1/K]
ALPHA = {
    'steel':      12e-6,
    'aluminium':  23e-6,
    'copper':     17e-6,
    'glass':       9e-6,
    'concrete':   12e-6,
}


def celsius_to_kelvin(t_c):
    return t_c + 273.15

def kelvin_to_celsius(t_k):
    return t_k - 273.15

def celsius_to_fahrenheit(t_c):
    return t_c * 9/5 + 32


def ideal_gas(p=None, V=None, n=None, T_celsius=None):
    """
    Solve ideal gas law: pV = nRT
    Provide 3 known values. T in Celsius (converted to Kelvin internally).
    p [Pa], V [m³], n [mol], T_celsius [°C]
    """
    if T_celsius is not None:
        T = celsius_to_kelvin(T_celsius)
    else:
        T = None

    if p is None and V is not None and n is not None and T is not None:
        p = n * R * T / V
    elif V is None and p is not None and n is not None and T is not None:
        V = n * R * T / p
    elif n is None and p is not None and V is not None and T is not None:
        n = p * V / (R * T)
    elif T is None and p is not None and V is not None and n is not None:
        T = p * V / (n * R)
        T_celsius = kelvin_to_celsius(T)

    return {
        'p_Pa': p,
        'p_kPa': p / 1000 if p else None,
        'p_atm': p / 101325 if p else None,
        'V_m3': V,
        'V_L': V * 1000 if V else None,
        'n_mol': n,
        'T_K': T,
        'T_C': T_celsius
    }


def heat_transfer(material, mass_kg, delta_T):
    """
    Calculate heat Q = m·c·ΔT
    material: key from SPECIFIC_HEAT dict (or pass c directly as float)
    mass_kg [kg], delta_T [K or °C]
    Returns Q in Joules and kJ.
    """
    if isinstance(material, str):
        c = SPECIFIC_HEAT.get(material.lower())
        if c is None:
            raise ValueError(f"Material '{material}' not found. Available: {list(SPECIFIC_HEAT.keys())}")
    else:
        c = float(material)  # custom c value

    Q = mass_kg * c * delta_T
    return {'Q_J': Q, 'Q_kJ': Q / 1000, 'c': c, 'material': material}


def thermal_expansion_linear(material, L0_m, delta_T):
    """
    Linear thermal expansion: ΔL = α · L₀ · ΔT
    Returns elongation ΔL and final length L_f.
    """
    if isinstance(material, str):
        alpha = ALPHA.get(material.lower())
        if alpha is None:
            raise ValueError(f"Material '{material}' not found. Available: {list(ALPHA.keys())}")
    else:
        alpha = float(material)

    delta_L = alpha * L0_m * delta_T
    return {
        'delta_L_m': delta_L,
        'delta_L_mm': delta_L * 1000,
        'L_final_m': L0_m + delta_L,
        'alpha': alpha
    }


def print_section(title):
    print(f"\n{'='*45}")
    print(f"  {title}")
    print('='*45)


if __name__ == '__main__':
    print("THERMODYNAMICS CALCULATOR — HAMK Technical Physics")

    # Example 1: Ideal gas — find pressure
    print_section("Example 1: Ideal Gas Law")
    print("  2 mol of gas at 25°C in a 50 L container → find pressure")
    r = ideal_gas(n=2, V=0.05, T_celsius=25)
    print(f"  Pressure: {r['p_Pa']:.1f} Pa = {r['p_kPa']:.2f} kPa = {r['p_atm']:.3f} atm")
    print(f"  Temperature: {r['T_C']}°C = {r['T_K']:.2f} K")

    # Example 2: Heat transfer
    print_section("Example 2: Heat Transfer")
    print("  Heating 2 kg of water from 20°C to 100°C")
    r2 = heat_transfer('water', mass_kg=2, delta_T=80)
    print(f"  Q = {r2['Q_J']:.0f} J = {r2['Q_kJ']:.2f} kJ")
    print(f"  (c_water = {r2['c']} J/kg·K)")

    # Example 3: Thermal expansion
    print_section("Example 3: Thermal Expansion")
    print("  Steel rail L₀=10 m, ΔT=40°C")
    r3 = thermal_expansion_linear('steel', L0_m=10, delta_T=40)
    print(f"  ΔL = {r3['delta_L_mm']:.3f} mm")
    print(f"  Final length: {r3['L_final_m']:.6f} m")

    # Temperature conversions
    print_section("Temperature Conversion Table")
    print(f"  {'°C':>8}  {'K':>10}  {'°F':>10}")
    print(f"  {'-'*32}")
    for tc in [-40, 0, 20, 37, 100, 373]:
        print(f"  {tc:>8.1f}  {celsius_to_kelvin(tc):>10.2f}  {celsius_to_fahrenheit(tc):>10.2f}")

    print("\nAvailable materials for heat_transfer():")
    for k, v in SPECIFIC_HEAT.items():
        print(f"  '{k}': c = {v} J/(kg·K)")
    print("\nAvailable materials for thermal_expansion_linear():")
    for k, v in ALPHA.items():
        print(f"  '{k}': α = {v:.1e} /K")
