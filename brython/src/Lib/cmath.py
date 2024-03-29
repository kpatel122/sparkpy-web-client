#############################################################################################################
# The code below was ported by Jonathan L. Verner from CPython's C implementation in Modules/cmathmodule.c
# (https://github.com/python/cpython/blob/84e6311dee71bb104e1779c89cf22ff703799086/Modules/cmathmodule.c)
#
# It is Licensed under the same license as the above file, i.e. PSF License Version 2
#
# Copyright (c) PSF 2017, (c) Jonathan L. Verner, 2017
#
#############################################################################################################

import math
import sys

def _takes_complex(func):
    def decorated(x):
        if isinstance(x, complex):
            return func(x)
        elif type(x) in [int, float]:
            return func(complex(x))
        elif hasattr(x, '__complex__'):
            c = x.__complex__()
            if not isinstance(c, complex):
                raise TypeError("A complex number is required")
            else:
                return func(c)
        elif hasattr(x, '__float__'):
            try:
                c = complex(x.__float__(), 0)
            except:
                raise TypeError("A complex number is required")
            return func(c)
        elif hasattr(x, '__index__'):
            try:
                c = complex(x.__index__(), 0)
            except:
                raise TypeError("A complex number is required")
            return func(c)
        else:
            raise TypeError("A complex number is required")
    if hasattr(func,'__doc__'):
        decorated.__doc__ = func.__doc__
    if hasattr(func,'__name__'):
        decorated.__name__ = func.__name__
    return decorated

@_takes_complex
def isfinite(x):
    return math.isfinite(x.imag) and math.isfinite(x.real)

@_takes_complex
def phase(x):
    """Return phase, also known as the argument, of a complex."""
    return math.atan2(x.imag, x.real)

@_takes_complex
def polar(x):
    """
        Convert a complex from rectangular coordinates to polar coordinates.

        The function returns a tuple with the two elements r and phi.
        r is the distance from 0 and phi the phase angle.
    """
    phi = math.atan2(x.imag, x.real)
    if math.isnan(x.imag):
        if math.isinf(x.real):
            return abs(x.real), nan
        return nan, nan
    elif math.isinf(x.imag):
        r = inf
    elif math.isinf(x.real):
        r = inf
    else:
        r = math.sqrt(x.real ** 2 + x.imag ** 2)
        if math.isinf(r):
            raise OverflowError("math range error")
    return r, phi

def rect(r, phi):
    """
        Convert from polar coordinates to rectangular coordinates and return a complex.
    """
    if math.isnan(r):
        if not math.isnan(phi) and not phi:
            return complex(nan, 0)
        return complex(nan, nan)
    elif math.isnan(phi):
        if not r:
            return complex(0, 0)
        elif math.isinf(r):
            return complex(inf, nan)
        return complex(nan, nan)
    if math.isinf(r) or math.isinf(phi):
        # need to raise Domain error if r is a nonzero number and phi
        # is infinite
        if math.isinf(phi) and r != .0 and not math.isnan(r):
            raise ValueError("math domain error")

        # if r is +/-infinity and phi is finite but nonzero then
        # result is (+-INF +-INF i), but we need to compute cos(phi)
        # and sin(phi) to figure out the signs.
        if -inf < phi < inf and phi != .0:
            if r > 0:
                _real = math.copysign(inf, math.cos(phi))
                _imag = math.copysign(inf, math.sin(phi))
            else:
                _real = -math.copysign(inf, math.cos(phi));
                _imag = -math.copysign(inf, math.sin(phi));
            return complex(_real, _imag)
        return _SPECIAL_VALUE(complex(r, phi), _rect_special_values)

    else:
        if phi == .0:
            # TODO: Not sure this applies to Brython ??
            # Workaround for buggy results with phi=-0.0 on OS X 10.8.
            # See bugs.python.org/issue18513.
            return complex(r, phi * r)
        else:
            return complex(r * math.cos(phi), r * math.sin(phi))

