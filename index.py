def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
 ##### Calling the function with three arguments
my_function("Emil", "Tobias", "Linus")