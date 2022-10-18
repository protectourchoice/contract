<table style="background-color: transparent; background-image: url(https://i.ibb.co/crxZMz2/arrows-removebg-preview.png); background-position: right bottom; background-repeat: no-repeat; background-size: contain; border: 0px solid transparent; margin: 0% 0% 0% 0%; padding: 0% 0% 0% 0%; table-layout: auto; width: 100%; height: 100%">
  <tr>
    <td style="border: 0px solid transparent">
      <h1>Protect Our Choice</h1>
      <h2>Token</h2>
      <h3>Security Assessment</h3>
      <h4>October 8th, 2022</h4>
      <h4 style="color: tomato">&nbsp;</h4>
    </td>
  </tr>
  <tr style="height: 1rem">
    <td style="border: 0px solid transparent"></td>
  </tr>
  <tr>
    <td style="border: 0px solid transparent">
      <b>Audited By</b>:
      <br>
      Angelos Apostolidis <br>
      <a href="mailto:angelos.apostolidis@ourovoros.io" style="color: rgb(249, 159, 28)">angelos.apostolidis@ourovoros.io</a>
      <br>
    </td>
  </tr>
  <tr style="height: 6rem">
    <td style="border: 0px solid transparent"></td>
  </tr>
</table>

<div style="page-break-after: always"></div>

## <img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/> Overview

### Project Summary

<table>
  <tr>
    <td style="width: 30%"><strong><span>Project Name</span></strong></td>
    <td><span>Protect Our Choice - Token</span></td>
  </tr>
  <tr>
    <td style="width: 30%"><strong><span>Website</span></strong></td>
    <td><a href="https://www.protectourchoice.org/">Protect Our Choice</a></td>
  </tr>
  <tr>
    <td><strong><span>Description</span></strong></td>
    <td><span>ERC-20 token extended by a LP acquisition mechanism</span></td>
  </tr>
  <tr>
    <td><strong><span>Platform</span></strong></td>
    <td><span>Ethereum; Vyper</span></td>
  </tr>
  <tr>
    <td><strong><span>Codebase</span></strong></td>
    <td><a href="https://github.com/protectourchoice/contract"><span>GitHub Repository</span></a></td>
  </tr>
  <tr>
    <td><strong><span>Commits</span></strong></td>
    <td>
      Pre-audit commit:<a href="https://github.com/protectourchoice/contract/commit/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f">8fc2f1fe98700fa48dc6bd42fb3b576a976a461f</a><br>
    </td>
    <td>
      Post-audit commit:<a href="https://github.com/protectourchoice/contract/commit/28b6739a44bc489644040828d0a1d49bf938b0bc">28b6739a44bc489644040828d0a1d49bf938b0bc</a><br>
    </td>
  </tr>
</table>

### Audit Summary

<table>
  <tr>
    <td style="width: 30%"><strong><span>Delivery Date</span></strong></td>
    <td><span>October 8th, 2022</span></td>
  </tr>
  <tr>
    <td><strong><span>Method of Audit</span></strong></td>
    <td><span>Manual Review</span></td>
  </tr>
</table>

### Vulnerability Summary

<table>
  <tr>
    <td style="width: 30%"><strong><span style="background-color: transparent; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> <span>Total Issues</span></strong></td>
    <td><span>29</span></td>
  </tr>
<tr>
    <td><strong><span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> <span>Total Major</span></strong></td>
    <td><span>5</span></td>
  </tr>
<tr>
    <td><strong><span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> <span>Total Minor</span></strong></td>
    <td><span>5</span></td>
  </tr>
<tr>
    <td><strong><span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> <span>Total Informational</span></strong></td>
    <td><span>19</span></td>
  </tr>
</table>

<div style="page-break-after: always"></div>

## <img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/> Files In Scope

| Contract | Location                                                                                                                            |
| :------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| Token.vy | [contracts/Token.vy](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy) |

## <img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/> Findings

