import { Col, Row, Container, Card, Image, ListGroup } from 'react-bootstrap'
import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { useParams, Link } from 'react-router-dom'


function ProductScreen(params) {
  const { id } = useParams()
  const [products, setProducts] = useState([])

  useEffect(() => {
    async function fetchProducts() {
      const {data} = await axios.get(`/api/products/${id}`)
      // console.log(data.data)
      setProducts(data)

    }
    fetchProducts()
  }, [id])

  let extract_str = (str) => {
    let a = [];
    let split_str = str.split(' ')
    for (let i = 0; i < 26; i++) {
      a.push(split_str[i])
    }
    let val = a.toString()
    return val.replaceAll(',', ' ');
  }

  return (
    <Container>
      <Link to='/'>
        <button className='btn btn-dark my-3'><i className="fa-solid fa-arrow-left"></i> Go Back</button>
      </Link>
      <Row>
        <Col md={6}>
          <Image src={products.image} alt={products.productname} fluid />
        </Col>

        <Col md={3}>
          <ListGroup>
            <ListGroup.Item className='h2'>{products.productname}</ListGroup.Item>
            <ListGroup.Item><i className="fa-solid fa-star" style={{ color: 'gold' }}></i> {products.rating} from {products.numReviews} <strong>Review</strong></ListGroup.Item>
            <ListGroup.Item>Rs. <strong>{products.price}</strong></ListGroup.Item>
            <ListGroup.Item>{products.productinfo ? extract_str(products.productinfo) : 'not available'}...</ListGroup.Item>
          </ListGroup>
        </Col>

        <Col md={3}>
          <Card>
          <ListGroup>
          <ListGroup.Item>
            <Row>
              <Col>Price:</Col>
              <Col><strong>Rs. {products.price}</strong></Col>
            </Row>
          </ListGroup.Item>

          <ListGroup.Item>
            <Row>
              <Col>Stock:</Col>
              <Col>{products.stockcount>0 ? 'InStock':'OutStock'}</Col>
            </Row>
          </ListGroup.Item>

          <ListGroup.Item>
            <Row>
              <Col><button className='btn btn-success' disabled={products.stockcount===0}>Add to Cart</button></Col>
            </Row>
          </ListGroup.Item>
          </ListGroup>
          </Card>
        </Col>
      </Row>
    </Container >
  )
}
export default ProductScreen;


/*{<ListGroup>
<ListGroup.Item>price:  {products.price}</ListGroup.Item>
<ListGroup.Item>status: {products.stockcount > 0 ? 'In Stock': 'Out Stock'}</ListGroup.Item>
<ListGroup.Item><button className='btn btn-success' disabled={products.stockcount==0}>Buy Now!</button></ListGroup.Item>
</ListGroup>}*/