'''
Task 1: Define Budget Category Class

Create a class BudgetCategory with private attributes for category name and allocated budget.
Initialize these attributes in the constructor.
Expected Outcome: A BudgetCategory class capable of storing category details securely.
Task 2: Implement Getters and Setters

Write getter and setter methods for both the category name and the allocated budget.
Ensure that the setter methods include validation (e.g., budget should be a positive number).
Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.
Task 3: Add Budget Functionality

Implement a method to add expenses to a category and adjust the budget accordingly.
Validate the expense amount before making deductions from the budget.
Expected Outcome: Ability to track expenses per category and update the remaining budget safely.
Task 4: Display Budget Details

Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.
Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.
'''

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name

    def get_allocated_budget(self):
        return self.__allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self.__allocated_budget = new_budget
        else:
            print("Error:")

    def add_expense(self, expense_amount):
        if expense_amount >= 0 and expense_amount <= self.__remaining_budget:
            self.__remaining_budget -= expense_amount
            print("Expense added successfully.")
        elif expense_amount < 0:
            print("Error: Expense amount must be a positive number.")
        else:
            print("Error: Expense amount exceeds remaining budget.")

    def display_budget_details(self):
        print("Category Name:", self.__category_name)
        print("Allocated Budget:", self.__allocated_budget)
        print("Remaining Budget:", self.__remaining_budget)


food_category = BudgetCategory("Food", 500)
food_category.display_budget_details()
food_category.add_expense(50)
food_category.add_expense(1000) 
food_category.display_budget_details()