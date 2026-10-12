import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    def poly(coeff,x):
        n = len(coeff) - 1
        return  sum(c*x**(n-i) for i,c in enumerate(coeff))
    def poly_deriv(coeff):
        n = len(coeff) -1
        return [c*(n-i )for i,c in enumerate(coeff[:-1])]

    g_x = poly(g_coeffs,x)
    h_x = poly(h_coeffs,x)
    d_g_x = poly(poly_deriv(g_coeffs),x)
    d_h_x = poly(poly_deriv(h_coeffs),x)

    return (d_g_x*h_x - g_x*d_h_x)/pow(h_x,2)
       