@_takes_complex
def sqrt(x):
    """
       Return the square root of x.

       This has the same branch cut as log().
    """
    #   Method: use symmetries to reduce to the case when x = z.real and y
    #   = z.imag are nonnegative.  Then the real part of the result is
    #   given by
    #
    #       s = sqrt((x + hypot(x, y))/2)
    #
    #   and the imaginary part is
    #
    #        d = (y/2)/s
    #
    #   If either x or y is very large then there's a risk of overflow in
    #   computation of the expression x + hypot(x, y).  We can avoid this
    #   by rewriting the formula for s as:
    #
    #       s = 2*sqrt(x/8 + hypot(x/8, y/8))
    #
    #   This costs us two extra multiplications/divisions, but avoids the
    #   overhead of checking for x and y large.
    #   If both x and y are subnormal then hypot(x, y) may also be
    #   subnormal, so will lack full precision.  We solve this by rescaling
    #   x and y by a sufficiently large power of 2 to ensure that x and y
    #   are normal.
    s, d, ax, ay = .0, .0, math.fabs(x.real), math.fabs(x.imag)

    ret = _SPECIAL_VALUE(x, _sqrt_special_values)
    if ret is not None:
        return ret

    if math.isinf(x.imag):
        return complex(inf, x.imag)

    if x.real == .0 and x.imag == .0:
        _real = .0
        _imag = x.imag
        return complex(_real,_imag)

    if ay == 0:
        s = math.sqrt(ax)
        d = 0 #x.imag
    elif ax < sys.float_info.min and ay < sys.float_info.min and (ax > 0. or ay > 0.):
        # here we catch cases where hypot(ax, ay) is subnormal
        AX = math.ldexp(ax, _CM_SCALE_UP)
        AY = math.ldexp(ay, _CM_SCALE_UP)
        S = math.sqrt((AX + math.hypot(AX, AY)) / 2.0)
        D = AY / (2 * S)
        s = math.ldexp(S, _CM_SCALE_DOWN)
        d = math.ldexp(D, _CM_SCALE_DOWN)
    else:
        ax /= 8.0;
        s = 2.0*math.sqrt(ax + math.hypot(ax, ay/8.0));
        d = ay/(2.0*s)

    if x.real >= .0:
        _real = s;
        _imag = math.copysign(d, x.imag)
    else:
        _real = d;
        _imag = math.copysign(s, x.imag)

    return complex(_real,_imag)

@_takes_complex
def acos(x):
    """
        Return the arc cosine of x.

        There are two branch cuts: One extends right from 1 along the real axis to ∞, continuous from below.
        The other extends left from -1 along the real axis to -∞, continuous from above.
    """

    ret = _SPECIAL_VALUE(x, _acos_special_values)
    if ret is not None:
        if isinstance(ret, Exception):
            raise ret
        return ret

    if math.fabs(x.real) > _CM_LARGE_DOUBLE or math.fabs(x.imag) > _CM_LARGE_DOUBLE:
        # avoid unnecessary overflow for large arguments
        _real = math.atan2(math.fabs(x.imag), x.real)

        # split into cases to make sure that the branch cut has the
        # correct continuity on systems with unsigned zeros
        if x.real < 0:
            _imag = -math.copysign(math.log(math.hypot(x.real/2., x.imag/2.)) + _M_LN2*2., x.imag);
        else:
            _imag = math.copysign(math.log(math.hypot(x.real/2., x.imag/2.)) + _M_LN2*2., -x.imag);
    elif math.isnan(x.real):
        return complex(nan, nan)
    elif math.isnan(x.imag):
        if x.real == 0:
            return complex(pi / 2, nan)
        return complex(nan, nan)
    else:
        s1 = complex(float(1 - x.real), -x.imag)
        s1 = sqrt(s1)
        s2 = complex(1.0+x.real, x.imag)
        s2 = sqrt(s2)
        _real = 2.0 * math.atan2(s1.real, s2.real)
        _imag = math.asinh(s2.real * s1.imag - s2.imag * s1.real)
        if not x.imag:
            if x.real > 1:
                _real = 0
            elif x.real < -1:
                _real = math.pi

    return complex(_real,_imag)

@_takes_complex
def acosh(x):
    """
        Return the hyperbolic arc cosine of x.

        There is one branch cut, extending left from 1 along the real axis to -∞, continuous from above.
    """
    ret = _SPECIAL_VALUE(x, _acosh_special_values)
    if ret is not None:
        return ret

    if math.fabs(x.real) > _CM_LARGE_DOUBLE or math.fabs(x.imag) > _CM_LARGE_DOUBLE:
        # avoid unnecessary overflow for large arguments
        _real = math.log(math.hypot(x.real/2.0, x.imag/2.0)) + _M_LN2*2.0
        _imag = math.atan2(x.imag, x.real);
    else:
        s1 = sqrt(complex(x.real-1.0, x.imag))
        s2 = sqrt(complex(x.real+1.0, x.imag))
        _real = math.asinh(s1.real*s2.real + s1.imag*s2.imag)
        _imag = 2.*math.atan2(s1.imag, s2.real)

    return complex(_real,_imag)

@_takes_complex
def asin(x):
    """
        Return the arc sine of x.

        This has the same branch cuts as acos().
    """
    # asin(z) == -i asinh(iz)
    s = complex(-x.imag, x.real)
    s = asinh(s)
    return complex(s.imag, -s.real)

@_takes_complex
def asinh(x):
    """
        Return the hyperbolic arc sine of x.

        There are two branch cuts: One extends from 1j along the imaginary axis to ∞j, continuous from the right.
        The other extends from -1j along the imaginary axis to -∞j, continuous from the left.
    """
    ret = _SPECIAL_VALUE(x, _asinh_special_values)
    if ret is not None:
        return ret

    if math.fabs(x.real) > _CM_LARGE_DOUBLE or math.fabs(x.imag) > _CM_LARGE_DOUBLE:
        if x.imag >= .0:
            _real = math.copysign(math.log(math.hypot(x.real/2., x.imag/2.)) + _M_LN2*2., x.real)
        else:
            _real = -math.copysign(math.log(math.hypot(x.real/2., x.imag/2.)) + _M_LN2*2., -x.real)
        _imag = math.atan2(x.imag,math.fabs(x.real))
    else:
        s1 = sqrt(complex(1.0+x.imag, -x.real))
        s2 = sqrt(complex(1.0-x.imag, x.real))
        _real = math.asinh(s1.real*s2.imag-s2.real*s1.imag)
        _imag = math.atan2(x.imag, s1.real*s2.real-s1.imag*s2.imag)
    return complex(_real,_imag)

