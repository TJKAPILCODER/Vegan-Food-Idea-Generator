import random

main_dish = ["Lentil Bolognese", "VEGETABLE BIRYANI", "WHOLE ROASTED CAULIFLOWER ", "FRANKIES! (BOMBAY BURRITOS)", "Chipotle Portobello Tacos", "VEGAN SHEPHERDS PIE","Spaghetti and Beetballs", "Spicy Chinese Eggplant with Szechuan Sauce",
 "KABOCHA SQUASH MILLET BOWLS","DATE NIGHT VEGAN ALFREDO", "VEGAN TIKKA MASALA",'VEGAN BROCCOLI “CHEDDAR”', "BUTTERNUT SQUASH RISOTTO WITH LEEKS AND SPINACH", "CRISPY VEGAN QUINOA CAKES", "Vegan Ramen with Miso Shiitake Broth",
  "Portobello Mushroom Burger", "VEGAN FARMERS MARKET FRIED RICE", "Roasted Sheet-Pan Ratatouille", "Oaxacan Bowl"]

side_dish = ["Creamy Corn Salad", "Pearl Couscous Salad", "Sauteed Mushrooms", "Mediterranean Quinoa Salad" "Roasted Broccoli with Sweet Chili Sauce", "Potato Cakes with Carrot and Rice",
"Three Bean Wild Rice Salad", "Sesame Garlic Green Beans", "Air Fryer Carrots (3 Ways)", "Cucumber Pasta Salad", "Lemon Garlic Grilled Zucchini", "Roasted Baby Potatoes with Pesto",
"Tahini Dill Carrot Noodles", "Roasted Balsamic Green Beans with Tomatoes", "Tomato Avocado Salad", "Roasted Asparagus with Lemon Tahini", "Garlicky Mashed Cauliflower", "Edamame Sesame Quinoa Salad",
"Raw Veggie Noodles", "Cilantro-Lime Black Bean Rice", "Maple Glazed Sauteed Carrots", "Cauliflower Rice", "Corn Avocado and Tomato Salad", "Moroccan Roasted Vegetable Salad",
"Chanterelle Mushrooms with Potatoes","Artichoke Sun-dried Tomato Risotto", "Smoky Baked Beans", "BBQ Brussels Sprouts", "Ranch Pasta Salad", "Miso Glazed Roasted Root Vegetables",
"Grilled Zucchini and Mushrooms", "Oven Baked Sweet Potato Fries", "Orzo Salad with Spinach and Tomato", "Thai Cucumber Salad", "Nicoise Salad", "Baked Zucchini Fries", "Cobb Salad",
"Lemon Garlic Herb Roasted Potatoes", "Tex Mex Roasted Sweet Potato Salad", "Tomato Cucumber Salad", "Chickpea Lemon Rice", "Roasted Carrots with Tahini", "Moroccan Quinoa and Carrot Salad",
" Spicy Stir-Fried Cabbage", "Corn Salad with Basil Pesto", "Maple Gochujang Roasted Brussels Sprouts", "Avocado Black Bean Salad", "“Cheesy” Roasted Cauliflower", "Balsamic Soy Roasted Garlic Mushrooms"]



random_choice_main = random.choice(main_dish)

random_choice_side = random.choice(side_dish)


print(f"How about you have {random_choice_main} for the main dish and {random_choice_side} for the side dish?")
