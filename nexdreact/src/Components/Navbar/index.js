/*
This creates the navigation bar that will be at top of page
*/
import React from "react";
import logo from "./NexdMovieClear.png";
import { Nav, NavLink, NavMenu } 
    from "./NavbarElements";
  
const Navbar = () => {
  return (
    <>
      <Nav>
        <NavMenu>
          <NavLink to ="/">
            <img src={logo} alt="logo" width="200" />
          </NavLink>
          <NavLink to="/about" activeStyle>
            About
          </NavLink>
        </NavMenu>
      </Nav>
    </>
  );
};
  
export default Navbar;