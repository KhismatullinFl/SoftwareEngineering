s = input()

l = len(s)
print(l)

s = s.lower()
print(s)

al = 'aeiou'
count = 0
for i in s:
    if i in al:
       count += 1
print(count)

s = s.replace('ugly','beauty')
print(s)

if s.startswith("the") and s.endswith("end"):
    print(f'Предложение начинается с The и заканчивается на end.')
else:
    print(f'Предложение не начинается с The и заканчивается на end.')

