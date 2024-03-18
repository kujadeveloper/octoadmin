import secrets
import string
import hashlib
import json
import uuid

def generate_custom_random_key(length, use_punctuation=False):
    characters = string.ascii_letters + string.digits
    if use_punctuation:
        characters += string.punctuation
    return ''.join(secrets.choice(characters) for i in range(length))


def generate_random_string(length=6):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for _ in range(length))
    return random_string

def custom_hash(input_string):
    hasher = hashlib.new('sha256')
    hasher.update(input_string.encode())
    # Add more steps or manipulations here as needed
    return hasher.hexdigest()

def filters(request,response):
    filters = request.GET.get('filters', None)
    orderBy = request.GET.get('orderBy', '')
    sortBy = request.GET.get('sortBy', 'id')

    if orderBy=='desc':
        orderBy = '-'
    else:
        orderBy =''

    if filters is not None:
        flter = {}
        try:
            filters_ = json.loads(filters)
        except:
            filters_ = {}
        for item in filters_:
            if filters_[item]!='' and filters_[item] is not None:
                flter[item] = filters_[item]
            response = response.filter(**flter)
    response = response.order_by(orderBy+sortBy).all()
    return response

def generate_unique_id():
    return str(uuid.uuid4())