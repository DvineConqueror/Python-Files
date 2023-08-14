import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Input Limit
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter Limit: ");
        int Limit = scanner.nextInt();
        
        // Initialize Number
        int Number = 1;
        
        // Find the smallest Number for which the sum is greater than Limit
        while (calculateSum(Number) <= Limit) {
            Number++;
        }
        
        // Calculate the final sum for the found Number
        int FinalSum = calculateSum(Number);
        
        // Print the results
        System.out.println("Smallest Number: " + Number);
        System.out.println("Final Sum: " + FinalSum);
    }
    
    // Define the function to calculate the sum
    public static int calculateSum(int Number) {
        int Sum = 0;
        for (int i = 1; i <= 2 * Number; i++) {
            Sum += i;
        }
        return Sum;
    }
}
