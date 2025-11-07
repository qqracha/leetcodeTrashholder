import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,5,3,8,6]

def changes():
    global y
    y = [1,2,3,1,5]

changes()
print('Apply changes...')

plt.plot(x,y,marker='o',linestyle='-',color='green')
plt.title('Simple graf XY')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()