<table style="table-layout: fixed">
  <tr style="height: 1em">
    <td style="width: 5.6em; text-align: right"><span>ID</span></td>
    <td><span>Title</span></td>
    <td style="width: 10.75em"><span>Type</span></td>
    <td style="width: 8.25em"><span>Severity</span></td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-01">F-01</a>
    </td>
    <td>Unlocked Compiler Version</td>
    <td>Language Specific</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-02">F-02</a>
    </td>
    <td>Wrong Interface Name</td>
    <td>Inconsistency</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-03">F-03</a>
    </td>
    <td>Potential Process Automation</td>
    <td>Coding Style</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-04">F-04</a>
    </td>
    <td>Token Decimals Bounds</td>
    <td>Language Specific</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-05">F-05</a>
    </td>
    <td>Mutability Specifiers Missing</td>
    <td>Gas Optimization</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-06">F-06</a>
    </td>
    <td>Ambiguous Modifier Implementation</td>
    <td>Language Specific</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-07">F-07</a>
    </td>
    <td>Duplicate Functionality</td>
    <td>Inconsistency, Coding Style</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-08">F-08</a>
    </td>
    <td>Missing Event Emission</td>
    <td>Volatile Code, Off-Chain Tracking</td>
    <td>
      <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-09">F-09</a>
    </td>
    <td>Static Code Optimization</td>
    <td>Gas Optimization</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-10">F-10</a>
    </td>
    <td>Incorrect Event Emission</td>
    <td>Volatile Code, Off-Chain Tracking</td>
    <td>
      <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-11">F-11</a>
    </td>
    <td>Redundant Variable</td>
    <td>Gas Optimization</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-12">F-12</a>
    </td>
    <td>Approved Transfer Extension</td>
    <td>Gas Optimization</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-13">F-13</a>
    </td>
    <td>Redundant Variable Initialization</td>
    <td>Coding Style</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-14">F-14</a>
    </td>
    <td>Ambiguous Pausable Functionality</td>
    <td>Volatile Code</td>
    <td>
      <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-15">F-15</a>
    </td>
    <td>Transferring Routes</td>
    <td>Inconsistency</td>
    <td>
      <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-16">F-16</a>
    </td>
    <td>Redundant State Look-Up</td>
    <td>Gas Optimization</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-17">F-17</a>
    </td>
    <td>Incorrect Math</td>
    <td>Inconsistency, Volatile Code</td>
    <td>
      <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-18">F-18</a>
    </td>
    <td>Ambiguous `NatSpec` Comment</td>
    <td>Inconsistency</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-19">F-19</a>
    </td>
    <td>Redundant Check</td>
    <td>Gas Optimization</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-20">F-20</a>
    </td>
    <td>Unused `internal` Function</td>
    <td>Dead Code</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-21">F-21</a>
    </td>
    <td>Redundant Storage</td>
    <td>Gas Optimization</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-22">F-22</a>
    </td>
    <td>Unused Returned Value</td>
    <td>Inconsistency, Coding Style</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-23">F-23</a>
    </td>
    <td>Router Unlimited Approval</td>
    <td>Volatile Code</td>
    <td>
      <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-24">F-24</a>
    </td>
    <td>Event Addition</td>
    <td>Language Specific</td>
    <td>
      <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-25">F-25</a>
    </td>
    <td>Privileged Ownership</td>
    <td>Centralization</td>
    <td>
      <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-26">F-26</a>
    </td>
    <td>Potential Sandwich Attack</td>
    <td>Volatile Code</td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-27">F-27</a>
    </td>
    <td>Inexistent Input Sanitization</td>
    <td>Logical Issue</td>
    <td>
      <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-28">F-28</a>
    </td>
    <td>Third Party Dependencies</td>
    <td>Control Flow </td>
    <td>
      <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational
    </td>
  </tr>
  <tr>
    <td style="text-align: right">
      <a href="#F-29">F-29</a>
    </td>
    <td>Ambiguous Limit Change</td>
    <td>Volatile Code</td>
    <td>
      <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major
    </td>
  </tr>
</table>

<div style="page-break-after: always"></div>

### <a name="F-01"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-01: Unlocked Compiler Version

| Type              | Severity                                                                                                                            | Location                                                                                                                                                           |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Language Specific | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L1](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L1)</span> |

#### <span class="informational">Description:</span>

