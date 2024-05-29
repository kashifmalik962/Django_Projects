import React, { useEffect } from 'react'
import { Container } from 'react-bootstrap'
// import axios from 'axios'
import {Row,Col} from 'react-bootstrap'
import Product from '../Product'
import { list_product } from '../actions/productActions'
import {useDispatch, useSelector} from 'react-redux'

function HomeScreen() {
    const dispatch = useDispatch()
    const productList = useSelector((state)=>state.productList)
    const {error, loading, products} = productList
    
    useEffect(() => {
        dispatch(list_product())
    },[dispatch])
    console.log(products)
  return (
    <>
    <Container>
        <br/>
        <h1>Products</h1>
        <br/>
        <Row>
            {products.map((products)=>(
                <Col key={products._id} sm={12} md={6} lg={4} xl={3}>
                    <Product Product={products}/>
                </Col>
            ))}
        </Row>
    </Container>
    </>
  )
}

export default HomeScreen;


// Dependency Array in useEffect: You should specify a dependency array as the second argument of useEffect to avoid unintentional infinite re-renders. Since you're fetching data inside useEffect, you should also pass an empty dependency array ([]) to ensure it only runs once when the component mounts.