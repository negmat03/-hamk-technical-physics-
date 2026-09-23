#!/usr/bin/env python3
"""
Kinematics Solver — HAMK Technical Physics
===========================================
Solves MRU (uniform motion) and MRUA (uniformly accelerated motion) problems.
Given any 3 of the 5 kinematic variables, finds the remaining 2.

Variables:
  s  = displacement [m]
  v0 = initial velocity [m/s]
  v  = final velocity [m/s]
  a  = acceleration [m/s²]
  t  = time [s]
"""

import math


def solve_kinematics(s=None, v0=None, v=None, a=None, t=None):
    """
    Solve for missing kinematic variables.
    Provide exactly 3 known values; the function finds the other 2.
    Pass None for unknowns.
    """
    knowns = {k: val for k, val in zip('sv0vat', [s, v0, v, a, t]) if val is not None}
    results = {'s': s, 'v0': v0, 'v': v, 'a': a, 't': t}

    # v = v0 + a*t
    if results['v'] is None and results['v0'] is not None and results['a'] is not None and results['t'] is not None:
        results['v'] = results['v0'] + results['a'] * results['t']

    if results['v0'] is None and results['v'] is not None and results['a'] is not None and results['t'] is not None:
        results['v0'] = results['v'] - results['a'] * results['t']

    if results['a'] is None and results['v'] is not None and results['v0'] is not None and results['t'] is not None:
        results['a'] = (results['v'] - results['v0']) / results['t']

    if results['t'] is None and results['v'] is not None and results['v0'] is not None and results['a'] is not None and results['a'] != 0:
        results['t'] = (results['v'] - results['v0']) / results['a']

    # s = v0*t + 0.5*a*t²
    if results['s'] is None and results['v0'] is not None and results['a'] is not None and results['t'] is not None:
        results['s'] = results['v0'] * results['t'] + 0.5 * results['a'] * results['t'] ** 2

    # v² = v0² + 2*a*s
    if results['v'] is None and results['v0'] is not None and results['a'] is not None and results['s'] is not None:
        val = results['v0'] ** 2 + 2 * results['a'] * results['s']
        results['v'] = math.sqrt(abs(val)) * (1 if val >= 0 else -1)

    if results['s'] is None and results['v'] is not None and results['v0'] is not None and results['a'] is not None and results['a'] != 0:
        results['s'] = (results['v'] ** 2 - results['v0'] ** 2) / (2 * results['a'])

    return results


def free_fall(h=None, t=None, v=None, g=9.81):
    """
    Solve free fall problems.
    h = height [m], t = time [s], v = impact velocity [m/s], g = 9.81 m/s²
    """
    results = {'h': h, 't': t, 'v': v, 'g': g}

    if results['h'] is not None and results['t'] is None:
        results['t'] = math.sqrt(2 * results['h'] / g)
    if results['t'] is not None and results['h'] is None:
        results['h'] = 0.5 * g * results['t'] ** 2
    if results['t'] is not None and results['v'] is None:
        results['v'] = g * results['t']
    if results['v'] is not None and results['t'] is None:
        results['t'] = results['v'] / g
        results['h'] = 0.5 * g * results['t'] ** 2

    return results


def print_results(label, results):
    print(f"\n{'='*40}")
    print(f"  {label}")
    print(f"{'='*40}")
    labels = {
        's': 'Displacement   s',
        'v0': 'Initial vel.  v0',
        'v': 'Final vel.     v',
        'a': 'Acceleration   a',
        't': 'Time           t',
        'h': 'Height         h',
        'g': 'Gravity        g'
    }
    units = {'s': 'm', 'v0': 'm/s', 'v': 'm/s', 'a': 'm/s²', 't': 's', 'h': 'm', 'g': 'm/s²'}
    for key, val in results.items():
        if key == 'g':
            continue
        name = labels.get(key, key)
        unit = units.get(key, '')
        if val is not None:
            print(f"  {name} = {val:.4f} {unit}")
        else:
            print(f"  {name} = [could not solve]")
    print()


if __name__ == '__main__':
    print("KINEMATICS SOLVER — HAMK Technical Physics")
    print("=" * 40)

    # --- Example 1: MRUA — find final velocity and displacement ---
    # A car starts from rest (v0=0), accelerates at 3 m/s² for 8 seconds
    print("\nExample 1: Car accelerating from rest")
    print("  Given: v0=0 m/s, a=3 m/s², t=8 s")
    r1 = solve_kinematics(v0=0, a=3, t=8)
    print_results("MRUA Result", r1)

    # --- Example 2: Free fall ---
    # A ball dropped from 45 m height
    print("Example 2: Free fall from 45 m")
    print("  Given: h=45 m")
    r2 = free_fall(h=45)
    print_results("Free Fall Result", r2)

    # --- Example 3: Braking ---
    # A car at 90 km/h brakes to a stop over 50 m. Find deceleration.
    print("Example 3: Car braking")
    v_kmh = 90
    v_ms = v_kmh / 3.6
    print(f"  Given: v0={v_kmh} km/h ({v_ms:.2f} m/s), v=0 m/s, s=50 m")
    r3 = solve_kinematics(v0=v_ms, v=0, s=50)
    print_results("Braking Result", r3)

    print("\nTo use in your own problems, call:")
    print("  solve_kinematics(v0=..., a=..., t=...)")
    print("  free_fall(h=...)  or  free_fall(t=...)")
