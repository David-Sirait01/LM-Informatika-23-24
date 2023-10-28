def percent_of(var, perc):
    result = (perc/100) * var
    return result

def main():
    var = int(input("Masukkan gaji :"))
    yr = int(input("Masukkan tahun :"))
    
    bonus = int
    
    if var >= 50_000 and yr > 5:
        bonus = 10
    elif var >= 50000 and yr <= 5:
        bonus = 5
    elif var <= 50000:
        bonus = 2
        
    bonus_val = percent_of(var, bonus)
    total = var + bonus_val
    print(f"Gaji awal = ${var}")
    print(f"{bonus}% bonus = ${bonus_val}")
    print(f"Total = ${total}")
    
main()