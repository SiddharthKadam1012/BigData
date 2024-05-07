from confluent_kafka import Producer
import json

def produce_inventory_order():
    # Configure the Kafka producer: 
    kafka_config = {'bootstrap.servers': 'localhost:9092'}

    # Create a new Kafka producer.
    producer = Producer(kafka_config)

    #Simulate inventory event data (replace with the actual data source).
    inventory_events = [
        {"type": "inventory", "item_id": "123", "quantity": 10},
        {"type": "inventory", "item_id": "456", "quantity": 20}
    ]

    # Send inventory events to the Kafka topic.
    for event in inventory_events:
        producer.produce('inventory_orders', json.dumps(event).encode('utf-8'))

    #  Flush the producer to send messages.
    producer.flush()

def produce_delivery_order():
    # Configure the Kafka producer: 
    kafka_config = {'bootstrap.servers': 'localhost:9092'}

    # Create a new Kafka producer.
    producer = Producer(kafka_config)

    # Simulate inventory event data (replace with the actual data source).
    delivery_events = [
        {"type": "delivery", "order_id": "1001", "status": "pending"},
        {"type": "delivery", "order_id": "1002", "status": "shipped"}
    ]

    # Send inventory events to the Kafka topic.
    for event in delivery_events:
        producer.produce('delivery_orders', json.dumps(event).encode('utf-8'))

    #  Flush the producer to send messages.
    producer.flush()

# Produce inventory and delivery orders
produce_inventory_order()
produce_delivery_order()
