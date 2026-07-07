## Week 3 Snapshot · Code Snippets (ภาษาไทย)
**Control Flow: Loops + Generators**

### 1. for Loop กับ `range()`

`range()` ใช้กำหนดจำนวนรอบการวนซ้ำได้ 3 แบบ: กำหนดแค่จุดสิ้นสุด, กำหนดจุดเริ่ม-จุดสิ้นสุด, หรือกำหนดขั้นกระโดด (step) เพิ่มเติม

```python
# range(stop): เริ่มจาก 0 ถึงก่อน stop
for i in range(5):
    print(f"รอบที่ {i}")
# Output: 0, 1, 2, 3, 4

# range(start, stop): เริ่มจาก start ถึงก่อน stop
for num in range(1, 11):
    print(num)
# Output: 1 ถึง 10

# range(start, stop, step): กระโดดทีละ step
for even_num in range(0, 11, 2):
    print(even_num)
# Output: 0, 2, 4, 6, 8, 10
```

**วนซ้ำทีละตัวอักษรในสตริง**
```python
my_string = "Python"
for char in my_string:
    print(f"ตัวอักษร: {char}")
```

---

### 2. while Loop

ใช้เมื่อไม่รู้จำนวนรอบล่วงหน้า แต่รู้ **เงื่อนไข** ที่จะหยุด — ต้องมีการอัปเดตค่าตัวแปรเงื่อนไขทุกครั้ง ไม่เช่นนั้นจะเป็น **infinite loop**

```python
# นับถอยหลัง
count = 5
while count > 0:
    print(f"เหลืออีก: {count}")
    count -= 1   # ขาดบรรทัดนี้ = วนไม่รู้จบ
print("หมดเวลา!")
```

**ตรวจสอบ input ของผู้ใช้**
```python
user_input = ""
while not (user_input == "yes" or user_input == "no"):
    user_input = input("กรุณาพิมพ์ 'yes' หรือ 'no': ").lower()
print(f"คุณพิมพ์ว่า: {user_input}")
```

---

### 3. Loop Control: `break` และ `continue`

- `break` → หยุดลูปทันที
- `continue` → ข้ามรอบปัจจุบัน ไปรอบถัดไป
- `while...else` → บล็อก `else` จะทำงานก็ต่อเมื่อลูปจบครบโดย**ไม่มี** `break`

```python
secret_number = 7
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input(f"ทายเลข (1-10) - ครั้งที่ {attempts + 1}/{max_attempts}: "))
    attempts += 1
    if guess == secret_number:
        print("ถูกต้อง! ยินดีด้วย")
        break
    elif guess < secret_number:
        print("น้อยไป!")
    else:
        print("มากไป!")
else:
    print(f"หมดโอกาสแล้ว เลขลับคือ {secret_number}")
```

```python
# continue: แสดงเฉพาะเลขคู่
for i in range(1, 11):
    if i % 2 != 0:
        continue   # ข้ามเลขคี่
    print(f"เลขคู่: {i}")
```

---

### 4. Nested Loops (ลูปซ้อนลูป)

ลูปวงในจะวนจนครบก่อน แล้วลูปวงนอกถึงจะขยับไปรอบถัดไป — เหมาะกับงานที่เป็นตาราง/กริด

```python
# สี่เหลี่ยมจัตุรัสดอกจัน 5x5
size = 5
for row in range(size):
    for col in range(size):
        print("* ", end="")
    print()
```

```python
# สามเหลี่ยมมุมฉาก
height = 5
for row in range(1, height + 1):
    for col in range(row):
        print("* ", end="")
    print()
```

```python
# ตารางสูตรคูณ 12x12
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i*j:4d}", end="")
    print()
```

---

### 5. Generators — ทางลัดของ Loop ที่ประหยัดหน่วยความจำ

**Generator function** ใช้ `yield` แทน `return` — ค่าจะถูกสร้าง "ทีละตัวตามที่ขอ" ไม่สร้างทั้ง list ทีเดียว จึงประหยัดหน่วยความจำกว่า

```python
def squares_gen():
    for x in range(10):
        yield x**2

g = squares_gen()
print(g)          # <generator object ...> — ยังไม่รันจนกว่าจะถูกดึงค่า
print(next(g))    # 0
print(next(g))    # 1
```

**Generator expression** — เหมือน list comprehension แต่ใช้วงเล็บ `()` แทน `[]`
```python
gen = (x**2 for x in range(10))
print(sum(gen))   # 285 — คำนวณค่าทีละตัว ไม่เก็บ list เต็มไว้ในหน่วยความจำ
```

**เชื่อมกับเรื่อง loop: generator ก็ใช้ `for` วนได้เหมือน list**
```python
for val in (x**2 for x in range(5)):
    print("ได้ค่า:", val)
```

**Infinite sequence** — จุดที่ generator ต่างจาก list ชัดที่สุด: ลูป `while True` + `yield` สร้างลำดับที่ไม่มีวันจบได้ โดยไม่ทำให้โปรแกรมค้าง (ตราบใดที่ไม่ดึงค่าจนหมด)

```python
def integers_from(n):
    while True:
        yield n
        n += 1

nums = integers_from(1)
first_five = [next(nums) for _ in range(5)]
print(first_five)   # [1, 2, 3, 4, 5]
```

**Fibonacci ด้วย generator** (ตัวอย่างคลาสสิกที่โชว์พลังของ `while True` + `yield`)
```python
def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
first_ten = list(islice(fibonacci(), 10))
print(first_ten)   # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

---

### สรุปจุดเชื่อมสำคัญของสัปดาห์นี้

Loop (`for`/`while`) คือกลไกควบคุมการทำงานซ้ำ ส่วน **Generator เป็นการนำแนวคิดของ loop มาห่อไว้ในฟังก์ชันที่ "จำสถานะ" ของตัวเองได้** — แทนที่จะรันลูปแล้วเก็บผลทุกตัวลง list ทันที (`return`) generator จะ "หยุดพัก" ที่ `yield` แล้วค่อยทำงานต่อเมื่อถูกเรียก `next()` อีกครั้ง ทำให้สามารถสร้างลำดับที่ยาวมาก หรือไม่มีที่สิ้นสุดได้ โดยใช้หน่วยความจำคงที่