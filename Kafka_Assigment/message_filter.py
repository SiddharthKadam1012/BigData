import json

def filter_inventory_message(message):
    """
    Filter inventory messages by 'type'.
    
    Args: Message (str): JSON-encoded string.
        
    Returns: bool: True for 'inventory' messages, False otherwise.

    """
    try:
        data = json.loads(message)
        return data.get('type') == 'inventory'
    except json.JSONDecodeError:
        return False

def filter_delivery_message(message):
    """
    Filter inventory messages by 'type'.
    
    Args: Message (str): JSON-encoded string.
        
    Returns: bool: True for 'delivery' messages, False otherwise.

    """
    try:
        data = json.loads(message)
        return data.get('type') == 'delivery'
    except json.JSONDecodeError:
        return False