The contract has unlocked compiler version. An unlocked compiler version in the source code of the contract permits the user to compile it at or above a particular version. This, in turn, leads to differences in the generated bytecode between compilations due to differing compiler version numbers. This can lead to an ambiguity when debugging as compiler specific bugs may occur in the codebase that would be hard to identify over a span of multiple compiler versions rather than a specific one.

#### <span class="informational">Recommendation:</span>

We advise that the compiler version is instead locked at the lowest version possible that the contract can be compiled at. For example, for version `v0.3.7` the contract should contain the following line:

```Solidity
# @version 0.3.7
```

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and locked the compiler to version `0.3.7`.

<div style="page-break-after: always"></div>

### <a name="F-02"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-02: Wrong Interface Name

| Type          | Severity                                                                                                                            | Location                                                                                                                                                             |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inconsistency | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L11](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L11)</span> |

#### <span class="informational">Description:</span>

The linked interface name is wrong, as the linked functionality refers to a different Uniswap interface.

#### <span class="informational">Recommendation:</span>

We advise to change the interface name to `IUniswapV2Router02`.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and changed the linked interface name to `IUniswapV2Router02`.

<div style="page-break-after: always"></div>

### <a name="F-03"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-03: Potential Process Automation

| Type         | Severity                                                                                                                            | Location                                                                                                                                                               |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Coding Style | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L112](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L112)</span> |

#### <span class="informational">Description:</span>

The code relevant to the Uniswap pair Ether liquidity addition is missing from the codebase. This is a two-step process whereby the Externally Owned Account (EOA) has to approve the Uniswap router for a specific token amount and then the same router is triggered pull the approved token and Ether amount.

#### <span class="informational">Recommendation:</span>

We advise add a function that programmatically increases the liquidity of the Liquidity Pool (LP). Such implementation takes away the human factor, hence lowering the margin of error and could minimize save gas used in the aforementioned process.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and added a function to add liquidity to the corresponding Liquidity Pool. Yet, because of the implementation, the `owner` address will accumulate a significant portion of the LP token over time.

<div style="page-break-after: always"></div>

### <a name="F-04"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-04: Token Decimals Bounds

| Type              | Severity                                                                                                                            | Location                                                                                                                                                             |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Language Specific | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L80](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L80)</span> |

#### <span class="informational">Description:</span>

Handling `ERC-20` token decimals can be an issue in Vyper. As described in [VVE-2020-0001](https://github.com/vyperlang/vyper/security/advisories/GHSA-mr6r-mvw4-736g), the typing system of the language cannot protect against the interface returning integer types. This could lead to unwanted behavior when the token is integrated into secondary DeFi protocols, like Decentralized Exchanges (DEXs).

#### <span class="informational">Recommendation:</span>

We advise to either bound the parameter `_decimals` that set the state variable `decimals` to `uint8` values or directly set the said state variable with a numeric literal.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and changed the type of the state variable `decimals` to `uint8`.

<div style="page-break-after: always"></div>

### <a name="F-05"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-05: Mutability Specifiers Missing

| Type             | Severity                                                                                                                            | Location                                                                                                                                                                                                                                                                                               |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gas Optimization | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L51-L54](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L51-L54), [L66](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L66)</span> |

#### <span class="informational">Description:</span>

The linked state variables are assigned to only once, during the `constructor`'s execution.

#### <span class="informational">Recommendation:</span>

We advise that the `immutable` mutability specifier is set at the variable's contract-level declaration to greatly optimize the gas cost of utilizing the variables.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and changed the mutability of the majority of the linked variables to `immutable`.

<div style="page-break-after: always"></div>

### <a name="F-06"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-06: Ambiguous Modifier Implementation

| Type              | Severity                                                                                                                            | Location                                                                                                                                                                         |
| :---------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Language Specific | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L102-L108](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L102-L108)</span> |

#### <span class="informational">Description:</span>

The `_checkOwner` internal function simulates the known Solidity modifier `onlyOwner`. Although this implementation achieves its goal, using both an `assert` statement on a conditional and returning `true` seems redundant.

#### <span class="informational">Recommendation:</span>