@_takes_complex
def atan(x):
    """
        Return the arc tangent of x.

        There are two branch cuts: One extends from 1j along the imaginary axis to ∞j, continuous from the right.
        The other extends from -1j along the imaginary axis to -∞j, continuous from the left.
    """
    ret = _SPECIAL_VALUE(x, _atan_special_values)
    if ret is not None:
        return ret

    if isinf(x):
        return complex(math.copysign(1, x.real) * pi / 2,
            math.copysign(0, x.imag))
    s = atanh(complex(-x.imag, x.real))
    return complex(s.imag, -s.real)

@_takes_complex
def atanh(x):
    """
        Return the hyperbolic arc tangent of x.

        There are two branch cuts: One extends from 1 along the real axis to ∞, continuous from below.
        The other extends from -1 along the real axis to -∞, continuous from above.
    """

    ret = _SPECIAL_VALUE(x, _atanh_special_values)
    if ret is not None:
        return ret

    if isinf(x):
        return complex(math.copysign(0, x.real),
            math.copysign(1, x.imag) * pi / 2)

    # Reduce to case where x.real >= 0., using atanh(z) = -atanh(-z).
    if x.real < .0:
        return -(atanh(-x))

    ay = math.fabs(x.imag)

    if x.real > _CM_SQRT_LARGE_DOUBLE or ay > _CM_SQRT_LARGE_DOUBLE:

        #   if math.fabs(z) is large then we use the approximation
        #   atanh(z) ~ 1/z +/- i*pi/2 (+/- depending on the sign
        #   of x.imag)

        h = math.hypot(x.real/2., x.imag/2.)  # safe from overflow
        _real = x.real/4./h/h

        #   the two negations in the next line cancel each other out
        #   except when working with unsigned zeros: they're there to
        #   ensure that the branch cut has the correct continuity on
        #   systems that don't support signed zeros

        _imag = -math.copysign(math.pi/2., -x.imag)

    elif x.real == 1.0 and ay < _CM_SQRT_DBL_MIN:

        # C99 standard says:  atanh(1+/-0.) should be inf +/- 0i
        if (ay == .0):
            raise ValueError("math domain error")
        else:
            _real = -math.log(math.sqrt(ay)/math.sqrt(math.hypot(ay, 2.)))
            _imag = math.copysign(math.atan2(2.0, -ay)/2, x.imag)

    else:

        _real = math.log1p(4.*x.real/((1-x.real)*(1-x.real) + ay*ay))/4.
        _imag = -math.atan2(-2.*x.imag, (1-x.real)*(1+x.real) - ay*ay)/2.
        errno = 0

    return complex(_real,_imag)

@_takes_complex
def cos(x):
    """Return the cosine of x."""
    return cosh(complex(-x.imag, x.real))

@_takes_complex
def cosh(x):
    """Return the hyperbolic cosine of x."""

    ret = _SPECIAL_VALUE(x, _cosh_special_values)
    if ret is not None:
        if isinstance(ret, Exception):
            raise ret
        return ret

    if not math.isinf(x.real) and math.fabs(x.real) > _CM_LOG_LARGE_DOUBLE:
        #  deal correctly with cases where cosh(x.real) overflows but
        #  cosh(z) does not.
        x_minus_one = x.real - math.copysign(1.0, x.real)
        _real = cos(x.imag) * math.cosh(x_minus_one) * math.e
        _imag = sin(x.imag) * math.sinh(x_minus_one) * math.e
    elif math.isinf(x.real) and x.imag == 0:
        if x.real > 0:
            return x
        else:
            return complex(inf, -x.imag)
    elif math.isinf(x.imag):
        raise ValueError("math domain error")
    else:
        _real = math.cos(x.imag) * math.cosh(x.real)
        _imag = math.sin(x.imag) * math.sinh(x.real)

    ret = complex(_real, _imag)
    return ret

