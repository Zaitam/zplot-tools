import numpy as np

def mean_and_ci(data, confidence=0.95):
    """Return the mean and confidence interval of the data."""
    a = np.array(data)
    mean = np.mean(a)
    sem = np.std(a, ddof=1) / np.sqrt(len(a))
    margin = sem * 1.96  # for ~95%
    return mean, mean - margin, mean + margin

def z_score(x, mean=None, std=None):
    """Compute z-score standardized values."""
    mean = mean if mean is not None else np.mean(x)
    std = std if std is not None else np.std(x)
    return (x - mean) / std


def to_scientific(value, precision=2):
    """
    Convert a number to scientific notation string with `precision` decimal places.
    Example: 0.00012 → '1.20e-4'
    """
    return f"{value:.{precision}e}"

def from_scientific(sci_str):
    """
    Parse a string in scientific notation and return the float value.
    Example: '1.20e-4' → 0.00012
    """
    try:
        return float(sci_str)
    except ValueError:
        raise ValueError(f"Invalid scientific notation: {sci_str}")

def molarity(moles, volume_liters):
    """Calculate molarity (mol/L) given moles and volume in liters."""
    return moles / volume_liters

def mass_from_moles(moles, molar_mass):
    """Calculate mass (g) given moles and molar mass (g/mol)."""
    return moles * molar_mass

def moles_from_mass(mass, molar_mass):
    """Calculate moles from mass and molar mass."""
    return mass / molar_mass

def percent_concentration(solute_mass_g, solution_mass_g):
    """% (w/w) concentration."""
    return (solute_mass_g / solution_mass_g) * 100

def ppm_concentration(solute_mass_mg, solution_mass_kg):
    """Parts per million (ppm) assuming mg in kg."""
    return (solute_mass_mg / solution_mass_kg)

def convert_mass(value, from_unit, to_unit):
    """
    Convert mass between 'mg', 'g', 'kg'.
    Example: convert_mass(500, 'mg', 'g') → 0.5
    """
    units = {"mg": 1e-3, "g": 1, "kg": 1e3}
    return value * units[from_unit] / units[to_unit]

def convert_volume(value, from_unit, to_unit):
    """
    Convert volume between 'uL', 'mL', 'L'.
    Example: convert_volume(1000, 'mL', 'L') → 1
    """
    units = {"uL": 1e-6, "mL": 1e-3, "L": 1}
    return value * units[from_unit] / units[to_unit]
