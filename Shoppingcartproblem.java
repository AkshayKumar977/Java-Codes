import java.util.Scanner;
public class Shoppingcartproblem {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String item;
        System.out.print("Enter the item you want to buy: ");
        item = scanner.nextLine();
        System.out.print("How much " + item + " You want to buy: ");
        int amount = scanner.nextInt();
        System.out.print("Enter the price of the " + item + ": ");
        Double price = scanner.nextDouble();
        Double total_price = amount * price;
        System.out.println("The total amount you have to pay is : " + total_price);
        scanner.close();
    }
}
