# Django and Python Signals & OOP Showcase
### (by Jayant Singh Jhala)

This project demonstrates answers to three Django signal-related interview questions and a Python OOP question regarding the `Rectangle` class. Below is an overview of each section, the code, and the expected outputs.

---

## Django Signal Questions

### 1. Are Django signals synchronous by default?

**Explanation**: By default, Django signals are executed synchronously. This means that the execution of the signal handler blocks further execution until the handler completes.

**Code Example**:

```python
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_synchronous(sender, instance, **kwargs):
    print(f"[Synchronous Signal] Signal received in thread: {threading.current_thread().name}")
    time.sleep(2)  # Introduce delay to simulate synchronous execution
    print("[Synchronous Signal] Signal processing done (synchronous)")
```

**Expected Output**:

```
[Synchronous Signal] Signal received in thread: MainThread
[Synchronous Signal] Signal processing done (synchronous)
```

This output confirms that the signal runs synchronously, blocking the execution for 2 seconds.

---

### 2. Do Django signals run in the same thread as the caller?

**Explanation**: Yes, Django signals run in the same thread as the caller. This can be verified by printing the thread name when the signal is executed.

**Code Example**:

```python
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_same_thread(sender, instance, **kwargs):
    print(f"[Same Thread Signal] Signal received in thread: {threading.current_thread().name}")
```

**Expected Output**:

```
[Same Thread Signal] Signal received in thread: MainThread
```

This output shows that the signal is executed in the `MainThread`, confirming it runs in the same thread as the process that triggered it.

---

### 3. Do Django signals run within the same database transaction as the caller?

**Explanation**: Yes, Django signals are executed within the same database transaction as the caller. If the signal is triggered inside an atomic block, it will also run inside the same transaction.

**Code Example**:

```python
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import transaction

@receiver(post_save, sender=User)
def signal_same_transaction(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("[Transaction Signal] Signal is within the same transaction")
```

**Expected Output**:

```
[Transaction Signal] Signal is within the same transaction
```

This output verifies that the signal is executed within the same transaction when inside an atomic block.

To add a new user, go to [http://127.0.0.1:8000/create_user/](http://127.0.0.1:8000/create_user/).
---

## Python OOP Question: Rectangle Class

**Explanation**: The `Rectangle` class allows for iterating over its dimensions (`length` and `width`) using Python's `__iter__()` method. Users can submit length and width values through a form, and the dimensions are displayed dynamically on the page.

**Code Example**:

```python
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
```

### Rectangle Dimensions via User Input

**Explanation**: This part of the project allows users to input the dimensions of a rectangle through an HTML form, and the server responds with the calculated dimensions.

**View Code**:

```python
from django.shortcuts import render

def rectangle_view(request):
    if request.method == 'POST':
        length = int(request.POST.get('length'))
        width = int(request.POST.get('width'))

        rect = Rectangle(length, width)
        dimensions = list(rect)

        return render(request, 'rectangle.html', {'dimensions': dimensions, 'length': length, 'width': width})
    
    return render(request, 'rectangle.html', {})
```

You can test this feature by submitting length and width values via the form located at `http://127.0.0.1:8000/rectangle/`.