@_takes_complex
def exp(x):
    """ Return the exponential value e**x."""
    if math.isinf(x.real) or math.isinf(x.imag):
        # need to raise DomainError if y is +/- infinity and x is not -infinity or NaN
        if math.isinf(x.imag) and (-inf < x.real < inf or math.isinf(x.real) and x.real > 0):
            raise ValueError("math domain error")

        if math.isinf(x.real) and -inf < x.imag < inf and x.imag != .0:
            if x.real > 0:
                _real = math.copysign(inf, math.cos(x.imag))
                _imag = math.copysign(inf, math.sin(x.imag))
            else:
                _real = math.copysign(.0, math.cos(x.imag))
                _imag = math.copysign(.0, math.sin(x.imag))
            return complex(_real, _imag)

        return _SPECIAL_VALUE(x, _exp_special_values)

    if math.isnan(x.real) and x.imag == 0:
        return x

    if x.real > _CM_LOG_LARGE_DOUBLE:
        l = math.exp(x.real - 1.);
        _real = l * math.cos(x.imag) * math.e
        _imag = l * math.sin(x.imag) * math.e
    else:
        l = math.exp(x.real);
        _real = l * math.cos(x.imag)
        _imag = l * math.sin(x.imag)

    if math.isinf(_real) or math.isinf(_imag):
        raise OverflowError()

    return complex(_real, _imag)

def isclose(x, y, *, rel_tol=1e-09, abs_tol=0.0):
    try:
        complex(x)
    except ValueError:
        raise TypeError(f"must be a number, not {x.__class__.__name__}")
    try:
        complex(y)
    except ValueError:
        raise TypeError(f"must be a number, not {y.__class__.__name__}")
    rel_tol = float(rel_tol)
    abs_tol = float(abs_tol)
    if rel_tol < 0.0 or abs_tol < 0.0:
        raise ValueError('tolerances must be non-negative')
    if x is inf or x is _NINF or y is inf or y is _NINF:
        return y is x
    if x is nan or y is nan:
        return False
    return abs(x - y) <= max(rel_tol * float(max(abs(x), abs(y))), abs_tol)

@_takes_complex
def isinf(x):
    """Return True if the real or the imaginary part of x is positive or negative infinity."""
    return math.isinf(x.real) or math.isinf(x.imag)

@_takes_complex
def isnan(x):
    """Return True if the real or imaginary part of x is not a number (NaN)."""
    return math.isnan(x.real) or math.isnan(x.imag)


@_takes_complex
def _to_complex(x):
    return x

def log(x, base=None):
    """
        Returns the logarithm of x to the given base. If the base is not specified, returns the natural logarithm of x.

        There is one branch cut, from 0 along the negative real axis to -∞, continuous from above.
    """
    #    The usual formula for the real part is log(hypot(z.real, z.imag)).
    #    There are four situations where this formula is potentially
    #    problematic:
    #
    #    (1) the absolute value of z is subnormal.  Then hypot is subnormal,
    #    so has fewer than the usual number of bits of accuracy, hence may
    #    have large relative error.  This then gives a large absolute error
    #    in the log.  This can be solved by rescaling z by a suitable power
    #    of 2.
    #
    #    (2) the absolute value of z is greater than DBL_MAX (e.g. when both
    #    z.real and z.imag are within a factor of 1/sqrt(2) of DBL_MAX)
    #    Again, rescaling solves this.
    #
    #    (3) the absolute value of z is close to 1.  In this case it's
    #    difficult to achieve good accuracy, at least in part because a
    #    change of 1ulp in the real or imaginary part of z can result in a
    #    change of billions of ulps in the correctly rounded answer.
    #
    #    (4) z = 0.  The simplest thing to do here is to call the
    #    floating-point log with an argument of 0, and let its behaviour
    #    (returning -infinity, signaling a floating-point exception, setting
    #    errno, or whatever) determine that of c_log.  So the usual formula
    #    is fine here.

    x = _to_complex(x)
    #if type(x) == str:
        #raise TypeError("A complex number is required")

    #if type(x) != complex:
        #x = complex(x)

    denom = 1 if base is None else log(base)
    """if not x.imag:
        res = math.log(x.real) / denom
        if type(res) != complex:
            res = complex(res, x.imag)
        return res"""

    ret = _SPECIAL_VALUE(x, _log_special_values)
    if ret is not None:
        return ret

    if math.isnan(x.real):
        return complex(inf if math.isinf(x.imag) else nan, nan)
    elif math.isnan(x.imag):
        return complex(inf if math.isinf(x.real) else nan, nan)

    ax = math.fabs(x.real)
    ay = math.fabs(x.imag)

    if ax > _CM_LARGE_DOUBLE or ay > _CM_LARGE_DOUBLE:
        _real = math.log(math.hypot(ax/2.0, ay/2.0)) + _M_LN2
    elif ax < sys.float_info.min and ay < sys.float_info.min:
        if ax > .0 or ay > .0:
            # catch cases where math.hypot(ax, ay) is subnormal
            _real = math.log(math.hypot(math.ldexp(ax, sys.float_info.mant_dig), math.ldexp(ay, sys.float_info.mant_dig))) - sys.float_info.mant_dig*_M_LN2
        else:
            # math.log(+/-0. +/- 0i)
            raise ValueError("math domain error")
            _real = -inf
            _imag = math.atan2(x.imag, x.real)
    else:
        h = math.hypot(ax, ay)
        _real = math.log(h) / denom
    if not ay:
        if type(_real) == complex:
            return _real
        if x.real < 0:
            return complex(_real, math.copysign(math.pi, x.imag))
        return complex(_real, x.imag)
    _imag = math.atan2(x.imag, x.real)
    return complex(_real, _imag)

