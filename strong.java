public class strong {

    // Pre-computed factorials for digits 0-9 for efficiency
    private static final int[] FACTORIALS = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

    /**
     * Checks if a given number is a strong number.
     * A strong number is a number whose sum of the factorial of its digits equals the original number.
     *
     * @param number The number to check.
     * @return true if the number is a strong number, false otherwise.
     */
    public static boolean isStrong(int number) {
        if (number < 0) { // Strong numbers are typically defined for non-negative integers
            return false;
        }
        int originalNumber = number;
        int sumOfFactorials = 0;

        while (number > 0) {
            int digit = number % 10;
            sumOfFactorials += FACTORIALS[digit];
            number /= 10;
        }

        return sumOfFactorials == originalNumber;
    }

    public static void main(String[] args) {
        System.out.println("Strong numbers from 1 to 5000:");
        for (int i = 1; i <= 5000; i++) {
            if (isStrong(i)) {
                System.out.println(i);
            }
        }
    }
}