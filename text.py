
# Bài 1 nhập và xuất
# From Vũ Minh Hiếu 

print('Nhập vào số các phần tử trong list');
n = int(input());
a = [];
for i in range(0,n):
	print('Nhập vào phần tử: ', i);
	n = int(input());
	a.append(n);
print('Xuất list');
for i in a:
	print(i, end = " ");
print();

# Bài 2 kiểm tra phần tử trong list
# From Vũ Minh Hiếu 

print('Nhập vào phần tử muốn kiểm tra');
n = int(input());
h = -1;
p = [];
for i in range(0,len(a)):
	if(a[i] == n):
		p.append(i);
		h = i;
if(h != -1 and len(p) == 1):
	print('Vị trí xuất hiện của', n, ' là: ',h);
elif(h != -1 and len(p) > 1):
	print('Vị trí xuất hiện của', n, ' là: ', end = '');
	for i in p:
		print(i, end = ' ');
	print();
else:
	print(n, ' Không xuất hiện trong list');

# Bài 3 Kiểm tra cặp chẵn liên tiếp (1)
# From Vũ Minh Hiếu 

k = 0;
m = 0;
while(k != len(a) - 2 + 1):
	h = [];
	h.append(a[k]);
	h.append(a[k + 1]);
	if(h[0] % 2 == 0 and h[1] % 2 == 0):
		m = m + 1;
	k = k + 1;
print('Số cặp chẵn trong list là: ', m);

# Bài 3 Kiểm tra cặp lẻ liên tiếp (2)
# From Vũ Minh Hiếu 

k = 0;
m = 0;
while(k != len(a) - 2 + 1):
	h = [];
	h.append(a[k]);
	h.append(a[k + 1]);
	if(h[0] % 2 != 0 and h[1] % 2 != 0):
		m = m + 1;
	k = k + 1;
print('Số cặp lẻ trong list là: ', m);

# Bài 4 chèn phần tử vào list
# From Vũ Minh Hiếu 

print('Nhập giá trị muốn chèn ở vị trí thứ 2: ');
m = int(input());
a.insert(2,m);
print('Nhập giá trị muốn chèn ở vị trí thứ 4: ');
m = int(input());
a.insert(4,m);
print('Xuất list')
for i in a:
	print(i, end = ' ');
print();