@_takes_complex
def log10(x):
    """
        Return the base-10 logarithm of x.

        This has the same branch cut as log().
    """
    ret = log(x)
    _real = ret.real / _M_LN10
    _imag = ret.imag / _M_LN10
    return complex(_real, _imag)

@_takes_complex
def sin(x):
    """ Return the sine of x. """
    # sin(x) = -i sinh(ix)
    s = complex(-x.imag, x.real)
    s = sinh(s)
    return complex(s.imag, -s.real)

@_takes_complex
def sinh(x):
    """ Return the hyperbolic sine of x. """

    ret = _SPECIAL_VALUE(x, _sinh_special_values)
    if ret is not None:
        if isinstance(ret, Exception):
            raise ret
        return ret

    if math.isinf(x.real) or math.isinf(x.imag):
        # need to raise DomainError if y is +/- infinity and x is not
        # a NaN and not -infinity
        if math.isinf(x.imag) and not math.isnan(x.real):
            raise ValueError("math domain error")

        if math.isinf(x.real) and -inf < x.imag < inf and x.imag != .0:
            if x.real > 0:
                _real = math.copysign(inf, math.cos(x.imag))
                _imag = math.copysign(inf, math.sin(x.imag))
            else:
                _real = -math.copysign(inf, math.cos(x.imag))
                _imag = math.copysign(inf, math.sin(x.imag))
            return complex(_real, _imag)

        return  _SPECIAL_VALUE(x, _sinh_special_values)

    if math.fabs(x.real) > _CM_LOG_LARGE_DOUBLE:
        x_minus_one = x.real - math.copysign(1.0, x.real)
        z = complex(x_minus_one, x.imag)
        _real = math.cos(z.imag) * math.sinh(z.real) * math.e
        _imag = math.sin(z.imag) * math.cosh(z.real) * math.e
    else:
        _real = math.cos(x.imag) * math.sinh(x.real)
        _imag = math.sin(x.imag) * math.cosh(x.real)

    if math.isinf(_real) or math.isinf(_imag):
        raise OverflowError()

    return complex(_real, _imag)

@_takes_complex
def tan(x):
    """ Return the tangent of x. """
    if math.isnan(x.real):
        if math.isinf(x.imag):
            return complex(0, math.copysign(1, x.imag))
        return complex(nan, nan)
    elif math.isnan(x.imag):
        if not x.real:
            return complex(math.copysign(0, x.real), nan)
        return complex(nan, nan)
    s = tanh(complex(-x.imag, x.real))
    return complex(s.imag, -s.real)

@_takes_complex
def tanh(x):
    """ Return the hyperbolic tangent of x. """
    """


    """

    # Formula:
    #       tanh(x+iy) = (tanh(x)(1+tan(y)^2) + i tan(y)(1-tanh(x))^2) /
    #       (1+tan(y)^2 tanh(x)^2)
    #       To avoid excessive roundoff error, 1-tanh(x)^2 is better computed
    #       as 1/cosh(x)^2.  When math.fabs(x) is large, we approximate 1-tanh(x)^2
    #       by 4 exp(-2*x) instead, to avoid possible overflow in the
    #       computation of cosh(x).
    #
    if math.isnan(x.real):
        if x.imag == 0:
            return complex(nan, math.copysign(0, x.imag))
        return complex(nan, nan)
    elif math.isnan(x.imag):
        if math.isinf(x.real):
            return complex(math.copysign(1, x.real), 0)
        return complex(nan, nan)

    if isinf(x):
        if math.isinf(x.imag) and -inf < x.real < inf:
            raise ValueError("math domain error")

        # special treatment for tanh(+/-inf + iy) if y is finite and nonzero
        if math.isinf(x.real) and -inf < x.imag < inf and x.imag != .0:
            if x.real > 0:
                _real = 1.0
                _imag = math.copysign(.0, 2.0*math.sin(x.imag)*math.cos(x.imag))
            else:
                _real = -1.0
                _imag = math.copysign(.0, 2.*math.sin(x.imag)*math.cos(x.imag))
            return complex(_real, _imag)
        return  _SPECIAL_VALUE(x, _tanh_special_values)

    # danger of overflow in 2.*z.imag !
    if math.fabs(x.real) > _CM_LOG_LARGE_DOUBLE:
        _real = math.copysign(1., x.real)
        _imag = 4.*math.sin(x.imag)*math.cos(x.imag)*math.exp(-2.*math.fabs(x.real))
    else:
        tx = math.tanh(x.real)
        ty = math.tan(x.imag)
        cx = 1.0/math.cosh(x.real)
        txty = tx*ty
        denom = 1. + txty*txty
        _real = tx*(1.+ty*ty)/denom
        _imag = ((ty/denom)*cx)*cx
    return complex(_real, _imag)