We advise either directly returning the conditional and using an `assert` statement on the code that utilizes this internal function, or removing the `return` statement.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and removed the `return` statement.

<div style="page-break-after: always"></div>

### <a name="F-07"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-07: Duplicate Functionality

| Type                        | Severity                                                                                                                            | Location                                                                                                                                                                                                                                                                                           |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inconsistency, Coding Style | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L230](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L230), [L268](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L268)</span> |

#### <span class="informational">Description:</span>

The linked assignments manually update the `allowance` state variable.

#### <span class="informational">Recommendation:</span>

We advise using the internal `_approve` function to increase the legibility of the codebase. Also, moving the event emission in the internal function is preferred.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references, adjusted the internal `_approve` function and used it in the externally-facing `approve` one.

<div style="page-break-after: always"></div>

### <a name="F-08"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-08: Missing Event Emission

| Type          | Severity                                                                                                                     | Location                                                                                                                                                       |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Volatile Code | <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor | <span class="minor">[Token.vy L268](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L268)</span> |

#### <span class="minor">Description:</span>

The `transferFrom` does not emit an `Approval` event after its allowance change. This can lead to inconsistencies to the off-chain services that keep track of the on-chain data.

#### <span class="minor">Recommendation:</span>

We advise emitting an `Approval` event inside the aforementioned function.

#### <span class="minor">Alleviation:</span>

The team opted to consider our references and added an `Approval` event emission inside the `transferFrom` function.

<div style="page-break-after: always"></div>

### <a name="F-09"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-09: Static Code Optimization

| Type             | Severity                                                                                                                            | Location                                                                                                                                                                         |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gas Optimization | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L110-L117](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L110-L117)</span> |

#### <span class="informational">Description:</span>

The `_getPair` internal function handles static code in order to set the value of the `tradingPair` state variable, hence redundantly taking up bytecode space.

#### <span class="informational">Recommendation:</span>

We advise moving the function's code in the constructor and changing the `tradingPair` state variable's mutability to immutable.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references, removed the `_getPair` internal function and used that function's code during the contract construction.

<div style="page-break-after: always"></div>

### <a name="F-10"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-10: Incorrect Event Emission

| Type                              | Severity                                                                                                                     | Location                                                                                                                                                     |
| :-------------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Volatile Code, Off-Chain Tracking | <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major | <span class="major">[Token.vy L96](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L96)</span> |

#### <span class="major">Description:</span>

The linked event emission incorrectly indicates that the deployer of the contract minted the total supply of the token.

#### <span class="major">Recommendation:</span>

We advise changing the token amount in the linked event to match the initial supply instead.

#### <span class="major">Alleviation:</span>

The team opted to consider our references and fixed the linked statement.

<div style="page-break-after: always"></div>

### <a name="F-11"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-11: Redundant Variable

| Type             | Severity                                                                                                                            | Location                                                                                                                                                             |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gas Optimization | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L82](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L82)</span> |

#### <span class="informational">Description:</span>

The linked variable is used only once.

#### <span class="informational">Recommendation:</span>

We advise removing the local variable and moving the initial supply calculation [L86](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L86).

#### <span class="informational">Alleviation:</span>

The team has acknowledged this exhibit but decided to use the aforementioned local variable throughout its scope, making this exhibit invalid.

<div style="page-break-after: always"></div>

### <a name="F-12"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-12: Approved Transfer Extension

| Type             | Severity                                                                                                                            | Location                                                                                                                                                               |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gas Optimization | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L268](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L268)</span> |

#### <span class="informational">Description:</span>

The `transferFrom` function can be extended to save gas when a user has unlimited approval.

#### <span class="informational">Recommendation:</span>

We advise checking the allowance the caller has from the token owner and, unless it's the maximum number of the `uint256` type, decrement the caller's allowance.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and implemented the proposed feature.

<div style="page-break-after: always"></div>

### <a name="F-13"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-13: Redundant Variable Initialization

| Type         | Severity                                                                                                                            | Location                                                                                                                                                                     |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Coding Style | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L88-L90](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L88-L90)</span> |

#### <span class="informational">Description:</span>

All variable types within Solidity are initialized to their default "empty" value, which is usually their zeroed out representation.

