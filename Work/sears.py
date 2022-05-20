
bill_thickness = 0.11 * 0.001 #grosor del billete en metros
sears_height = 422 #altura de la sears en metros
num_bills = 1
days = 1


while num_bills * bill_thickness < sears_height:
    print(days, num_bills, (num_bills * bill_thickness))
    days = days + 1
    num_bills = num_bills * 2

print('Numero de dias:', days)
print('Numero de billetes:', num_bills)
print('Altura Final:', num_bills * bill_thickness)