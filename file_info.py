def load_product():
  from pathlib import Path
  import json
  folder = Path.cwd()
  product_json = folder / 'products.json'
  if product_json.exists():
      with open(product_json, 'r', encoding='utf-8') as f:
          data = json.load(f)
          return data
  else:
      raise FileNotFoundError("File Not Found!")
  
def load_user_detail(choice):
  from pathlib import Path
  import json
  folder = Path.cwd()
  if choice == 1:
      farmer_json = folder / 'farmers.json'
      if farmer_json.exists():
          with open(farmer_json, 'r', encoding='utf-8') as f:
              data = json.load(f)
              return data
      else:
          raise FileNotFoundError("File Not Found!")
  else:
      trader_json = folder / 'traders.json'
      if trader_json.exists():
          with open(trader_json, 'r', encoding='utf-8') as f:
              data = json.load(f)
              return data
      else:
          raise FileNotFoundError("File Not Found!")

