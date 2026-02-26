public class Complex {

	double re;
	double im;

	public Complex(double re, double im) {
		this.re = re;
		this.im = im;
	}

	public String toString() {
		return this.re + " " + this.im;
	}

	public Complex add(Complex other) {
		return new Complex(this.re+other.re, this.im+other.im);
	}

	public static void main(String[] args) {
		Complex z1 = new Complex(1,2);
		Complex z2 = new Complex(3,4);
		System.out.println(z1+z2);
	}
}
