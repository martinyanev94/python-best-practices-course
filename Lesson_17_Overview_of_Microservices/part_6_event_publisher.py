class EventPublisher:
    def publish_event(self, event):
        # Send the event to a message broker or event bus.
        message_broker.send(event)

event = {"type": "OrderPlaced", "order_id": "12345"}
EventPublisher().publish_event(event)