#### <span class="informational">Recommendation:</span>

We advise that the linked initialization statements are removed from the codebase to increase legibility.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and removed the redundant statements from the constructor.

<div style="page-break-after: always"></div>

### <a name="F-14"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-14: Ambiguous Pausable Functionality

| Type          | Severity                                                                                                                     | Location                                                                                                                                                                                                                                                                                           |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Volatile Code | <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major | <span class="major">[Token.vy L60](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L60), [L285-L295](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L285-L295)</span> |

#### <span class="major">Description:</span>

The token's pausability implementation does not block token transfers when the state variable is toggled to `true`. Also, `hasPaused` has no way of turning back to `false` to resume its normal course of action.

#### <span class="major">Recommendation:</span>

We advise revising the pausability implementation of the token.

#### <span class="major">Alleviation:</span>

The team opted to consider our references and revised the pausability implementation while also adding a "pause only once" feature. Note that any token transfers to and fro the `owner` address are still possible while the token is in a "paused" state.

<div style="page-break-after: always"></div>

### <a name="F-15"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-15: Transferring Routes

| Type          | Severity                                                                                                                     | Location                                                                                                                                                                 |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inconsistency | <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major | <span class="major">[Token.vy L327-L335](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L327-L335)</span> |

#### <span class="major">Description:</span>

The `transfer` and `transferFrom` functions are implemented differently. Such approach can lead to malicious users cherry picking the functionality they need to break the normal flow of the token. Also, the `assert` statement in [L247](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L247) is redundant as the balance of the `msg.sender` cannot underflow and `msg.sender` is mistakenly used over the `_from` parameter in [L147](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L147) and [L159](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L159).

#### <span class="major">Recommendation:</span>

We advise having both `transfer` and `transferFrom` functions calling a revised version of the internal `transfer` functionality, where additional control flow will lead to the correct state update.

#### <span class="major">Alleviation:</span>

The team opted to consider our references and used the internal `transfer` functionality to all externally-facing transfer functionality.

<div style="page-break-after: always"></div>

### <a name="F-16"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-16: Redundant State Look-Up

| Type             | Severity                                                                                                                            | Location                                                                                                                                                             |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gas Optimization | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L94](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L94)</span> |

#### <span class="informational">Description:</span>

The linked assignments redundantly uses state variables.

#### <span class="informational">Recommendation:</span>

We advise utilizing local variables or function parameters instead.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and partially removed the redundant state look-ups.

<div style="page-break-after: always"></div>

### <a name="F-17"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-17: Incorrect Math

| Type                         | Severity                                                                                                                     | Location                                                                                                                                                                                                                                                                               |
| :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inconsistency, Volatile Code | <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major | <span class="major">[Token.vy L82](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L82), [L87](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L87)</span> |

#### <span class="major">Description:</span>

The linked assignments indicate either that the contract's creator balance (also known as initial supply) is not in-line with the token's total supply or that the total token supply is stored without the decimal points. Both cases lead to a critical flaw in the project's tokenomics, as either the `owner` acquires a huge portion of the tokens and that amount is not taken into consideration in the total supply, or an incorrect total supply value is used throughout the codebase (including interaction with secondary protocols).

#### <span class="major">Recommendation:</span>

We advise to revise the arithmetic of the contract.

#### <span class="major">Alleviation:</span>

The team opted to consider our references and fixed the arithmetics of the codebase.

<div style="page-break-after: always"></div>

### <a name="F-18"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-18: Ambiguous `NatSpec` Comment

| Type          | Severity                                                                                                                            | Location                                                                                                                                                                         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inconsistency | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L311-L316](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L311-L316)</span> |

#### <span class="informational">Description:</span>

The implementation of the `setTaxes` function is not in-line with its NatSpec comment.

#### <span class="informational">Recommendation:</span>

We advise changing the implementation's numeric literal to reflect the NatSpec comment or vice-versa.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and fixed the aforementioned inconsistency.

<div style="page-break-after: always"></div>

### <a name="F-19"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-19: Redundant Check

| Type             | Severity                                                                                                                            | Location                                                                                                                                                               |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gas Optimization | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L166](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L166)</span> |

