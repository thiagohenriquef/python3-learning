def calc_final_price(brute_price, taxes_calc, *args):
  return brute_price + brute_price * taxes_calc(*args)

def tax_x(imported):
  return 0.22 if imported else 0.11

def tax_y(explosive, mult_factor=1):
  return 0.11 * mult_factor if explosive 