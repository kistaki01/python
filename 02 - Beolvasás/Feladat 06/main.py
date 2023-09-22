print("kedvenc film:", end="")
title: str = input()

print("megjelenes eve:", end="")
realasedate: int = int(input())

print("rendezo neve:", end="")
director: str = input()

print("foszereplo:", end="")
mainc: str = input()

print(f'{realasedate}-ban {director} rendezesevel megjelent a/az {title} cimu film {mainc} foszereplesevel!')