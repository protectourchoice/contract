# @version 0.3.6

"""
@title Bare-bones Token implementation
@notice Based on the ERC-20 token standard as defined at
        https://eips.ethereum.org/EIPS/eip-20
"""

from vyper.interfaces import ERC20


interface IUniswapV2Router02:
    # def factory() -> address: view
    def WETH() -> address: view

    def addLiquidityETH(
        _token: address,
        _amountTokenDesired: uint256,
        _amountTokenMin: uint256,
        _amountETHMin: uint256,
        _to: address,
        _deadline: uint256
    ) -> (uint256, uint256, uint256): payable

    def swapExactTokensForETHSupportingFeeOnTransferTokens(
        _amountIn: uint256,
        _amountOutMin: uint256,
        _path: DynArray[address, 3],
        _to: address,
        _deadline: uint256
    ): nonpayable

# interface IUniswapV2Factory:

#     def createPair(
#         _tokenA: address,
#         _tokenB: address
#     ) -> address: nonpayable


implements: ERC20


event Approval:
    owner: indexed(address)
    spender: indexed(address)
    value: uint256

event Transfer:
    sender: indexed(address)
    receiver: indexed(address)
    value: uint256

# Public generated getters
name: public(String[64])
symbol: public(String[32])
decimals: public(uint256)
totalSupply: public(uint256)
balanceOf: public(HashMap[address, uint256])
allowance: public(HashMap[address, HashMap[address, uint256]])
buyTax: public(uint256)
sellTax: public(uint256)
isTrading: public(bool)
hasPaused: public(bool)
owner: public(address)
devWallet: public(address)
launchedAt: public(uint256)
swapThreshold: public(uint256)
txLimit: public(uint256)
routerAddress: public(address)
botVestedAmount: public(uint8)

# Internal use var
WETH: address

@external
def __init__(
    _name: String[64], 
    _symbol: String[32], 
    _decimals: uint256, 
    _total_supply: uint256):
    init_supply: uint256 = _total_supply * 10 ** _decimals
    self.name = _name
    self.symbol = _symbol
    self.decimals = _decimals
    self.balanceOf[msg.sender] = init_supply
    self.totalSupply = _total_supply
    self.routerAddress = empty(address)
    self.buyTax = empty(uint256)
    self.sellTax = empty(uint256)
    self.isTrading = False
    self.hasPaused = False
    self.botVestedAmount = empty(uint8)
    self.owner = msg.sender
    self.devWallet = empty(address)
    self.launchedAt = empty(uint256)
    self.swapThreshold = empty(uint256)
    self.WETH = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
    # self.factory = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"
    self.txLimit = self.totalSupply * 2 / 100 * (10 ** self.decimals)
    log Transfer(ZERO_ADDRESS, msg.sender, _total_supply)

##########
# @dev Functions below for internal use
##########
@internal
def _isOwner() -> bool:
    """
    @dev Internal bool check for owner assert
    """
    assert msg.sender == self.owner, "ah ah ah, you didn't say the magic word"
    return True


@internal
def _transfer(_from: address, _to: address, _value: uint256):
    """
    @dev Internal shared logic for transfer
    """
    assert _from != empty(address)
    assert _to != empty(address)
    assert _value > 0
    assert self.isTrading, "Trading is not enabled"
    assert self.balanceOf[_from] >= _value, "Insufficient balance"
    assert _value <= self.txLimit
    if _from == self.routerAddress:
        self.balanceOf[_from] -= _value
        self.balanceOf[_to] += _value
    else:
        self._distributeTax(_from, _to, _value)
        # if self._shouldSwapback():
        #     self._swapBack()
    log Transfer(_from, _to, _value)


@internal
def _distributeTax(_from: address, _to: address, _value: uint256) -> bool:
    """
    @dev Internal function for the tax math distribution
    """
    self.balanceOf[_from] -= _value
    self.balanceOf[self] += _value * self.buyTax / 100  # Transfer tax amount to self(contract)
    self.balanceOf[_to] += (100 - self.buyTax) * _value / 100 # Transfer token amount minus tax to holder
    return True


@internal
def _transferFrom(_from: address, _to: address, _value: uint256):
    """
    @dev Internal shared logic for transferFrom
    """
    assert _value <= self.txLimit
    assert self.isTrading, "Trading is not enabled"
    assert self.balanceOf[_from] >= _value, "Insufficient balance"
    self._distributeTax(_from, _to, _value)

    log Transfer(_from, _to, _value)


@internal
def _shouldSwapback() -> bool:
    """
    @dev Check if next sell should swap back tokens from taxes held in contract
    """
    assert self.balanceOf[self] >= self.swapThreshold
    return True


