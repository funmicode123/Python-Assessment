mortgage_calculator = new mortgage_calculator();
	
	principal = input("Enter Principal: ")
	rate = input("Enter rate: ")
	duration = input("Enter duration: ")

	mortgage_calculator.setPrincipal(principal1)
	mortgage_calculator.setRate(rate1)
	mortgage_calculator.setDuration(duration1)

	mortgageResult = mortgage_calculator.computeMortgage()
	print("The mortgage result: %.2f", mortgageResult)

	set_principal(principal)
		this.principal = principal

	set_rate(rate)
		this.rate = rate

	set_duration(duration)
		this.duration = duration


			computeMortgage()
		monthlyRate = (rate / 100)
		percentageRate = monthlyRate / 12
		noOfMonths = duration * 12
		numerator = percentageRate * Math.pow((1 + percentageRate), 	noOfMonths)
		denominator = Math.pow((1 + percentageRate), noOfMonths) - 1

	
	return principal * (numerator / denominator)

