Here's a basic implementation of the `Smart-Fit-Planner`, a personalized fitness planning application that generates adaptive workout and nutrition plans based on user data and goals. This program is interactive and can be built upon further with more advanced functionalities. It uses object-oriented programming to structure the application and includes error handling and comments for clarity.

```python
import json

class User:
    def __init__(self, username, age, gender, weight, height, goal):
        self.username = username
        self.age = age
        self.gender = gender
        self.weight = weight
        self.height = height
        self.goal = goal
        self.workouts = []
        self.nutrition_plan = {}

    def update_weight(self, new_weight):
        try:
            self.weight = float(new_weight)
            self.update_plans()  # Recalculate plans based on new weight
        except ValueError as e:
            print(f"Error updating weight: {e}")

    def update_plans(self):
        """ Update workout and nutrition plans based on user data and goals """
        self.workouts = self.generate_workout_plan()
        self.nutrition_plan = self.generate_nutrition_plan()

    def generate_workout_plan(self):
        """ Generate a workout plan based on user goals """
        print("Generating workout plan...")
        if self.goal.lower() == "lose weight":
            return ["Cardio - 30 mins", "Cycling - 20 mins", "Yoga - 15 mins"]
        elif self.goal.lower() == "gain muscle":
            return ["Weight lifting - 40 mins", "HIIT - 20 mins", "Planks - 10 mins"]
        elif self.goal.lower() == "maintain":
            return ["Running - 20 mins", "Swimming - 30 mins", "Pilates - 20 mins"]
        else:
            return ["General Fitness - 30 mins stretch"]

    def generate_nutrition_plan(self):
        """ Generate a nutrition plan based on user goals """
        print("Generating nutrition plan...")
        if self.goal.lower() == "lose weight":
            return {"Breakfast": "Oatmeal", "Lunch": "Grilled Chicken Salad", "Dinner": "Steamed Vegetables"}
        elif self.goal.lower() == "gain muscle":
            return {"Breakfast": "Protein Shake", "Lunch": "Chicken Breast & Rice", "Dinner": "Beef Stew"}
        elif self.goal.lower() == "maintain":
            return {"Breakfast": "Toast with Avocado", "Lunch": "Quinoa Salad", "Dinner": "Salmon & Broccoli"}
        else:
            return {"Breakfast": "Smoothie", "Lunch": "Mixed Veggie Wrap", "Dinner": "Vegetable Soup"}

def main():
    print("Welcome to Smart-Fit-Planner!")
    try:
        username = input("Enter your username: ")
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (M/F): ")
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        goal = input("What is your fitness goal? (lose weight/gain muscle/maintain): ")

        user = User(username, age, gender, weight, height, goal)
        user.update_plans()

        # Display the generated plans
        print(f"Workout plan for {user.username}: {user.workouts}")
        print(f"Nutrition plan for {user.username}: {json.dumps(user.nutrition_plan, indent=2)}")

        # Update weight and plans
        while True:
            update = input("Do you want to update your weight? (yes/no): ")
            if update.lower() == 'yes':
                new_weight = input("Enter your new weight in kg: ")
                user.update_weight(new_weight)
                print(f"Updated Workout plan: {user.workouts}")
                print(f"Updated Nutrition plan: {json.dumps(user.nutrition_plan, indent=2)}")
            else:
                break

    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
```

**Explanation:**

1. **User Class**: 
   - Encapsulates user-related data.
   - Functions for updating weight and generating workout/nutrition plans based on user data/goal.

2. **Error Handling**: 
   - Around input parsing and performing operations that might raise exceptions.

3. **Interactive Session**:
   - Asks for user inputs to create an initial profile.
   - Users can update their weight, triggering an update to the plans.

4. **Plans Generation**:
   - Simple conditionals to demonstrate how plans are generated. You can expand these rules to include more logic, maybe using libraries or APIs to fetch more realistic exercise and meal options.

This basic script relies on simple conditions to generate plans. More complex algorithms or real-time data API integration can provide more personalized and precise plans.