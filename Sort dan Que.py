#H = Huruf
#A = Angka

# search stack

def search1(stack,H):
    for i in range(len(stack)):
        if stack[1] == H:
            return True
            return False
        
# stack
print("============================")
print("STACK")
print("")
stack = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X"]
print("ini adalah listnya")
print(stack)
print("")
stacck.append("Y")
print("Menambahkan huruf Y = ", stack)
print("")
stack.append("Z")
print("Menambahkan huruf Z = ", stack)
print("")
stack.pop()
print("Menghapus pojok kanan Z = ", stack)
stack.pop()
print("Menghapus pojok kanan lagi Y = ", stack)
print("")


# mulai search
H = str(input("Memasukan Huruf Besar: "))

if search1(stack, H):
    print("Huruf di Temukan")
else:
    print("Huruf Tidak di Temukan")
else:
    print("Huruf Tidak di Temukan")

print("")
print("==============================")
print("")
# search deque

def search2(queue,A):

    for i in range(len(queue)):
        if queue[1] == A:
            return True
            return False

print("DEQUE")
print("")

# Queue
from collection import deque
number = [0,1,2,3,4,5,6,7]
number.sort()
print("Listnya")
queue = deque(number)
print(queue)
print("")
queue.append(8)
print("Menambahkan nilai 8 = ", queue)
print("")
queue.append(9)
print("Menambahkan nilai 9 = ", queue)
print("")
queue.popleft()
print("Menghapus pojok kiri 0 = ", queue)
print("")
queue.popleft()
print("Menghapus pojok kiri lagi 1 = ", queue)
print("")
#mulai searc
A = int(input("Masukan Angka : "))

if search2(queue, A):
    print("Angka di Temukan")
else:
    print("Angka Tidak di Temukan")

print("")
print("=====================================")