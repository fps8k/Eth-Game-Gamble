from brownie import Game, accounts, network, config

def deploy():
   account = getAccount()

   print("Deploying...")

   deploy = Game.deploy({"from": account}, publish_source=True)


   print(f"Deployed at {deploy.address} !!!")

   title = "Game"
   link = "https://rinkeby.etherscan.io/address/"
   with open("../Deployment Address.txt", "a+") as file:
      file.write(f"{title} => {link}{deploy.address}\n\n")


def getAccount():
   if network.show_active() == "development":
      return accounts[0]
   else:
      return accounts.add(config['wallet']['from_key'])

def main():
   deploy()