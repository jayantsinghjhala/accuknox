import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading
from django.db import transaction

# Q1: Signal is executed synchronously
@receiver(post_save, sender=User)
def signal_synchronous(sender, instance, **kwargs):
     print(f"[Synchronous Signal] Signal received in thread: {threading.current_thread().name}")
     time.sleep(2)  # Introduce a delay to simulate synchronous execution
     print("[Synchronous Signal] Signal processing done (synchronous)")

# Q2: Signal runs in the same thread as the caller
@receiver(post_save, sender=User)
def signal_same_thread(sender, instance, **kwargs):
    print(f"[Same Thread Signal] Signal received in thread: {threading.current_thread().name}")

# Q3: Signal runs within the same transaction
@receiver(post_save, sender=User)
def signal_same_transaction(sender, instance, **kwargs):
    if transaction.get_connection().in_atomic_block:
        print("[Transaction Signal] Signal is within the same transaction")