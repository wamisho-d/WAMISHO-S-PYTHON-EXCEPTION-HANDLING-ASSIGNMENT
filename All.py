# Question 1 Task 1: Start
def temperature():
    while True:
        user_input = int(input("Eenter the temperature in Fahrenheit: "))
        try:
            temperature = int(user_input)
            print(f"The temperature you entered is {temperature}°F.")
            break
        except ValueError:
            print("Invalid input. Enter a number.")
            
temperature()

# Question 1 Task 2: Temperature Conversion.
def Fahrenheit_to_Celsius(Fahrenheit):
    try:
       celsius = (Fahrenheit - 32) * 5/9
       return celsius
    except TypeError:
      return "Error: Input must be a numerical value."
    except OverflowError:
      return " Error: Input is too large."
    except Exception as e:
      return f"An unexpected error occured: {str(e)}"
    
print(Fahrenheit_to_Celsius(120))
print(Fahrenheit_to_Celsius("a lot"))

# Question 1 Task 3: User Experience
def convert_temperature(temperature, unit):
   try:
       if unit.lower() == 'c':
         converted_temperature = (temperature * 9/5) + 32
         unit = 'F'
       elif unit.lower() == 'f':
         converted_temperature = (temperature - 32)* 5/9
         unit = 'C'
       else:
          raise ValueError("Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit.")
   except  ValueError as e:
      print(f"Error: {e}") 
   else:
      print(f"The converted temperature is :{converted_temperature: .2f}°{unit}")
   finally:
      print("Thank you for using the weather forecast application.")
try:
   temperature = int(input("Enter the temperature:"))
   unit = input("Enter the unit('C' for Celsius or 'F' for Fahrenheit):")
   convert_temperature(temperature, unit)
except ValueError:
   print("Enter a valid numerical value for the temperature.")

# Question 2 Task 1: Start. 
def valid_input(prompt):
   while True:
      try:
         user_input = input(prompt)
         value = int(user_input)
         if value <= 0:
            raise ValueError("The number of serving must be greater than zero.")
         return value 
      except ValueError as e:
         print(f"Invalid input: {e}. Enter a valid numerical value.")

def main():
   orginal_servings = valid_input("Enter the number of servings the recipe is originally for:")
   desired_serving = valid_input("Enter the number of servings they wish to prepare: ")
   print(f"orginal_serving:{orginal_servings}")
   print(f"desired_serving:{desired_serving}")

if __name__ == "__main__":
 main()

# Question 2 Task 2: Quantity Calculation.

def calculate_the_adjustment_factor(desired_servings,original_servings):
   try:
      adjustment_factor = desired_servings / original_servings
      return adjustment_factor
   except ZeroDivisionError:
       return "Error: Division by zero is not allowed."
   except TypeError:
       return "Error: Both desired_servings and original_servings must be numbers."

desired_servings = 60
original_servings = 10
   
adjustment_factor = calculate_the_adjustment_factor(desired_servings, original_servings)
print(f"Adjustment factor: {adjustment_factor}")

# Question 2 Task 3: Serving Success.
def adjust_recipe(orginal_quantity, scale_factor):
   try:
      adjusted_quantity = orginal_quantity * scale_factor
      print(f"Adjusted Recipe Quantity: {adjusted_quantity}")
   except  Exception as e:
      print(f"An error happend: {e}")
   finally:
      print("Enjoy your cooking.")

orginal_quantity = 600
scale_factor = 3
adjust_recipe(orginal_quantity, scale_factor)
       


   
   
   

   
   
      


   


     
 
       
     

     