#### <span class="informational">Description:</span>

The linked `assert` statement is redundant due to [L167](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L167).

#### <span class="informational">Recommendation:</span>

We advise removing redundant code.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and removed the redundant code.

<div style="page-break-after: always"></div>

### <a name="F-20"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-20: Unused `internal` Function

| Type      | Severity                                                                                                                            | Location                                                                                                                                                                         |
| :-------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dead Code | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L178-L185](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L178-L185)</span> |

#### <span class="informational">Description:</span>

The linked functions do not affect the overall functionality of the codebase.

#### <span class="informational">Recommendation:</span>

We advise revising the existence of the linked functions.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and removed the redundant code.

<div style="page-break-after: always"></div>

### <a name="F-21"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-21: Redundant Storage

| Type             | Severity                                                                                                                            | Location                                                                                                                                                             |
| :--------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gas Optimization | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L74](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L74)</span> |

#### <span class="informational">Description:</span>

The linked state variable is not used throughout the codebase.

#### <span class="informational">Recommendation:</span>

We advise revising the existence of the linked state variable.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and removed the redundant state variable.

<div style="page-break-after: always"></div>

### <a name="F-22"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-22: Unused Returned Value

| Type                        | Severity                                                                                                                            | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inconsistency, Coding Style | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L120](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L120),[L133](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L133), [L172](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L172), [L248](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L248), [L179](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L179),[L188](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L188)</span> |

#### <span class="informational">Description:</span>

The linked invocations do not check the return value of the function calls.

#### <span class="informational">Recommendation:</span>

We advise the returned variables are either utilized or omitted from the function declaration.

#### <span class="informational">Alleviation:</span>

The team opted to consider our references and omitted the returned values to the linked functions.

<div style="page-break-after: always"></div>

### <a name="F-23"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-23: Router Unlimited Approval

| Type          | Severity                                                                                                                     | Location                                                                                                                                                       |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Volatile Code | <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor | <span class="minor">[Token.vy L194](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L194)</span> |

#### <span class="minor">Description:</span>

By giving the Uniswap router the right to use the contract's tokens (unlimited approval), bug exploits in that secondary protocol immediately affect the token. Although the Uniswap Decentralized Exchange (DEX) one of the most trustworthy web3 projects, the token is still facing risks.

#### <span class="minor">Recommendation:</span>

We advise to approve the Uniswap router for a specific amount right before invoking either `addLiquidityETH` or `swapExactTokensForETHSupportingFeeOnTransferTokens`. The code containing the aforementioned function calls is rarely used, meaning the gas saved is not worth the security implications.

#### <span class="minor">Alleviation:</span>

The team opted to consider our references and used fixed-price approvals to the router.

<div style="page-break-after: always"></div>

### <a name="F-24"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-24: Event Addition

| Type              | Severity                                                                                                                     | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Language Specific | <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor | <span class="minor">[Token.vy L282-L283](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L282-L283), [L294-L295](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L294-L295), [L307](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L307), [L319-L320](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L319-L320), [L340](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L340), [L360](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L360)</span> |

#### <span class="minor">Description:</span>

Important system values are updated, yet no event is emitted from such changes.

#### <span class="minor">Recommendation:</span>

We advise that the linked functions emit events, signifying a change in the related values.

#### <span class="minor">Alleviation:</span>

The team opted to consider our references and added events for all the important state changes.

<div style="page-break-after: always"></div>

### <a name="F-25"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-25: Privileged Ownership

| Type           | Severity                                                                                                                     | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------- | :--------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Centralization | <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor | <span class="minor">[Token.vy L307](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L307), [L319-L320](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L319-L320), [L340](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L340), [L360](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L360)</span> |

#### <span class="minor">Description:</span>

The `owner` of contract has the permission to:

- pause the token transfers,
- change the swap threshold for tax sells,
- set the tax fees and
- change the Decentralized Exchange (DEX) the token interacts with

without obtaining the consensus of the community.

#### <span class="minor">Recommendation:</span>

We advise renouncing ownership when it is the right timing, or gradually migrate to a timelock governing procedure and let the community monitor in respect of transparency considerations.

