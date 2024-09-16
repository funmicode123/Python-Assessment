import java.util.Scanner;
public class PizzaTest {
	
	public static void main(String... args){
	Scanner input = new Scanner(System.in);
	System.out.println("Please, enter your name: ");
	String customerName = input.nextLine();
	System.out.println("Welcome " + customerName + ", to Iya Afeez Pizza joint, Ajegunle");
	System.out.println("Enter number of guest: ");
	int guestNumber = input.nextInt();

	String pizzaCategoryMenu = """ 
                Pizza type   Number Of Slices        Price Per Box
                ----------------------------------------------------
                1           4                        2000
                2           6                        2400
                3           6                        3000
                4           12                       4200
                """;

	System.out.println("Pizza Category: ");
	System.out.println(pizzaCategoryMenu);

	System.out.println("Enter the Pizza category (1-4): ");
	int pizzaCategory = input.nextInt();

	if (pizzaCategory < 1 || pizzaCategory > 4){
		System.out.println("Invalid pizza category.");
		return;
	}
	
	int pricePerBox = PizzaFunction.returnPrice(pizzaCategory);
	int slicesPerBox = PizzaFunction.numberOfSlices(pizzaCategory);
	

	int boxesNeeded = PizzaFunction.numberOfPizzaBoxes(guestNumber, slicesPerBox);
	System.out.println("Number of boxes of Pizza to buy: " + boxesNeeded);

	int leftOverSlices = PizzaFunction.leftOver(boxesNeeded, slicesPerBox, guestNumber);
	System.out.println("Number of leftover slices: " + leftOverSlices + "slices");

	int totalPrice = PizzaFunction.customerPrice(boxesNeeded, pricePerBox);
	System.out.println("Cost of the Pizza: " + totalPrice);

	}
}