which_one = int(input("Whath month, (1 - 12)? "))
months = ['Jnuar', 'Februar', 'Mart', 'April', 'Maj', 'Jun',
          'Jul', 'Avgust', 'Septembar', 'Oktobar', 'Novembar', 'Decembar']
if 1 <= which_one <= 12:
    print("mesec je", months[which_one -1])
