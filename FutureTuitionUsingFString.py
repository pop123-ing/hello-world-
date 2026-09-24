tuition=10000
year=0   #year=0

while tuition<20000:
    tuition=tuition*1.07
    year+=1

print("tuition will be doubled in", year," years.")
print(f"tuition will be ${tuition:.2f} in {year} years.")