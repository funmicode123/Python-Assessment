public class PizzaFunction {


	public static int returnPrice(int pizzaCategory){

	switch (pizzaCategory){	

		case 1:
			return 2000;

		case 2: 
			return 2400;

		case 3:
			return 3000;

		case 4:
			return 4200;
		default:
			throw new IllegalArgumentException("Invalid pizza category");
	}

	}


	public static int numberOfSlices(int pizzaCategory){
	
	switch (pizzaCategory){
		case 1: 
			return 4;

		case 2: 
			return 6;

		case 3:
			return 8;

		case 4: 
			return 12;
		default:
			throw new IllegalArgumentException("Invalid pizza category");



	}

	}


	public static int numberOfPizzaBoxes(int guestNumber, int slicesPerBox){
	if (guestNumber % slicesPerBox == 0)
		return guestNumber / slicesPerBox;
	else
		return guestNumber / slicesPerBox + 1;

	}


	public static int leftOver (int boxesNeeded, int slicesPerBox, int guestNumber){

	return (boxesNeeded * slicesPerBox) - guestNumber;

	}


	public static int customerPrice(int boxesNeeded, int pricePerBox){

	return boxesNeeded * pricePerBox;
	}



}