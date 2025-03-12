import argparse
import hashlib
import json
import os
from mnemonic import Mnemonic
from ecdsa import SigningKey, SECP256k1
import pyfiglet



print()
print(pyfiglet.figlet_format("Wallet", font="stforek", justify="center"))
print(pyfiglet.figlet_format("Generator", font="stforek", justify="center"))
print()
print()


def generate_wallets(count=1, words=12, output_file="wallets.json"):
    """
    Generate multiple Ethereum wallets.

    :param count: Jumlah wallet yang ingin dibuat
    :param words: Jumlah kata dalam mnemonic (12 atau 24)
    :param output_file: Nama file JSON untuk menyimpan hasil
    :return: List of generated wallets
    """
    if words not in [12, 24]:
        raise ValueError("Mnemonic hanya bisa 12 atau 24 kata.")

    mnemo = Mnemonic("english")
    new_wallets = []

    for _ in range(count):
        mnemonic_phrase = mnemo.generate(strength=128 if words == 12 else 256)

        seed = mnemo.to_seed(mnemonic_phrase)

        private_key = hashlib.sha256(seed).hexdigest()

        sk = SigningKey.from_string(bytes.fromhex(private_key), curve=SECP256k1)
        vk = sk.verifying_key
        public_key = b'\x04' + vk.to_string()

        address = hashlib.sha3_256(public_key).digest()[-20:]
        eth_address = "0x" + address.hex()

        new_wallets.append({
            "mnemonic": mnemonic_phrase,
            "private_key": private_key,
            "address": eth_address
        })

    if os.path.exists(output_file):
        with open(output_file, "r") as f:
            try:
                existing_wallets = json.load(f)
                if not isinstance(existing_wallets, list):
                    existing_wallets = []
            except json.JSONDecodeError:
                existing_wallets = []
    else:
        existing_wallets = []

    existing_wallets.extend(new_wallets)

    with open(output_file, "w") as f:
        json.dump(existing_wallets, f, indent=4)

    return new_wallets

def main():
    parser = argparse.ArgumentParser(description="Generate Ethereum wallets and save to a JSON file.")
    parser.add_argument("--create", type=int, default=1, help="Jumlah wallet yang ingin dibuat (default: 1)")
    parser.add_argument("--words", type=int, choices=[12, 24], default=12, help="Jumlah kata dalam mnemonic (12 atau 24, default: 12)")
    parser.add_argument("--file", type=str, default="wallets.json", help="Nama file JSON untuk menyimpan hasil (default: wallets.json)")
    
    args = parser.parse_args()

    wallets = generate_wallets(count=args.create, words=args.words, output_file=args.file)

    for i, wallet in enumerate(wallets):
        print("×" * os.get_terminal_size().columns)
        print("Mnemonic    : ", wallet["mnemonic"])
        print("Private Key : ", wallet["private_key"])
        print("Address     : ", wallet["address"])
        print()

    print(f"Wallet baru telah ditambahkan ke '{args.file}'")

if __name__ == "__main__":
    main()
          
