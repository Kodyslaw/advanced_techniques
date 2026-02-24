import numpy as np
import pytest

from copilot_fft import rms

#dodaj własny przypadek testowy dla sygnału zerowego 
def test_rms_zero_signal():
    """RMS of a zero signal should be zero."""
    arr = np.zeros(100)
    assert rms(arr) == pytest.approx(0.0)


def test_rms_constant_signal():
    """A constant nonzero signal has RMS equal to absolute value."""
    arr = np.full(50, -3.0)
    assert rms(arr) == pytest.approx(3.0)


def test_rms_known_values():
    # simple two-point example: values 1 and -1 -> rms = 1
    arr = np.array([1.0, -1.0])
    assert rms(arr) == pytest.approx(1.0)

    # verify against numpy directly for random data
    rng = np.random.default_rng(0)
    arr = rng.standard_normal(1000)
    expected = np.sqrt(np.mean(arr**2))
    assert rms(arr) == pytest.approx(expected)