# For compliance with CPython, set all functions as built-in
FunctionType = type(_takes_complex)
locs = locals()
keys = list(locs.keys())
for f in keys:
    if type(locs[f]) is FunctionType and not f.startswith("_"):
        locals()[f] = type(abs)(locals()[f])

pi = math.pi
e = math.e
tau = math.tau

_CM_LARGE_DOUBLE = sys.float_info.max/4
_CM_SQRT_LARGE_DOUBLE = math.sqrt(_CM_LARGE_DOUBLE)
_CM_LOG_LARGE_DOUBLE = math.log(_CM_LARGE_DOUBLE)
_CM_SQRT_DBL_MIN = math.sqrt(sys.float_info.min)
_M_LN2 = 0.6931471805599453094  #  natural log of 2
_M_LN10 = 2.302585092994045684  #  natural log of 10

if sys.float_info.radix == 2:
    _CM_SCALE_UP = int((2*(sys.float_info.mant_dig/2) + 1))
elif sys.float_info.radix == 16:
    _CM_SCALE_UP = int((4*sys.float_info.mant_dig+1))
else:
    raise ("cmath implementation expects the float base to be either 2 or 16, got "+str(sys.float_info.radix)+" instead.")
_CM_SCALE_DOWN =int((-(_CM_SCALE_UP+1)/2))

inf = float('inf')
infj = complex(0.0, inf)
_NINF = float('-inf')
nan = float('nan')
nanj = complex(0.0, float('nan'))

_P14 = 0.25 * pi
_P12 = 0.5 * pi
_P34 = 0.75 * pi
_U   = -9.5426319407711027e33 # unlikely value, used as placeholder


_ST_NINF  = 0  # negative infinity
_ST_NEG   = 1  # negative finite number (nonzero)
_ST_NZERO = 2  # -0.
_ST_PZERO = 3  # +0.
_ST_POS   = 4  # positive finite number (nonzero)
_ST_PINF  = 5  # positive infinity
_ST_NAN   = 6  # Not a Number


def _SPECIAL_VALUE(z, table):
    if not math.isfinite(z.real) or not math.isfinite(z.imag):
        return table[_special_type(z.real)][_special_type(z.imag)]
    else:
        return None

def _special_type(x):
    if -inf < x < inf:
        if x != 0:
            if math.copysign(1.0, x) == 1.0:
                return _ST_POS
            else:
                return _ST_NEG
        else:
            if math.copysign(1.0, x) == 1.0:
                return _ST_PZERO
            else:
                return _ST_NZERO
    if math.isnan(x):
        return _ST_NAN
    if math.copysign(1.0, x) == 1.0:
        return _ST_PINF
    else:
        return _ST_NINF

_acos_special_values = [
    [complex(2.356194490192345, inf), None, complex(3.141592653589793, inf), complex(3.141592653589793, -inf), None, complex(2.356194490192345, -inf), complex(nan, inf)],
    [None, None, None, None, None, None, None],
    [complex(1.5707963267948966, inf), None, complex(1.5707963267948966, 0.0), complex(1.5707963267948966, -0.0), None, complex(1.5707963267948966, -inf), complex(1.5707963267948966, nan)],
    [complex(1.5707963267948966, inf), None, complex(1.5707963267948966, 0.0), complex(1.5707963267948966, -0.0), None, complex(1.5707963267948966, -inf), complex(1.5707963267948966, nan)],
    [None, None, None, None, None, None, None],
    [complex(0.7853981633974483, inf), None, complex(0.0, inf), complex(0.0, -inf), None, complex(0.7853981633974483, -inf), complex(nan, inf)],
    [complex(nan, inf), None, complex(nan, nan), complex(nan, nan), None, complex(nan, -inf), complex(nan, nan)],
]

_acosh_special_values = [
    [complex(inf, -2.356194490192345), None, complex(inf, -3.141592653589793), complex(inf, 3.141592653589793), None, complex(inf, 2.356194490192345), complex(inf, nan)],
    [None, None, None, None, None, None, None],
    [complex(inf, -1.5707963267948966), None, complex(0.0, -1.5707963267948966), complex(0.0, 1.5707963267948966), None, complex(inf, 1.5707963267948966), complex(nan, nan)],
    [complex(inf, -1.5707963267948966), None, complex(0.0, -1.5707963267948966), complex(0.0, 1.5707963267948966), None, complex(inf, 1.5707963267948966), complex(nan, nan)],
    [None, None, None, None, None, None, None],
    [complex(inf, -0.7853981633974483), None, complex(inf, -0.0), complex(inf, 0.0), None, complex(inf, 0.7853981633974483), complex(inf, nan)],
    [complex(inf, nan), None, complex(nan, nan), complex(nan, nan), None, complex(inf, nan), complex(nan, nan)],
]

