typedef struct {
    float real;
    float imag;
} Complex;

extern Complex add(Complex x, Complex y)
{
    Complex result;
    result.real = x.real + y.real;
    result.imag = x.imag + y.imag;
    return result;
}

extern int equal(Complex x, Complex y)
{
    return x.real == y.real && x.imag == y.imag;
}
