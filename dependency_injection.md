# 🪄 Dependency Injection in Python (Beginner-Friendly)

This guide introduces **Dependency Injection (DI)** in Python — what it is, why it matters, and how to use it to write modular, testable, and maintainable code.  
We’ll also learn how to wire services together in `__init__.py` and how to test them with `pytest`.

---

## 💡 What is Dependency Injection?

**Dependency Injection (DI)** is the practice of giving a class the things it needs (its *dependencies*) **from the outside** instead of creating them internally.

### ✅ Benefits:
- Makes your code **easier to test**.
- Allows you to **swap implementations** without touching the class logic.
- Keeps code **cleaner, modular, and maintainable**.

---

## 🔒 Without DI (Tight Coupling)

```python
class NotificationService:
    def __init__(self):
        # creates its own dependency
        self.email_sender = EmailSender()

    def notify(self, email, message):
        self.email_sender.send(email, "Notice", message)
```

🚨 **Problems:**
- Hard to test — always uses the real `EmailSender`.
- Hard to replace `EmailSender` with a different implementation.

---

## ✅ With DI (Constructor Injection)

```python
class NotificationService:
    def __init__(self, email_sender):  # dependency is injected
        self.email_sender = email_sender

    def notify(self, email, message):
        self.email_sender.send(email, "Notice", message)
```

Now you can inject different implementations:

```python
service = NotificationService(EmailSender())       # production
service = NotificationService(FakeEmailSender())   # testing
```

---

## 📦 Wiring Multiple Services with `__init__.py`

Let’s organize our app and wire up services in one place (known as the **composition root**):

```
myapp/
├── __init__.py
├── email_sender.py
├── sms_sender.py
├── notification_service.py
└── user_service.py
```

---

### `email_sender.py`

```python
class EmailSender:
    def send(self, to, subject, body):
        print(f"[EMAIL to={to}] {subject} - {body}")
```

---

### `sms_sender.py`

```python
class SmsSender:
    def send(self, number, message):
        print(f"[SMS to={number}] {message}")
```

---

### `notification_service.py`

```python
class NotificationService:
    def __init__(self, email_sender, sms_sender):
        self.email_sender = email_sender
        self.sms_sender = sms_sender

    def notify_by_email(self, email, message):
        self.email_sender.send(email, "Notice", message)

    def notify_by_sms(self, phone, message):
        self.sms_sender.send(phone, message)
```

---

### `user_service.py`

```python
class UserService:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def onboard_user(self, email, phone):
        print(f"Onboarding {email}")
        self.notification_service.notify_by_email(email, "Welcome!")
        self.notification_service.notify_by_sms(phone, "Welcome via SMS!")
```

---

### `__init__.py`

```python
from .email_sender import EmailSender
from .sms_sender import SmsSender
from .notification_service import NotificationService
from .user_service import UserService

# Instantiate dependencies
email_sender = EmailSender()
sms_sender = SmsSender()

# Wire into NotificationService
notification_service = NotificationService(email_sender, sms_sender)

# Wire into UserService
user_service = UserService(notification_service)

# Expose top-level services
__all__ = ["notification_service", "user_service"]
```

---

### `main.py`

```python
from myapp import user_service

user_service.onboard_user("intern@example.com", "+123456789")
```

---

## 🧪 Testing with `pytest`

Instead of using real senders in tests, we inject **fakes**:

### `tests/fakes.py`

```python
class FakeEmailSender:
    def __init__(self):
        self.sent = []

    def send(self, to, subject, body):
        self.sent.append((to, subject, body))


class FakeSmsSender:
    def __init__(self):
        self.sent = []

    def send(self, number, message):
        self.sent.append((number, message))
```

---

### `tests/test_user_service.py`

```python
import pytest
from myapp.user_service import UserService
from myapp.notification_service import NotificationService
from tests.fakes import FakeEmailSender, FakeSmsSender

@pytest.fixture
def user_service():
    fake_email = FakeEmailSender()
    fake_sms = FakeSmsSender()
    notification_service = NotificationService(fake_email, fake_sms)
    return UserService(notification_service), fake_email, fake_sms

def test_onboard_user_sends_notifications(user_service):
    service, fake_email, fake_sms = user_service

    service.onboard_user("intern@example.com", "+123456789")

    assert fake_email.sent == [
        ("intern@example.com", "Notice", "Welcome!")
    ]
    assert fake_sms.sent == [
        ("+123456789", "Welcome via SMS!")
    ]
```

---

### 🧪 Run the Tests

```bash
pytest -v
```

✅ Expected output:

```
tests/test_user_service.py::test_onboard_user_sends_notifications PASSED
```

---

## 🚀 Key Takeaways

- **Constructor injection** = pass dependencies via `__init__`.
- `__init__.py` can act as a **composition root** where everything is wired together.
- In tests, inject **fakes** or **mocks** instead of real dependencies.
- Your code becomes **modular, testable, and easy to maintain**.

---

## 📚 Further Reading

- [Martin Fowler – Inversion of Control Containers and the Dependency Injection pattern](https://martinfowler.com/articles/injection.html)
- [pytest documentation](https://docs.pytest.org/)
