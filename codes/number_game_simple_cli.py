# Saliz Thanks You

from random import shuffle

class Main:
	def __init__(self):
		self.rumus = self.make_rumus()
		self.sort_number = self.rand_sort_number()
		self.index = self.find_index()
		self.angka = self.sorted_to_rumus()

	@staticmethod
	def make_rumus():
		data = [
			[1, 1, 2, 3, 4],
			[5, 5, 2, 6, 7],
			[8, 8, 3, 6, 9],
			[0, 0, 4, 7, 9]
		]
		for x in range(len(data)):
			shuffle(data[x])
		shuffle(data)
		return data

	@staticmethod
	def rand_sort_number():
		data = list(range(1,21))
		shuffle(data)
		genap = [data[i] for i in range(len(data)) if i % 2 == 0]
		ganjil = [data[i] for i in range(len(data)) if i % 2 != 0]
		return list(zip(ganjil, genap))

	@staticmethod
	def find_double_one_line(x):
		for i in x:
			if x.count(i) == 2:
				y = i
				break
		data = [i for i, e in enumerate(x) if e == y]
		return data

	@staticmethod
	def find_double_multi_line(a,b):
		sarua = list(set(a) & set(b))[0]
		data = [i for i, e in enumerate(a + b) if e == sarua]
		data[1] -= 5
		return data

	def find_index(self):
		rumus = self.rumus
		data = {}
		for i, x in enumerate(rumus):
			data[i + 1] = self.find_double_one_line(x)

		for i, x in enumerate(rumus):
			for i2, y in enumerate(rumus):
				if i != i2 and not (i2 + 1, i + 1) in data:
					data[i + 1, i2 + 1] = self.find_double_multi_line(x,y)

		return data

	def sorted_to_rumus(self):
		# rumus = self.rumus
		sort = self.sort_number
		data = [
			[None] * 5,
			[None] * 5,
			[None] * 5, 
			[None] * 5 
		]
		angka = -1
		for key, value in self.index.items():
			angka += 1
			if not "tuple" in str(type(key)):
				data[key - 1][value[0]] = sort[angka][0]
				data[key - 1][value[1]] = sort[angka][1]
			else:
				data[key[0] - 1][value[0]] = sort[angka][0]
				data[key[1] - 1][value[1]] = sort[angka][1]
		return data

	def search(self, data):
		if "int" in str(type(data)):
			a = self.index[data][0]
			b = self.index[data][1]
			c = self.angka[data - 1]
			return list((c[a], c[b]))
		else:
			rv = []
			data = tuple(sorted(data))
			value = self.index[data]
			for x in zip(list(data), value):
				a = self.angka[x[0] - 1]
				rv.append(a[x[1]])
			return rv

def main():
	gas = Main()
	os.system("cls" if os.name == "nt" else "clear")
	print("Pilih dua angka dari urutan dibawah (harus satu kelompok atau dalam satu tanda kurung) dan tulis angka pilihanmu dikertas !\n")
	print(gas.sort_number)
	getpass("\nSudah Menulis? Enter Untuk Melanjutkan")
	os.system("cls" if os.name == "nt" else "clear")
	for i, x in enumerate(gas.angka):
		print(f"{i + 1}.\t{x}")
	data = eval(input("\nDibaris berapa angka pilihanmu berada? (contoh: 1 atau 1,3): "))
	print("\nAngka pilihanmu adalah: ", gas.search(data))
	print("KALO SALAH BERARTI LU NYA YG GOBLOKK !!!!")

if __name__ == "__main__":
	from getpass import getpass
	import os
	main()
