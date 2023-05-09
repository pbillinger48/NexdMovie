import { FaBars } from "react-icons/fa";
import { NavLink as Link } from "react-router-dom";
import styled from "styled-components";
  
export const Nav = styled.nav`
  background: #282c34;
  height: 85px;
  display: flex;
`;
  
export const NavLink = styled(Link)`
  color: white;
  display: flex;
  align-items: center;
  text-decoration: none;
  padding: 0 1rem;
  height: 100%;
  cursor: pointer;
  &.active {
    color: #ff8000;
  }
`;
  
export const NavMenu = styled.div`
  display: flex; 
  @media screen and (max-width: 768px) {
    display: none;
  }
`;