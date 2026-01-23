from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self, message: str) -> None:
        pass

class EmailNotification(Notification):
    def notify(self, message: str) -> None:
        print(f"Email Notification Sent: {message}")

class SMSNotification(Notification):
    def notify(self, message: str) -> None:
        print(f"SMS Notification Sent: {message}")

class PushNotification(Notification):
    def notify(self, message: str) -> None:
        print(f"Push Notification Sent: {message}")

class NotificationFactory:
    @staticmethod
    def get_notification(notification_type: str) -> Notification:
        if notification_type.lower() == "email":
            return EmailNotification()
        elif notification_type.lower() == "sms":
            return SMSNotification()
        elif notification_type.lower() == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")

if __name__ == "__main__":
    try:
        notification = NotificationFactory.get_notification("email")
        notification.notify("Welcome to our platform!")
        
        notification = NotificationFactory.get_notification("sms")
        notification.notify("Your OTP is 1234.")
        
        notification = NotificationFactory.get_notification("push")
        notification.notify("You have a new message.")
        
        notification = NotificationFactory.get_notification("fax")
        
    except ValueError as e:
        print(e)
