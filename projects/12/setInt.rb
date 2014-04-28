number = 12345

while number > 0
  exp = 1
  first_digit = number

  while first_digit > 9
    first_digit /= 10
    exp *= 10
  end

  number = number - exp * first_digit
  print number + 48
end
