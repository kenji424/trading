pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/Context.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract IssueNFT is Context, ERC721Enumerable, Ownable {
    constructor(
        string memory name,
        string memory symbol
    ) ERC721(name, symbol) {}

    function mint(address to) public virtual {
        _mint(to, totalSupply());
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        return string();
    }    

}
