import React from 'react'
import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav className="navbar navbar-expand-lg bg-dark navbar-dark">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/"><h5>Ecommerce-Cart</h5></Link>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <Link className="nav-link" to="/">Home <i className="fa-solid fa-house"></i></Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/cart">Cart</Link>
            </li>
            <li className="nav-item dropdown">
              <Link className="nav-link dropdown-toggle" to="/" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                New User?
              </Link>
              <ul className="dropdown-menu">
                <li><Link className="dropdown-item" to="/login">Login</Link></li>
                <li><Link className="dropdown-item" to="/signup">Signup</Link></li>
                <li><hr className="dropdown-divider"/></li>
                <li><Link className="dropdown-item" to="/logout">Logout</Link></li>
              </ul>
            </li>
          </ul>
          <form className="d-flex" role="search">
            <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
            <button className="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
  )
}