#### <span class="minor">Alleviation:</span>

The development team has acknowledged this exhibit.

<div style="page-break-after: always"></div>

### <a name="F-26"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-26: Potential Sandwich Attack

| Type          | Severity                                                                                                                            | Location                                                                                                                                                                         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Volatile Code | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">[Token.vy L196-L202](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L196-L202)</span> |

#### <span class="informational">Description:</span>

Potential sandwich attacks could happen if calling `uniswapV2Router.swapExactTokensForETHSupportingFeeOnTransferTokens` without slippage control.

#### <span class="informational">Recommendation:</span>

We recommend using an oracle to get an estimation of prices and setting minimum amounts based on the prices when calling the aforementioned functions.

#### <span class="informational">Alleviation:</span>

The development team has acknowledged this exhibit.

<div style="page-break-after: always"></div>

### <a name="F-27"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-27: Inexistent Input Sanitization

| Type          | Severity                                                                                                                     | Location                                                                                                                                                                                                                                                                                   |
| :------------ | :--------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Logical Issue | <span style="background-color: dodgerblue; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Minor | <span class="minor">[Token.vy L329](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L329), [L340](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L340)</span> |

#### <span class="minor">Description:</span>

The linked assignments update state variables without prior checks to the values of the arguments.

#### <span class="minor">Recommendation:</span>

We advise adding an `assert` statement, checking the input values against the `ZERO_ADDRESS`.

#### <span class="minor">Alleviation:</span>

The team opted to consider our references and added `assert` statements to check the input value.

## <div style="page-break-after: always"></div>

### <a name="F-28"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-28: Third Party Dependencies

| Type         | Severity                                                                                                                            | Location                                   |
| :----------- | :---------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------- |
| Control Flow | <span style="background-color: limegreen; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Informational | <span class="informational">General</span> |

#### <span class="informational">Description:</span>

The contract is serving as the underlying entity to interact with third party Uniswap protocol. We treat those third party entities as black boxes and assume its functional correctness. However in the real world, third parties may be compromised that led to assets lost or stolen.

#### <span class="informational">Recommendation:</span>

We encourage the team to constantly monitor the statuses of those third parties, i.e. Uniswap protocol, to mitigate the side effects when unexpected activities are observed.

#### <span class="informational">Alleviation:</span>

The development team has acknowledged this exhibit.

## <div style="page-break-after: always"></div>

### <a name="F-29"><img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/></a> F-29: Ambiguous Limit Change

| Type                         | Severity                                                                                                                     | Location                                                                                                                                                                 |
| :--------------------------- | :--------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Inconsistency, Volatile Code | <span style="background-color: darkorange; border-radius: 50%; display: inline-block; height: 8pt; width: 8pt"></span> Major | <span class="major">[Token.vy L354-L361](https://github.com/protectourchoice/contract/blob/8fc2f1fe98700fa48dc6bd42fb3b576a976a461f/contracts/Token.vy#L354-L361)</span> |

#### <span class="major">Description:</span>

The `walletCap` state variable is not updated proportionally to the `txLimit` one.

#### <span class="major">Recommendation:</span>

We advise revising the aforementioned function.

#### <span class="major">Alleviation:</span>

The team opted to consider our references and changed the values of both `txLimit` & `walletCap` state variables in the linked function.

## <img src="https://i.ibb.co/NFtf2HY/logo-removebg-preview.png" style="height: 28pt; filter: invert(0)"/> Disclaimer

Reports made by Ourovoros are not to be considered as a recommendation or approval of any particular project or team. Security reviews made by Ourovoros for any project or team are not to be taken as a depiction of the value of the “product” or “asset” that is being reviewed.

Ourovoros reports are not to be considered as a guarantee of the bug-free nature of the technology analyzed and should not be used as an investment decision with any particular project. They represent an extensive auditing process intending to help our customers increase the quality of their code while reducing the high level of risk presented by cryptographic tokens and blockchain technology.

Each company and individual is responsible for their own due diligence and continuous security. Our goal is to help reduce the attack parameters and the high level of variance associated with utilizing new and consistently changing technologies, and in no way claim any guarantee of security or functionality of the technology we agree to analyze.
