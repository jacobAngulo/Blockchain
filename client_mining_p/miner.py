import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof
def proof_of_work(last_proof):
    """
    Simple Proof of Work Algorithm
    - Find a number p' such that hash(pp') contains 4 leading
    zeroes, where p is the previous p'
    - p is the previous proof, and p' is the new proof
    """

    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof += 1

    return proof


def valid_proof(last_proof, proof):
    """
    Validates the Proof:  Does hash(last_proof, proof) contain 4
    leading zeroes?
    """
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    # return guess_hash[:6] == "000000"
    return guess_hash[:4] == "0000"


if __name__ == '__main__':
    coins = 0
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://127.0.0.1:5000"

    coins_mined = 0
    # Run forever until interrupted
    print('\n')
    while True:
        # TODO: Get the last proof from the server and look for a new one

        r = requests.get(url=f'{node}/last_proof')
        data = r.json()
        last_proof = data['last_proof']
        print(' last proof: ', last_proof)

        new_proof = proof_of_work(last_proof)
        print(' new proof: ', new_proof)

        p = requests.post(url=f'{node}/mine', json={"proof": new_proof})

        post_data = p.json()
        print(' post message: ', post_data['message'])

        if post_data['message'] == 'New Block Forged':
            coins = coins + 1

        print(' coins: ', coins, '\n')

        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass
