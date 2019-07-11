import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof


if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    print('\n')
    while True:
        # TODO: Get the last proof from the server and look for a new one

        r = requests.get(url=f'{node}/last_proof')
        data = r.json()
        last_proof = data['last_proof']
        print(' last proof: ', last_proof, '\n')

        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass
