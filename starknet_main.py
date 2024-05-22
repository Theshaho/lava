import requests, time, random, rpc

# Define the JSON-RPC method and parameters
method = "starknet_blockNumber"
params = {} 
tx_counter = 0

# Create JSON-RPC payload
payload = {
    "jsonrpc": "2.0",
    "method": method,
    "params": params,
    "id": 1,
}

def get_blockNumber():
    # Make the JSON-RPC request using the requests library
    response = requests.post(rpc.stark_main_endpoint, json=payload)

    # Parse the response
    result = response.json()

    # get current block number
    block_number = result['result']

    # Print the result
    print(f'Current Starknet block number is: {block_number}')

while True:
    # Increase the transaction coutner
    tx_counter += 1
    print(f"Transaction no: {tx_counter}")

    try:
        get_blockNumber()
    except Exception as e:
        print("An error occurred:", e)
    
    # Generate a random delay between 60 and 90 seconds
    random_delay = random.randint(60, 90)
    print(f"Waiting for {random_delay} seconds...")

    # Wait for the random delay finish before looping again
    time.sleep(random_delay) 
