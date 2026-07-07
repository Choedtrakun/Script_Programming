# Week 3 Snapshot: Control Flow — Loops

## ทำไมเราต้องมี Loops?

ลองนึกภาพว่าอยากพิมพ์คำว่า "สวัสดี" ออกมา 100 ครั้ง ถ้าไม่มี loop เราต้องเขียน `print("สวัสดี")` ซ้ำ 100 บรรทัด! Loop ช่วยให้เราสั่งให้คอมพิวเตอร์ทำงานซ้ำๆ โดยเขียนโค้ดแค่ครั้งเดียว เหมาะกับงานที่ต้อง**ทำซ้ำ**หรือ**ประมวลผลข้อมูลจำนวนมาก**

```python
# ไม่มี loop (แย่มาก อย่าทำแบบนี้)
print("สวัสดี")
print("สวัสดี")
print("สวัสดี")
# ... ซ้ำไปเรื่อยๆ 100 ครั้ง

# มี loop (ดีกว่ามาก)
for i in range(100):
    print("สวัสดี")
```

---

## 1. for Loop — วนซ้ำตามจำนวนที่รู้แน่นอน

### โครงสร้างพื้นฐาน
```python
for item in sequence:
    # ทำอะไรบางอย่างกับ item
```

`for` loop ใช้เมื่อเรารู้ว่าต้องวนกี่รอบ หรือมี "ชุดข้อมูล" ที่จะวนไล่ทีละตัว

### ทำความรู้จัก range()

`range()` คือฟังก์ชันที่สร้างลำดับตัวเลข มี 3 รูปแบบ:

**แบบที่ 1: `range(stop)`** — เริ่มจาก 0 ไปจนถึง (แต่ไม่รวม) stop
```python
for i in range(5):
    print(f"รอบที่ {i}")
# ผลลัพธ์: 0, 1, 2, 3, 4  (ไม่มี 5 นะ! เพราะไม่รวมตัวสุดท้าย)
```

**แบบที่ 2: `range(start, stop)`** — เริ่มจาก start ไปจนถึง (ไม่รวม) stop
```python
for num in range(1, 11):
    print(num)
# ผลลัพธ์: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

**แบบที่ 3: `range(start, stop, step)`** — เพิ่มทีละ step
```python
for even_num in range(0, 11, 2):
    print(even_num)
# ผลลัพธ์: 0, 2, 4, 6, 8, 10  (กระโดดทีละ 2)
```

> **จุดที่มือใหม่มักพลาด**: `range(1, 5)` จะได้ 1, 2, 3, 4 เท่านั้น **ไม่มี 5** เพราะ stop ไม่ถูกนับรวม ถ้าอยากให้ถึง 5 ต้องเขียน `range(1, 6)`

### วนซ้ำ string ได้ด้วย
```python
my_string = "Python"
for char in my_string:
    print(f"ตัวอักษร: {char}")
# ผลลัพธ์: ตัวอักษร: P, ตัวอักษร: y, ตัวอักษร: t, ... (ทีละตัว)
```

### ตัวอย่างการใช้งานจริง: บวกเลข 1-5
```python
total_sum = 0
for i in range(1, 6):       # 1, 2, 3, 4, 5
    total_sum += i           # เท่ากับ total_sum = total_sum + i
print(f"ผลรวม: {total_sum}")  # ผลลัพธ์: 15
```

---

## 2. while Loop — วนซ้ำจนกว่าเงื่อนไขจะเป็นเท็จ

### โครงสร้างพื้นฐาน
```python
while condition:
    # ทำงานซ้ำ ตราบใดที่ condition ยังเป็น True
```

`while` ใช้เมื่อเรา**ไม่รู้ล่วงหน้า**ว่าจะต้องวนกี่รอบ — ขึ้นอยู่กับเงื่อนไข เช่น รอผู้ใช้กรอกค่าที่ถูกต้อง

### ⚠️ กฎเหล็ก 3 ข้อ ที่ต้องมีเสมอ (ไม่งั้น loop จะไม่จบ!)
1. **Initialization** — ตั้งค่าตัวแปรเริ่มต้นก่อนเข้า loop
2. **Condition** — เงื่อนไขที่ใช้เช็คว่าจะวนต่อไหม
3. **Update** — ต้องมีการเปลี่ยนค่าตัวแปรในแต่ละรอบ ไม่งั้นเงื่อนไขจะเป็นจริงตลอดไป

```python
count = 5          # 1. Initialization
while count > 0:   # 2. Condition
    print(f"นับถอยหลัง: {count}")
    count -= 1      # 3. Update (ถ้าลืมบรรทัดนี้ = infinite loop!)
print("บึ้ม!")
```

### ตัวอย่าง: รอผู้ใช้กรอกค่าที่ถูกต้อง (Input Validation)
```python
user_input = ""
while not (user_input == "yes" or user_input == "no"):
    user_input = input("กรุณาพิมพ์ 'yes' หรือ 'no': ").lower()