@internal 
def _swapBack() -> bool:
    """
    @dev Internal function for swapping contract tokens for eth
         using uniswap router
    """
    router: IUniswapV2Router02 = IUniswapV2Router02(self.routerAddress)
    router.swapExactTokensForETHSupportingFeeOnTransferTokens(
        self.swapThreshold,
        0,
        [self, self.WETH],
        self.devWallet,
        block.timestamp + 4
    )
    return True

@internal
def _approve(_owner: address, _spender: address, _value: uint256):
    self.allowance[_owner][_spender] = _value


##########
# @dev Functions below are public functions
##########
@external
def approve(_spender : address, _value : uint256) -> bool:
    """
    @notice Approve an address to spend the specified amount of tokens on behalf of msg.sender
    @dev Beware that changing an allowance with this method brings the risk that someone may use both the old
         and the new allowance by unfortunate transaction ordering. One possible solution to mitigate this
         race condition is to first reduce the spender's allowance to 0 and set the desired value afterwards:
         https://github.com/ethereum/EIPs/issues/20#issuecomment-263524729
    @param _spender The address which will spend the funds.
    @param _value The amount of tokens to be spent.
    @return Success boolean
    """
    self.allowance[msg.sender][_spender] = _value
    log Approval(msg.sender, _spender, _value)
    return True


@external
def transfer(_to : address, _value : uint256) -> bool:
    """
    @notice Transfer tokens to a specified address
    @dev Vyper does not allow underflows, so attempting to transfer more
         tokens than an account has will revert
    @param _to The address to transfer to
    @param _value The amount to be transferred
    @return Success boolean
    """
    self._transfer(msg.sender, _to, _value)
    return True


@external
def transferFrom(_from : address, _to : address, _value : uint256) -> bool:
    """
    @notice Transfer tokens from one address to another
    @dev Vyper does not allow underflows, so attempting to transfer more
         tokens than an account has will revert
    @param _from The address which you want to send tokens from
    @param _to The address which you want to transfer to
    @param _value The amount of tokens to be transferred
    @return Success boolean
    """
    assert self.allowance[_from][msg.sender] >= _value, "Insufficient allowance"
    self.allowance[_from][msg.sender] -= _value
    self._transfer(_from, _to, _value)
    return True

##########
# @dev Functions below are owner only
##########
@external
def canTrade():
    """
    @dev Owner only function to enable trading
    """
    self._isOwner()
    self.launchedAt = block.timestamp
    self.isTrading = True

@external
def manualSwapBack() -> bool:
    """
    @dev Manual swapBack for tokens stuck in contract from tax
         Limited to swap threshold so it cannot sell a large chunk
         Good use for launch as well.
    """
    self._isOwner()
    self._swapBack()
    return True

@external
def pauseTrading():
    """
    @dev Owner only function that only be called once for emergency use
         will increase pause counter to one and will revert if counter is above zero
    """
    self._isOwner()
    assert self.hasPaused == False
    self.hasPaused = True
    self.isTrading = False

@external
def setSwapThreshold(_value: uint256):
    """
    @dev Owner only function to set swap threshold for tax sells
         Tax amount must be less than 1% of total supply
    @param _value is an int less than ten. This is a percentage
            based on 1000 points  
    """
    self._isOwner()
    assert _value < 10
    self.swapThreshold = self.totalSupply * _value / 1000

@external
def setTaxes(_buyTaxValue: uint256, _sellTaxValue: uint256):
    """
    @dev Owner only function to set tax amounts
        cannot exceed 30
    """
    self._isOwner()
    assert _sellTaxValue + _buyTaxValue <= 25, "More than 25% round trip is gross"
    self.buyTax = _buyTaxValue
    self.sellTax = _sellTaxValue
    
@external
def setDevWallet(_newWallet: address) -> bool:
    """
    @dev Owner only function to set new developer wallet
    """
    self._isOwner()
    self.devWallet = _newWallet
    return True

@external
def setRouter(_address: address) -> bool:
    """
    @dev Set router in case of uniswap upgrade
    @param _address Router address 
    """
    self._isOwner()
    self.routerAddress = _address
    return True

@external
@payable
def addLiquidity():
    """
    @dev Owner only function to add liquidity
    """
    self._isOwner()
    assert self.routerAddress != empty(address)
    self._approve(self, self.routerAddress, max_value(uint256))
    router: IUniswapV2Router02 = IUniswapV2Router02(self.routerAddress)
    self._transfer(self.owner, self, self.totalSupply / 2)
    router.addLiquidityETH(
        self,
        self.totalSupply / 2,
        0,
        1,
        self.owner,
        block.timestamp + 5,
        value=msg.value
        )


