import React from 'react'
import Navbar from './Navbar'
// import Footer from './Footer'
import Cart from './Cart'
import Homescreen from './Screen/Homescreen'
import Loginscreen from './Screen/Loginscreen'
import Signupscreen from './Screen/Signupscreen'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import ProductScreen from './Screen/ProductScreen'

export default function App() {
  return (
    <Router>
        <Navbar />
        <Routes>
          <Route exact path="/" element={<Homescreen/>} />
          <Route exact path="/cart" element={<Cart/>} />
          <Route exact path="/login" element={<Loginscreen/>} />
          <Route exact path="/signup" element={<Signupscreen/>} />
          <Route exact path="/product/:id" element={<ProductScreen/>} />
        </Routes>
        {/* <Footer /> */}
    </Router>
  )
}