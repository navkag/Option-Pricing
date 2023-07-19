# Option Price Calculator

Welcome to the Option Price Calculator project! This web application allows users to calculate the price of an option based on various inputs such as spot price, volatility, interest rate, maturity time, and strike price of the underlying security. The calculation can be performed using three different pricing methods: 2-step binomial pricing, N-step binomial pricing, and Normal Distribution pricing.

## Demo

https://github.com/navkag/Option-Pricing/assets/88591105/be69495c-8605-4876-ba39-5ac7215856e7


## Features

- **User-Friendly Interface:** The front-end of the website is designed using HTML and CSS, providing an intuitive and visually appealing interface. Users can easily navigate through the options and input their values effortlessly.

- **Accurate Calculation:** The back-end of the website is powered by Django, a robust Python web framework. The option price calculation is performed based on the user's inputs and the chosen pricing method. This ensures accurate and reliable results for the users.

- **Transparency and Understanding:** The results page not only displays the calculated option price but also showcases the formulae used to arrive at that price. These formulae are presented in LaTeX format, making it easier for users to understand and verify the calculations.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/navkag/option-pricing.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Start the Django development server: `python manage.py runserver`
4. Access the application in your browser: `http://localhost:8000`
