import xlsxwriter

from Repository.file_repository import FileRepository

workbook = xlsxwriter.Workbook('Example2.xlsx')
worksheet = workbook.add_worksheet()

row = 0
column = 0
medicament_repository = FileRepository('medicament.txt')
content = []

for i in medicament_repository.get_all():
    content.append(i.id_entity)

for item in content:
    worksheet.write("A1", "Id medicament")
    worksheet.write("B1", "nume")
    worksheet.write("C1", "producator")
    worksheet.write("D1", "pret")
    worksheet.write("E1", "reteta")
    row = row + 1

content2 = []
for i in medicament_repository.get_all():
    content2.append([i.id_entity, i.nume, i.producator, i.pret, i.reteta])
row = 1
for id, nume, producator, pret, reteta in content2:
    worksheet.write(row, column, id)

    worksheet.write(row, column + 1, nume)

    worksheet.write(row, column + 2, producator)

    worksheet.write(row, column + 3, pret)

    worksheet.write(row, column + 4, reteta)
    row += 1

workbook.close()