print(f"คุณพิมพ์: {user_input}")
```
ตรงนี้เราไม่รู้ว่าผู้ใช้จะพิมพ์ถูกตอนไหน — เลยต้องใช้ `while` แทน `for`

### ⚠️ ระวัง Infinite Loop!
```python
# อย่าทำแบบนี้! — โค้ดนี้จะวนไม่มีที่สิ้นสุด
counter = 0
while counter < 5:
    print(counter)
    # ลืมเพิ่มค่า counter! -> counter จะเป็น 0 ตลอดไป -> เงื่อนไขเป็น True ตลอด
```

---

## 3. break และ continue — ควบคุมการวนซ้ำ

| คำสั่ง | ความหมาย |
|---|---|
| `break` | **หยุด loop ทันที** ออกจาก loop เลย ไม่สนใจรอบที่เหลือ |
| `continue` | **ข้ามแค่รอบนี้** ไปเริ่มรอบถัดไปเลย (ไม่หยุดทั้ง loop) |

### ตัวอย่าง break: เกมทายเลข
```python
secret_number = 7
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    guess = int(input(f"ทายเลข (ครั้งที่ {attempts + 1}/{max_attempts}): "))
    attempts += 1
    
    if guess == secret_number:
        print("ยินดีด้วย! ทายถูก!")
        break   # ทายถูกแล้ว ออกจาก loop ทันที ไม่ต้องรอครบ 3 ครั้ง
    elif guess < secret_number:
        print("น้อยไป!")
    else:
        print("มากไป!")
else:
    # else ของ while จะทำงาน "เฉพาะตอนที่ loop จบโดยไม่มี break"
    print(f"เสียใจด้วย หมดโอกาสแล้ว เลขลับคือ {secret_number}")
```

### ตัวอย่าง continue: แสดงเฉพาะเลขคู่
```python
for i in range(1, 11):
    if i % 2 != 0:      # ถ้าเป็นเลขคี่
        continue         # ข้ามไปเลย ไม่ print
    print(f"เลขคู่: {i}")
# ผลลัพธ์: เลขคู่: 2, เลขคู่: 4, เลขคู่: 6, เลขคู่: 8, เลขคู่: 10
```

---

## 4. Nested Loops — Loop ซ้อน Loop

Loop ข้างในจะวนจน**ครบทุกรอบ**ก่อน แล้ว loop ข้างนอกถึงจะขยับไปรอบต่อไป เหมาะกับงานที่เกี่ยวกับตาราง, กริด, หรือลวดลาย 2 มิติ

### ตัวอย่าง: สี่เหลี่ยมดอกจัน 5x5
```python
size = 5
for row in range(size):        # loop นอก = แถว
    for col in range(size):    # loop ใน = คอลัมน์
        print("*", end="")     # end="" = ไม่ขึ้นบรรทัดใหม่
    print()                     # ขึ้นบรรทัดใหม่หลังจบแต่ละแถว
```
ผลลัพธ์:
```
*****
*****
*****
*****
*****
```

### ตัวอย่าง: สามเหลี่ยมมุมฉาก
```python
height = 5
for row in range(1, height + 1):   # แถวที่ 1 ถึง 5
    for col in range(row):          # แถวที่ N พิมพ์ N ดอกจัน
        print("*", end="")
    print()
```
ผลลัพธ์:
```
*
**
***
****
*****
```

### ตัวอย่าง: ตารางสูตรคูณ (การใช้งานจริง)
```python
for i in range(1, 13):           # loop นอก = แถว (1-12)
    for j in range(1, 13):       # loop ใน = คอลัมน์ (1-12)
        print(f"{i*j:4d}", end="")  # จัดตำแหน่งให้เป็นระเบียบ
    print()
```

---

## 5. Advanced Topic: Generators (yield) — เสริมความรู้

Generator คือฟังก์ชันพิเศษที่ "คืนค่าทีละตัว" แทนที่จะสร้าง list ทั้งหมดมาเก็บใน memory พร้อมกัน — ประหยัดหน่วยความจำมาก โดยเฉพาะกับข้อมูลจำนวนมากหรือไม่มีที่สิ้นสุด

```python
def fibonacci():
    a, b = 1, 1
    while True:          # วนไม่มีที่สิ้นสุด!
        yield a           # คืนค่า a แล้ว "หยุดรอ" ตรงนี้ จนกว่าจะถูกเรียกอีกครั้ง
        a, b = b, a + b

# ดึงมาแค่ 10 ตัวแรก ด้วย islice (ไม่งั้นจะวนไม่จบ)
from itertools import islice
first_ten = list(islice(fibonacci(), 10))
print(first_ten)
# ผลลัพธ์: [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
```

**จุดสำคัญ**: `yield` ต่างจาก `return` ตรงที่ฟังก์ชันจะ "หยุดชั่วคราว" แล้วค่อยทำงานต่อจากจุดเดิมในครั้งถัดไปที่ถูกเรียก ไม่ใช่เริ่มใหม่ทั้งหมด
