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
  &:hover {
    font-size: 1.3em;
    img {
      transform: scale(1.1);
    }
  }
  &.active {
    color: #ff8000;
  }
  img {
    transition: all 0.1s ease-in-out;
  }
`;
  
export const NavMenu = styled.div`
  display: flex; 
  @media screen and (max-width: 768px) {
    display: none;
  }
`;