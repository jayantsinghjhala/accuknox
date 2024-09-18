# Django and Python Signals & OOP Showcase

This project demonstrates answers to three Django signal-related interview questions and a Python OOP question regarding the `Rectangle` class. Below is an overview of each section and its corresponding code.

## Django Signal Questions

### 1. Are Django signals synchronous by default?
By default, Django signals are synchronous. This is demonstrated by introducing a delay in the signal receiver and showing that the signal blocks execution.

```
@receiver(post_save, sender=User)
def signal_synchronous(sender, instance, **kwargs):
    time.sleep(2)
    print("Signal processing done (synchronous)")
```

### 2. Do Django signals run in the same thread as the caller?
Yes, Django signals run in the same thread as the caller.

```
@receiver(post_save, sender=User)
def signal_same_thread(sender, instance, **kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")
```

### 3. Do Django signals run within the same database transaction as the caller?
Yes, Django signals run within the same transaction as the caller.

```
@receiver(post_save, sender=User)
def signal_same_transaction(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("Signal is within the same transaction")
```

### Python OOP Question: Rectangle Class
The Rectangle class allows for iterating over its dimensions.

```
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}
```

You can view the output by visiting http://localhost:8000/rectangle/