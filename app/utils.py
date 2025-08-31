# app/utils.py

def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if (min_val is not None and val < min_val) or (max_val is not None and val > max_val):
                print(f"Input harus antara {min_val} dan {max_val}.")
                continue
            return val
        except ValueError:
            print("Input harus berupa angka.")