_asinh_special_values = [
    [complex(-inf, -0.7853981633974483), None, complex(-inf, -0.0), complex(-inf, 0.0), None, complex(-inf, 0.7853981633974483), complex(-inf, nan)],
    [None, None, None, None, None, None, None],
    [complex(-inf, -1.5707963267948966), None, complex(-0.0, -0.0), complex(-0.0, 0.0), None, complex(-inf, 1.5707963267948966), complex(nan, nan)],
    [complex(inf, -1.5707963267948966), None, complex(0.0, -0.0), complex(0.0, 0.0), None, complex(inf, 1.5707963267948966), complex(nan, nan)],
    [None, None, None, None, None, None, None],
    [complex(inf, -0.7853981633974483), None, complex(inf, -0.0), complex(inf, 0.0), None, complex(inf, 0.7853981633974483), complex(inf, nan)],
    [complex(inf, nan), None, complex(nan, -0.0), complex(nan, 0.0), None, complex(inf, nan), complex(nan, nan)],
]

_atan_special_values = [
    [complex(-1.5707963267948966, -0.0), None, complex(-1.5707963267948966, -0.0), complex(-1.5707963267948966, 0.0), None, complex(-1.5707963267948966, 0.0), complex(-1.5707963267948966, -0.0)],
    [None, None, None, None, None, None, None],
    [complex(-1.5707963267948966, -0.0), None, complex(-0.0, -0.0), complex(-0.0, 0.0), None, complex(-1.5707963267948966, 0.0), complex(nan, nan)],
    [complex(1.5707963267948966, -0.0), None, complex(0.0, -0.0), complex(0.0, 0.0), None, complex(1.5707963267948966, 0.0), complex(nan, nan)],
    [None, None, None, None, None, None, None],
    [complex(1.5707963267948966, -0.0), None, complex(1.5707963267948966, -0.0), complex(1.5707963267948966, 0.0), None, complex(1.5707963267948966, 0.0), complex(1.5707963267948966, -0.0)],
    [complex(nan, -0.0), None, complex(nan, -0.0), complex(nan, 0.0), None, complex(nan, 0.0), complex(nan, nan)],
]

_atanh_special_values = [
    [complex(-0.0, -1.5707963267948966), None, complex(-0.0, -1.5707963267948966), complex(-0.0, 1.5707963267948966), None, complex(-0.0, 1.5707963267948966), complex(-0.0, nan)],
    [None, None, None, None, None, None, None],
    [complex(-0.0, -1.5707963267948966), None, complex(-0.0, -0.0), complex(-0.0, 0.0), None, complex(-0.0, 1.5707963267948966), complex(-0.0, nan)],
    [complex(0.0, -1.5707963267948966), None, complex(0.0, -0.0), complex(0.0, 0.0), None, complex(0.0, 1.5707963267948966), complex(0.0, nan)],
    [None, None, None, None, None, None, None],
    [complex(0.0, -1.5707963267948966), None, complex(0.0, -1.5707963267948966), complex(0.0, 1.5707963267948966), None, complex(0.0, 1.5707963267948966), complex(0.0, nan)],
    [complex(0.0, -1.5707963267948966), None, complex(nan, nan), complex(nan, nan), None, complex(0.0, 1.5707963267948966), complex(nan, nan)],
]

_cosh_special_values = [
    [ValueError('math domain error'), None, complex(inf, 0.0), complex(inf, -0.0), None, ValueError('math domain error'), complex(inf, nan)],
    [None, None, None, None, None, None, None],
    [ValueError('math domain error'), None, complex(1.0, 0.0), complex(1.0, -0.0), None, ValueError('math domain error'), complex(nan, 0.0)],
    [ValueError('math domain error'), None, complex(1.0, -0.0), complex(1.0, 0.0), None, ValueError('math domain error'), complex(nan, 0.0)],
    [None, None, None, None, None, None, None],
    [ValueError('math domain error'), None, complex(inf, -0.0), complex(inf, 0.0), None, ValueError('math domain error'), complex(inf, nan)],
    [complex(nan, nan), None, complex(nan, 0.0), complex(nan, 0.0), None, complex(nan, nan), complex(nan, nan)],
]

_exp_special_values = [
    [complex(0.0, 0.0), None, complex(0.0, -0.0), complex(0.0, 0.0), None, complex(0.0, 0.0), complex(0.0, 0.0)],
    [None, None, None, None, None, None, None],
    [ValueError('math domain error'), None, complex(1.0, -0.0), complex(1.0, 0.0), None, ValueError('math domain error'), complex(nan, nan)],
    [ValueError('math domain error'), None, complex(1.0, -0.0), complex(1.0, 0.0), None, ValueError('math domain error'), complex(nan, nan)],
    [None, None, None, None, None, None, None],
    [ValueError('math domain error'), None, complex(inf, -0.0), complex(inf, 0.0), None, ValueError('math domain error'), complex(inf, nan)],
    [complex(nan, nan), None, complex(nan, -0.0), complex(nan, 0.0), None, complex(nan, nan), complex(nan, nan)],
]

