from uniswap import Uniswap
#https://uniswap-python.com/getting-started.html?highlight=route
address = None          # or None if you're not going to make transactions
private_key = None  # or None if you're not going to make transactions
version = 2                       # specify which version of Uniswap to use
provider = "https://mainnet.infura.io/v3/7d42941339644de38358efdb8551e0ee"    # can also be set through the environment variable `PROVIDER`
uniswap = Uniswap(address=address, private_key=private_key, version=version, provider=provider)

# Some token addresses we'll be using later in this guide
eth = "0x0000000000000000000000000000000000000000"
bat = "0x0D8775F648430679A709E98d2b0Cb6250d2887EF"
dai = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
ohm = "0x383518188c0c6d7730d91b2c03a03c837814a899"
aave = "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"
# Returns the amount of DAI you get for 1 ETH (10^18 wei)




price = uniswap.get_price_input(aave, dai, 10**2)




print(price)