

#add another function to do fah to celcius

def f_to_c(celsius):
  """given a celsius value return the conversion"""
  fahrenheit= celsius * 9/5 + 32 
  return ( f + 32)*5/9

celsius = 25
fahrenheit = celsius_to_farenheit(celsius)
print(f"{celsius} Celsius to Fahrenheit is {fahrenheit}")


celsius = f_to_c(fahrenheit)
print(f"{fahrenheit} Fahrenheit to celcius is {celsius}")