_log_special_values = [
    [complex(inf, -2.356194490192345), None, complex(inf, -3.141592653589793), complex(inf, 3.141592653589793), None, complex(inf, 2.356194490192345), complex(inf, nan)],
    [None, None, None, None, None, None, None],
    [complex(inf, -1.5707963267948966), None, ValueError('math domain error'), ValueError('math domain error'), None, complex(inf, 1.5707963267948966), complex(nan, nan)],
    [complex(inf, -1.5707963267948966), None, ValueError('math domain error'), ValueError('math domain error'), None, complex(inf, 1.5707963267948966), complex(nan, nan)],
    [None, None, None, None, None, None, None],
    [complex(inf, -0.7853981633974483), None, complex(inf, -0.0), complex(inf, 0.0), None, complex(inf, 0.7853981633974483), complex(inf, nan)],
    [complex(inf, nan), None, complex(nan, nan), complex(nan, nan), None, complex(inf, nan), complex(nan, nan)],
]

_sinh_special_values = [
    [ValueError('math domain error'), None, complex(-inf, -0.0), complex(-inf, 0.0), None, ValueError('math domain error'), complex(inf, nan)],
    [None, None, None, None, None, None, None],
    [ValueError('math domain error'), None, complex(-0.0, -0.0), complex(-0.0, 0.0), None, ValueError('math domain error'), complex(0.0, nan)],
    [ValueError('math domain error'), None, complex(0.0, -0.0), complex(0.0, 0.0), None, ValueError('math domain error'), complex(0.0, nan)],
    [None, None, None, None, None, None, None],
    [ValueError('math domain error'), None, complex(inf, -0.0), complex(inf, 0.0), None, ValueError('math domain error'), complex(inf, nan)],
    [complex(nan, nan), None, complex(nan, -0.0), complex(nan, 0.0), None, complex(nan, nan), complex(nan, nan)],
]

_sqrt_special_values = [
    [complex(inf, -inf), None, complex(0.0, -inf), complex(0.0, inf), None, complex(inf, inf), complex(nan, inf)],
    [None, None, None, None, None, None, None],
    [complex(inf, -inf), None, complex(0.0, -0.0), complex(0.0, 0.0), None, complex(inf, inf), complex(nan, nan)],
    [complex(inf, -inf), None, complex(0.0, -0.0), complex(0.0, 0.0), None, complex(inf, inf), complex(nan, nan)],
    [None, None, None, None, None, None, None],
    [complex(inf, -inf), None, complex(inf, -0.0), complex(inf, 0.0), None, complex(inf, inf), complex(inf, nan)],
    [complex(inf, -inf), None, complex(nan, nan), complex(nan, nan), None, complex(inf, inf), complex(nan, nan)],
]

_tanh_special_values = [
    [complex(-1.0, 0.0), None, complex(-1.0, -0.0), complex(-1.0, 0.0), None, complex(-1.0, 0.0), complex(-1.0, 0.0)],
    [None, None, None, None, None, None, None],
    [ValueError('math domain error'), None, complex(-0.0, -0.0), complex(-0.0, 0.0), None, ValueError('math domain error'), complex(nan, nan)],
    [ValueError('math domain error'), None, complex(0.0, -0.0), complex(0.0, 0.0), None, ValueError('math domain error'), complex(nan, nan)],
    [None, None, None, None, None, None, None],
    [complex(1.0, 0.0), None, complex(1.0, -0.0), complex(1.0, 0.0), None, complex(1.0, 0.0), complex(1.0, 0.0)],
    [complex(nan, nan), None, complex(nan, -0.0), complex(nan, 0.0), None, complex(nan, nan), complex(nan, nan)],
]

_rect_special_values = [
    [ValueError('math domain error'), complex(inf, inf), complex(-inf, 0.0), complex(-inf, -0.0), complex(inf, -inf), ValueError('math domain error'), complex(inf, nan)],
    [ValueError('math domain error'), complex(0.8322936730942848, 1.8185948536513634), complex(-2.0, 0.0), complex(-2.0, -0.0), complex(0.8322936730942848, -1.8185948536513634), ValueError('math domain error'), complex(nan, nan)],
    [complex(0.0, 0.0), complex(0.0, 0.0), complex(-0.0, 0.0), complex(-0.0, -0.0), complex(0.0, -0.0), complex(0.0, 0.0), complex(0.0, 0.0)],
    [complex(0.0, 0.0), complex(-0.0, -0.0), complex(0.0, -0.0), complex(0.0, 0.0), complex(-0.0, 0.0), complex(0.0, 0.0), complex(0.0, 0.0)],
    [ValueError('math domain error'), complex(-0.8322936730942848, -1.8185948536513634), complex(2.0, -0.0), complex(2.0, 0.0), complex(-0.8322936730942848, 1.8185948536513634), ValueError('math domain error'), complex(nan, nan)],
    [ValueError('math domain error'), complex(-inf, -inf), complex(inf, -0.0), complex(inf, 0.0), complex(-inf, inf), ValueError('math domain error'), complex(inf, nan)],
    [complex(nan, nan), complex(nan, nan), complex(nan, 0.0), complex(nan, 0.0), complex(nan, nan), complex(nan, nan), complex(nan, nan)],
]



