import React from 'react'
import { Card } from 'react-bootstrap'
import { Link } from 'react-router-dom'

export default function Product(props) {
  return (
    <>
      <Card className='my-3 p-3 rounded'>
        <Link to={`/product/${props.Product._id}`}>
          <Card.Img src={props.Product.image} />
        </Link>
        <Card.Body>
          <Link to={`/product/${props.Product._id}`} className='text-dark text-decoration-none'>
            <Card.Title as='h3'>
              {props.Product.productname}
            </Card.Title>
          </Link>

          <Card.Text>
            <span className='my-3'>
            <i className="fa-solid fa-star" style={{ color: 'gold' }}></i> {props.Product.rating} from {props.Product.numReviews} Review
            </span>
          </Card.Text>
          <Card.Text as='h6'>
             Rs. {props.Product.price}
          </Card.Text>
        </Card.Body>
      </Card>
    </>
  )
}