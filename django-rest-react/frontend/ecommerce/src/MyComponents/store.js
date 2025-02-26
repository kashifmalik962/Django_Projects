import {createStore, combineReducers, applyMiddleware} from 'redux'
import thunk from 'redux-thunk'
import {composeWithDevTools} from 'redux-devtools-extension'
import { productsListReducers } from './reducers/productReducers'

const reducer = combineReducers({
    productList: productsListReducers
})

const initialSate={}
const middleware=[thunk]
const store = createStore(reducer, initialSate, composeWithDevTools(applyMiddleware(...middleware)))

export default store;